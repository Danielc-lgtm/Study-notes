[CmdletBinding()]
param(
    [string]$RepoRoot = (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)),
    [switch]$ConfigOnly
)

# Read-only structural checks. This does not judge mathematical correctness,
# self-containedness, selection quality, or whether a linked heading exists.
$ErrorActionPreference = 'Stop'
$problems = [System.Collections.Generic.List[string]]::new()
$skillCount = 0
$exerciseCount = 0
$previewCount = 0
$indexCount = 0
$linkCount = 0
$tablePageCount = 0

function Add-Problem([string]$Message) { $problems.Add($Message) }

function Read-Markdown([string]$Path) {
    $raw = [System.IO.File]::ReadAllText($Path).TrimStart([char]0xFEFF)
    $metadata = @{}
    $body = $raw
    $yaml = ''
    $front = [regex]::Match($raw, '\A---\r?\n(?<yaml>[\s\S]*?)\r?\n---(?:\r?\n|\z)')
    if ($front.Success) {
        $yaml = $front.Groups['yaml'].Value
        $body = $raw.Substring($front.Length)
        foreach ($line in ($yaml -split '\r?\n')) {
            if ($line -match '^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$') {
                $metadata[$Matches[1]] = $Matches[2].Trim().Trim('"', "'")
            }
        }
    }
    [pscustomobject]@{ Path = $Path; Raw = $raw; Metadata = $metadata; Yaml = $yaml; Body = ($body -replace "`r`n", "`n") }
}

function Remove-CodeFences([string]$Body) {
    # Handles ordinary and quoted fences so code samples do not become links/headings.
    $result = [System.Collections.Generic.List[string]]::new()
    $fenceCharacter = ''
    $fenceLength = 0
    foreach ($line in ($Body -split '\r?\n')) {
        $unquoted = $line -replace '^\s*(?:>\s?)*', ''
        $fence = [regex]::Match($unquoted, '^(`{3,}|~{3,})')
        if ($fenceCharacter) {
            if ($fence.Success -and $fence.Value[0].ToString() -eq $fenceCharacter -and $fence.Length -ge $fenceLength -and $unquoted.Substring($fence.Length).Trim() -eq '') {
                $fenceCharacter = ''
            }
            $result.Add((' ' * $line.Length))
            continue
        }
        if ($fence.Success) {
            $fenceCharacter = $fence.Value[0].ToString()
            $fenceLength = $fence.Length
            $result.Add((' ' * $line.Length))
            continue
        }
        # Preserve character offsets so later section checks can inspect original text.
        $withoutInlineCode = [regex]::Replace($line, '(`+)(.*?)\1', { param($match) ' ' * $match.Length })
        $result.Add($withoutInlineCode)
    }
    return ($result -join "`n")
}

function Get-TableLine([string]$Line) {
    $prefix = [regex]::Match($Line, '^\s*(?:>\s?)*')
    [pscustomobject]@{
        Depth = ([regex]::Matches($prefix.Value, '>')).Count
        Text = $Line.Substring($prefix.Length).Trim()
    }
}

function Test-UnescapedPipe([string]$Text, [int]$Position) {
    $slashes = 0
    for ($offset = $Position - 1; $offset -ge 0 -and $Text[$offset] -eq '\'; $offset--) { $slashes++ }
    return ($slashes % 2 -eq 0)
}

function Check-TableLinks([string]$Visible, [string]$Label) {
    # A file target can exist while Markdown splits the link across table cells.
    # Detect real tables by their delimiter row, including tables in callouts.
    $lines = @($Visible -split '\r?\n')
    $rows = [System.Collections.Generic.HashSet[int]]::new()
    for ($i = 1; $i -lt $lines.Count; $i++) {
        $delimiter = Get-TableLine $lines[$i]
        if ($delimiter.Text -notmatch '\|' -or $delimiter.Text -notmatch '^\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?$') { continue }
        $header = Get-TableLine $lines[$i - 1]
        if (!$header.Text -or $header.Depth -ne $delimiter.Depth) { continue }
        [void]$rows.Add($i - 1)
        for ($j = $i + 1; $j -lt $lines.Count; $j++) {
            $row = Get-TableLine $lines[$j]
            if (!$row.Text -or $row.Depth -ne $delimiter.Depth -or $row.Text -notmatch '\|') { break }
            [void]$rows.Add($j)
        }
    }
    foreach ($rowNumber in @($rows | Sort-Object)) {
        foreach ($link in [regex]::Matches($lines[$rowNumber], '\[\[([^\]\r\n]+)\]\]')) {
            for ($position = 0; $position -lt $link.Value.Length; $position++) {
                if ($link.Value[$position] -eq '|' -and (Test-UnescapedPipe $link.Value $position)) {
                    Add-Problem "$Label body line $($rowNumber + 1) has an unescaped pipe inside a table wikilink/embed: $($link.Value). Use \| inside table links."
                    break
                }
            }
        }
    }
}

function Normalize-Path([string]$Path) {
    return [System.IO.Path]::GetFullPath($Path).TrimEnd('\', '/')
}

function Is-Within([string]$Path, [string]$Root) {
    $candidate = Normalize-Path $Path
    $base = Normalize-Path $Root
    return $candidate.Equals($base, [System.StringComparison]::OrdinalIgnoreCase) -or $candidate.StartsWith($base + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)
}

function Is-ManagedContentPath([string]$Path) {
    $relative = (Normalize-Path $Path).Substring($exerciseRoot.Length).TrimStart('\', '/')
    foreach ($part in ($relative -split '[/\\]')) {
        if ($part.StartsWith('.') -or $part -in @('attachments', 'assets', 'tools', 'node_modules')) { return $false }
    }
    return $true
}

function Resolve-WikiTarget([string]$Target, [string]$SourcePath) {
    # Markdown removes the escaping before Obsidian interprets a table alias.
    $Target = $Target.Replace('\|', '|')
    $targetFile = (($Target -split '\|', 2)[0] -split '#', 2)[0].Trim()
    if (!$targetFile) { return $SourcePath }
    $targetFile = $targetFile -replace '/', [System.IO.Path]::DirectorySeparatorChar
    $extensions = @('')
    if (![System.IO.Path]::GetExtension($targetFile)) { $extensions = @('.md', '') }
    foreach ($base in @($vaultRoot, (Split-Path -Parent $SourcePath))) {
        foreach ($extension in $extensions) {
            $candidate = Normalize-Path (Join-Path $base ($targetFile + $extension))
            if ((Is-Within $candidate $vaultRoot) -and (Test-Path -LiteralPath $candidate -PathType Leaf)) { return $candidate }
        }
    }
    # Obsidian also supports unique shortest paths. Ambiguous targets fail visibly.
    $suffixes = @($extensions | ForEach-Object { [System.IO.Path]::DirectorySeparatorChar + $targetFile + $_ })
    $matchesFound = @($vaultFiles | Where-Object {
        $file = $_
        @($suffixes | Where-Object { $file.EndsWith($_, [System.StringComparison]::OrdinalIgnoreCase) }).Count -gt 0
    })
    if ($matchesFound.Count -eq 1) { return $matchesFound[0] }
    return $null
}

function Check-Exercise($Page, [string]$Label) {
    $mode = $Page.Metadata['mode']
    if ($mode -notin @('algorithmic', 'competitive-programming', 'interdisciplinary', 'frontier-rediscovery')) {
        Add-Problem "$Label has no recognized exercise mode."
        return
    }
    $dagValue = $Page.Metadata['dag_nodes']
    $blockList = [regex]::IsMatch($Page.Yaml, '(?m)^dag_nodes:\s*\r?\n(?:[ \t]*\r?\n)*[ \t]+-\s+\S')
    if (!$Page.Metadata.ContainsKey('dag_nodes') -or !($dagValue -match '^\[.*\]$' -or $blockList)) {
        Add-Problem "$Label must provide dag_nodes as a YAML list (an empty list is allowed)."
    }
    $inlineContents = ($dagValue -replace '^\[|\]$', '').Trim(' ', "'", '"', ',')
    if ($Page.Metadata['type'] -ne 'format-preview' -and $mode -in @('interdisciplinary', 'frontier-rediscovery') -and !$blockList -and [string]::IsNullOrWhiteSpace($inlineContents)) {
        Add-Problem "$Label needs at least one dag_nodes entry for mode '$mode'."
    }
    $visible = Remove-CodeFences $Page.Body
    $headings = @([regex]::Matches($visible, '(?m)^## (.+?)[ \t]*$') | ForEach-Object { $_.Groups[1].Value })
    $expected = if ($mode -in @('algorithmic', 'competitive-programming')) { @('Problem', 'Solution') } else { @('Context', 'Problem', 'Solution') }
    if (($headings -join '|') -cne ($expected -join '|')) {
        Add-Problem "$Label must have exactly these unquoted level-2 sections: $($expected -join ', ')."
    }
    $solution = [regex]::Match($visible, '(?m)^## Solution[ \t]*$')
    $insights = [regex]::Matches($visible, '(?im)^\*\*insight:\*\*[^\r\n]*')
    $feedbacks = [regex]::Matches($visible, '(?im)^\*\*feedback:\*\*[^\r\n]*')
    if ($insights.Count -ne 1 -or !$solution.Success -or $insights[0].Index -ge $solution.Index) {
        Add-Problem "$Label needs one unquoted **insight:** field before Solution."
    }
    if ($feedbacks.Count -ne 1 -or !$solution.Success -or $feedbacks[0].Index -le $solution.Index) {
        Add-Problem "$Label needs one unquoted **feedback:** field after the collapsed solution."
    }
    if (!$solution.Success -or $feedbacks.Count -ne 1 -or $feedbacks[0].Index -le $solution.Index) { return }
    $solutionBody = $Page.Body.Substring($solution.Index + $solution.Length, $feedbacks[0].Index - $solution.Index - $solution.Length).Trim()
    if ([regex]::IsMatch($solutionBody, '(?m)^[ \t]*$')) {
        Add-Problem "$Label has a bare blank line inside the solution callout; prefix blank callout lines with >."
    }
    $solutionLines = @($solutionBody -split '\r?\n' | Where-Object { $_.Trim() -ne '' })
    if ($solutionLines.Count -lt 2 -or $solutionLines[0] -notmatch '^>\s*\[!note\]-\s+Full solution\s*$') {
        Add-Problem "$Label needs a default-collapsed '> [!note]- Full solution' callout with content."
    }
    if (@($solutionLines | Where-Object { $_ -notmatch '^>' }).Count -gt 0) {
        Add-Problem "$Label has solution text outside its collapsed callout."
    }
    if (@($solutionLines | Select-Object -Skip 1 | Where-Object { $_ -match '^>\s*\S' }).Count -eq 0) {
        Add-Problem "$Label has an empty solution callout."
    }
}

try {
    $RepoRoot = Normalize-Path $RepoRoot
    if (!(Test-Path -LiteralPath $RepoRoot -PathType Container)) { throw "Repository folder does not exist: $RepoRoot" }
    $required = @('AGENTS.md', '.codex/config.toml', '.codex/README.md', '.codex/standards.md', '.codex/exercise-format.md', '.codex/selection.md', '.codex/feedback.md', '.codex/current-task.md')
    foreach ($relative in $required) {
        $path = Join-Path $RepoRoot $relative
        if (!(Test-Path -LiteralPath $path -PathType Leaf)) { Add-Problem "Missing required file: $relative" }
        elseif ([string]::IsNullOrWhiteSpace([System.IO.File]::ReadAllText($path))) { Add-Problem "Required file is empty: $relative" }
    }
    $configPath = Join-Path $RepoRoot '.codex/config.toml'
    if ((Test-Path -LiteralPath $configPath -PathType Leaf) -and ![regex]::IsMatch([System.IO.File]::ReadAllText($configPath), '(?m)^\s*web_search\s*=\s*["'']live["'']\s*(?:#.*)?$')) {
        Add-Problem '.codex/config.toml must enable web_search = "live" for current contest/research verification.'
    }
    foreach ($name in @('algorithmic-exercises', 'interdisciplinary-exercises', 'frontier-rediscovery', 'active-research')) {
        $relative = ".agents/skills/$name/SKILL.md"
        $path = Join-Path $RepoRoot $relative
        if (!(Test-Path -LiteralPath $path -PathType Leaf)) { Add-Problem "Missing required skill: $relative"; continue }
        $skillCount++
        $page = Read-Markdown $path
        if ($page.Metadata['name'] -cne $name) { Add-Problem "$relative frontmatter name must equal '$name'." }
        if ([string]::IsNullOrWhiteSpace($page.Metadata['description'])) { Add-Problem "$relative needs a nonempty frontmatter description." }
        if ($page.Raw -match '(?i)\.claude[/\\]skills|(?m)^\s*(?:See|Read|Follow|Load|Use)\b[^\r\n]*\bCLAUDE\.md\b') { Add-Problem "$relative contains a Claude instruction dependency; Codex skills must stand alone." }
    }
    if (!$ConfigOnly) {
        $vaultRoot = Normalize-Path (Join-Path $RepoRoot 'Study notes')
        $exerciseRoot = Normalize-Path (Join-Path $vaultRoot 'exercises')
        if (!(Test-Path -LiteralPath (Join-Path $vaultRoot 'Prerequisite DAG.md') -PathType Leaf)) { Add-Problem 'Missing vault prerequisite DAG: Study notes/Prerequisite DAG.md' }
        if (!(Test-Path -LiteralPath $exerciseRoot -PathType Container)) { Add-Problem 'Missing managed exercise folder: Study notes/exercises' }
        else {
            $vaultFiles = @(Get-ChildItem -LiteralPath $vaultRoot -Recurse -File | ForEach-Object { Normalize-Path $_.FullName })
            # The escaping defect can affect existing subject notes as well as indexes.
            # Audit table syntax throughout the vault; broader link/schema checks stay
            # scoped to the managed exercise tree so unrelated legacy notes are valid.
            foreach ($file in $vaultFiles) {
                $relativeVaultPath = $file.Substring($vaultRoot.Length + 1)
                if ([IO.Path]::GetExtension($file) -ine '.md' -or $relativeVaultPath -match '(^|[\\/])(?:\.[^\\/]+|attachments|assets|tools|node_modules)([\\/]|$)') { continue }
                $tablePageCount++
                $rawTableCandidate = [IO.File]::ReadAllText($file)
                # Most notes have no tables. Avoid tokenizing their prose line by line.
                $delimiterPattern = '(?m)^[ \t]*(?:>[ \t]*)*(?=[^\r\n]*\|)\|?[ \t]*:?-{2,}:?[ \t]*(?:\|[ \t]*:?-{2,}:?[ \t]*)*\|?[ \t]*\r?$'
                if (!$rawTableCandidate.Contains('[[') -or ![regex]::IsMatch($rawTableCandidate, $delimiterPattern)) { continue }
                $tablePage = Read-Markdown $file
                Check-TableLinks (Remove-CodeFences $tablePage.Body) ($file.Substring($RepoRoot.Length + 1))
            }
            $pages = @(Get-ChildItem -LiteralPath $exerciseRoot -Recurse -File -Filter '*.md' | Where-Object { Is-ManagedContentPath $_.FullName } | ForEach-Object { Read-Markdown $_.FullName })
            $indexes = @{}
            $pageLinks = @{}
            foreach ($page in $pages) {
                $label = $page.Path.Substring($RepoRoot.Length + 1)
                if ($page.Metadata['type'] -notin @('index', 'exercise', 'format-preview', 'research-roadmap', 'concept')) { Add-Problem "$label needs a recognized page type: index, exercise, format-preview, research-roadmap, or concept." }
                $visible = Remove-CodeFences $page.Body
                $resolvedLinks = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
                foreach ($link in [regex]::Matches($visible, '\[\[([^\]\r\n]+)\]\]')) {
                    $linkCount++
                    $target = Resolve-WikiTarget $link.Groups[1].Value $page.Path
                    if (!$target) { Add-Problem "$label has a missing or ambiguous wikilink: $($link.Value)" }
                    else { [void]$resolvedLinks.Add($target) }
                }
                $pageLinks[$page.Path] = $resolvedLinks
                if ($page.Metadata['type'] -in @('exercise', 'format-preview')) {
                    if ($page.Metadata['type'] -eq 'exercise') { $exerciseCount++ } else { $previewCount++ }
                    Check-Exercise $page $label
                }
                if ($page.Metadata['type'] -eq 'index') {
                    $indexCount++
                    $folderValue = $page.Metadata['indexed_folder']
                    if ([string]::IsNullOrWhiteSpace($folderValue) -or [System.IO.Path]::IsPathRooted($folderValue)) { Add-Problem "$label needs a vault-relative indexed_folder."; continue }
                    $folder = Normalize-Path (Join-Path $vaultRoot $folderValue)
                    if (!(Is-Within $folder $exerciseRoot) -or !(Test-Path -LiteralPath $folder -PathType Container) -or !(Is-ManagedContentPath $folder)) { Add-Problem "$label indexes a nonexistent/excluded folder or a folder outside exercises: $folderValue"; continue }
                    if ($indexes.ContainsKey($folder)) { Add-Problem "Multiple indexes cover $folderValue`: $($indexes[$folder]) and $label" }
                    else { $indexes[$folder] = $page.Path }
                    if ($resolvedLinks.Contains($page.Path)) { Add-Problem "$label contains an unnecessary self-link." }
                }
            }
            $folders = @($exerciseRoot) + @(Get-ChildItem -LiteralPath $exerciseRoot -Directory -Recurse | Where-Object { Is-ManagedContentPath $_.FullName } | ForEach-Object { Normalize-Path $_.FullName })
            foreach ($folder in $folders) {
                $folderLabel = $folder.Substring($vaultRoot.Length + 1)
                if (!$indexes.ContainsKey($folder)) { Add-Problem "No index covers folder: $folderLabel"; continue }
                $indexPath = $indexes[$folder]
                $links = $pageLinks[$indexPath]
                foreach ($file in @(Get-ChildItem -LiteralPath $folder -File -Filter '*.md' | Where-Object { Is-ManagedContentPath $_.FullName })) {
                    if ($file.FullName -ne $indexPath -and !$links.Contains($file.FullName)) { Add-Problem "Index '$([System.IO.Path]::GetFileName($indexPath))' omits direct page: $folderLabel/$($file.Name)" }
                }
                foreach ($child in @(Get-ChildItem -LiteralPath $folder -Directory | Where-Object { Is-ManagedContentPath $_.FullName })) {
                    if ($indexes.ContainsKey($child.FullName) -and $indexes[$child.FullName] -ne $indexPath -and !$links.Contains($indexes[$child.FullName])) { Add-Problem "Index '$([System.IO.Path]::GetFileName($indexPath))' omits the index for child folder: $($child.Name)" }
                }
                if ($folder -ne $exerciseRoot) {
                    $parentFolder = Normalize-Path (Split-Path -Parent $folder)
                    if ($indexes.ContainsKey($parentFolder) -and !$links.Contains($indexes[$parentFolder])) { Add-Problem "Index '$([System.IO.Path]::GetFileName($indexPath))' omits its parent-folder index link." }
                }
            }
        }
    }
}
catch { Add-Problem "Validation could not finish: $($_.Exception.Message)" }

if ($problems.Count -gt 0) {
    Write-Output "FAIL: $($problems.Count) setup issue(s)."
    foreach ($problem in $problems) { Write-Output "- $problem" }
    exit 1
}
if ($ConfigOnly) { Write-Output "PASS: $($required.Count) configuration files and $skillCount skills. Vault/content checks skipped (-ConfigOnly)." }
else { Write-Output "PASS: $($required.Count) configuration files, $skillCount skills, $indexCount folder indexes, $exerciseCount exercises, $previewCount format previews, $linkCount managed wikilinks; table-link syntax checked in $tablePageCount vault notes. File targets checked for managed notes; heading/block anchors and mathematical quality require manual review." }
exit 0
