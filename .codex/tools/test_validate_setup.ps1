[CmdletBinding()]
param(
    [string]$ValidatorPath = (Join-Path $PSScriptRoot 'validate_setup.ps1'),
    [switch]$KeepFixture
)

# End-to-end regressions for Obsidian wikilinks in Markdown tables.
# Uses only PowerShell and disposable local fixtures; no repository data or Pester.
$ErrorActionPreference = 'Stop'
$fixtureRoot = $null
$passed = 0

function Write-FixtureFile([string]$RelativePath, [string]$Content) {
    $destination = Join-Path $fixtureRoot $RelativePath
    [void](New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force)
    [System.IO.File]::WriteAllText($destination, $Content)
}

function Run-Case(
    [string]$Name,
    [int]$ExpectedExit,
    [string]$ExpectedMessage,
    [string]$ConceptBody,
    [string]$MasterBody = $defaultMasterBody,
    [string]$ForbiddenMessage = ''
) {
    Write-FixtureFile 'Study notes/exercises/Exercises Index.md' ($masterFrontmatter + $MasterBody)
    Write-FixtureFile 'Study notes/exercises/algorithmic/Target.md' ($conceptFrontmatter + $ConceptBody)
    $output = @(& $shellExecutable -NoProfile -File $ValidatorPath -RepoRoot $fixtureRoot 2>&1)
    $actualExit = $LASTEXITCODE
    $message = $output -join "`n"
    if ($actualExit -ne $ExpectedExit -or $message -notmatch $ExpectedMessage -or ($ForbiddenMessage -and $message -match $ForbiddenMessage)) {
        throw "Case '$Name' expected exit $ExpectedExit and /$ExpectedMessage/; received exit $actualExit.`n$message"
    }
    $script:passed++
    Write-Output "PASS: $Name (validator exit $actualExit)"
}

try {
    $ValidatorPath = [System.IO.Path]::GetFullPath($ValidatorPath)
    if (!(Test-Path -LiteralPath $ValidatorPath -PathType Leaf)) { throw "Validator does not exist: $ValidatorPath" }
    $shellName = if ($PSVersionTable.PSEdition -eq 'Core') { 'pwsh.exe' } else { 'powershell.exe' }
    $shellExecutable = Join-Path $PSHOME $shellName
    if (!(Test-Path -LiteralPath $shellExecutable -PathType Leaf)) { throw "PowerShell executable does not exist: $shellExecutable" }
    $tempBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath()).TrimEnd('\', '/')
    $fixtureRoot = Join-Path $tempBase ('codex-validate-links-' + [guid]::NewGuid().ToString('N'))
    [void](New-Item -ItemType Directory -Path $fixtureRoot)

    foreach ($relative in @('AGENTS.md', '.codex/README.md', '.codex/standards.md', '.codex/exercise-format.md', '.codex/selection.md', '.codex/feedback.md', '.codex/current-task.md')) {
        Write-FixtureFile $relative 'Local regression fixture configuration.'
    }
    Write-FixtureFile '.codex/config.toml' 'web_search = "live"'
    foreach ($name in @('algorithmic-exercises', 'interdisciplinary-exercises', 'frontier-rediscovery', 'active-research')) {
        Write-FixtureFile ".agents/skills/$name/SKILL.md" "---`nname: $name`ndescription: Independent fixture instructions.`n---`n# Fixture skill`n"
    }
    Write-FixtureFile 'Study notes/Prerequisite DAG.md' '# Fixture prerequisite DAG'

    $masterFrontmatter = "---`ntype: index`nindexed_folder: exercises`n---`n# Exercises`n`n"
    $conceptFrontmatter = "---`ntype: concept`n---`n# Target`n`n"
    $defaultMasterBody = "[[exercises/Algorithmic Index|Algorithmic]]`n"
    Write-FixtureFile 'Study notes/exercises/Algorithmic Index.md' @'
---
type: index
indexed_folder: exercises/algorithmic
---
# Algorithmic Index

Parent: [[exercises/Exercises Index|Exercises]]

[[exercises/algorithmic/Target|Target concept]]
'@
    # File existence is all the validator needs; this is a fixture, not rendered media.
    Write-FixtureFile 'Study notes/exercises/assets/fixture.png' 'Fixture attachment.'

    Run-Case 'baseline fixture and raw aliases outside tables' 0 '^PASS:' @'
Ordinary prose: [[exercises/Algorithmic Index|Collection]].

An ordinary embed: ![[exercises/assets/fixture.png|120]].
'@

    # Exact original three-column header/separator and first corrupted master row.
    # The other categories are omitted to keep the fixture at two genuine indexes.
    $originalThreeColumn = @'
| Collection                                | What you can do here      |                                                                                   |
| ----------------------------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| [[exercises/Algorithmic Index             | Algorithmic]]             | Reconstruct algorithms and data structures from their required behavior.          |
'@
    Run-Case 'original split-alias three-column master table rejected' 1 'unescaped' 'Fixture concept.' $originalThreeColumn

    $originalTwoColumn = @'
| Collection | What you can do here |
| --- | --- |
| [[exercises/Algorithmic Index|Algorithmic]] | Reconstruct algorithms and data structures from their required behavior. |
'@
    Run-Case 'original raw-alias two-column master table rejected' 1 'unescaped' 'Fixture concept.' $originalTwoColumn

    $escapedTwoColumn = @'
| Collection | What you can do here |
| --- | --- |
| [[exercises/Algorithmic Index\|Algorithmic]] | Reconstruct algorithms and data structures from their required behavior. |
'@
    Run-Case 'escaped alias in master table resolves and passes' 0 '^PASS:' 'Fixture concept.' $escapedTwoColumn

    Run-Case 'plain wikilinks without aliases in a table pass' 0 '^PASS:' @'
| Page | Description |
| --- | --- |
| [[exercises/Algorithmic Index]] | Collection index. |
'@

    Run-Case 'legitimate three-column table passes' 0 '^PASS:' @'
| Page | Type | Description |
| :--- | :---: | ---: |
| [[exercises/Algorithmic Index\|Collection]] | Index | Navigate exercises. |
| [[Prerequisite DAG]] | Study map | Find a subject. |
'@

    Run-Case 'raw alias in table header rejected' 1 'unescaped' @'
| [[exercises/Algorithmic Index|Collection]] | Description |
| --- | --- |
| Plain text | Some description. |
'@

    Run-Case 'raw alias in quoted callout table rejected' 1 'unescaped' @'
> [!note]- Example
> | Page | Description |
> | --- | --- |
> | [[exercises/Algorithmic Index|Collection]] | Collection index. |
'@

    Run-Case 'escaped alias in quoted callout table passes' 0 '^PASS:' @'
> [!note]- Example
> | Page | Description |
> | --- | --- |
> | [[exercises/Algorithmic Index\|Collection]] | Collection index. |
'@

    Run-Case 'raw alias in table without outer bars rejected' 1 'unescaped' @'
Page | Description
--- | ---
[[exercises/Algorithmic Index|Collection]] | Collection index.
'@

    Run-Case 'escaped alias in table without outer bars passes' 0 '^PASS:' @'
Page | Description
:--- | ---:
[[exercises/Algorithmic Index\|Collection]] | Collection index.
'@

    Run-Case 'table examples inside fenced code are ignored' 0 '^PASS:' @'
```markdown
| Page | Description |
| --- | --- |
| [[This target does not exist|Raw example]] | Code only. |
```

> [!note]- Another code example
> ```markdown
> Page | Description
> --- | ---
> [[Another missing target|Raw example]] | Code only.
> ```
'@

    Run-Case 'inline code examples inside a real table are ignored' 0 '^PASS:' @'
| Syntax | Description |
| --- | --- |
| `[[This target does not exist|Raw example]]` | Literal example only. |
| `![[Missing image.png|120]]` | Literal embed example only. |
'@

    Run-Case 'broken escaped target still fails file resolution' 1 'missing or ambiguous wikilink' @'
| Page | Description |
| --- | --- |
| [[exercises/algorithmic/Does not exist\|Missing]] | Broken target. |
'@ $defaultMasterBody 'unescaped'

    Run-Case 'raw image resize pipe in a table rejected' 1 'unescaped' @'
| Figure | Description |
| --- | --- |
| ![[exercises/assets/fixture.png|120]] | Fixture attachment. |
'@

    Run-Case 'escaped image resize pipe in a table passes' 0 '^PASS:' @'
| Figure | Description |
| --- | --- |
| ![[exercises/assets/fixture.png\|120]] | Fixture attachment. |
'@

    Run-Case 'later raw image pipe after an escaped pipe rejected' 1 'unescaped' @'
| Figure | Description |
| --- | --- |
| ![[exercises/assets/fixture.png\|Fixture|120]] | Fixture attachment. |
'@

    Run-Case 'multiple escaped image pipes in a table pass' 0 '^PASS:' @'
| Figure | Description |
| --- | --- |
| ![[exercises/assets/fixture.png\|Fixture\|120]] | Fixture attachment. |
'@

    # Subject notes outside the managed exercise tree receive only the table scan.
    # They intentionally have no exercise metadata and no corresponding folder index.
    Write-FixtureFile 'Study notes/Ordinary subject/Existing note.md' @'
# Existing subject note

| Reference | Meaning |
| --- | --- |
| [[Prerequisite DAG|Study map]] | An ordinary subject-note reference. |
'@
    Run-Case 'raw table alias in an ordinary subject note rejected' 1 'unescaped' 'Fixture concept.'

    Write-FixtureFile 'Study notes/Ordinary subject/Existing note.md' @'
# Existing subject note

| Reference | Meaning |
| --- | --- |
| [[Prerequisite DAG\|Study map]] | An ordinary subject-note reference. |
'@
    Run-Case 'escaped subject-note alias passes without exercise schema or index rules' 0 '^PASS:' 'Fixture concept.'

    Write-Output "PASS: all $passed table-wikilink regression cases."
    if ($KeepFixture) { Write-Output "Fixture retained: $fixtureRoot" }
    else {
        $resolvedFixture = (Resolve-Path -LiteralPath $fixtureRoot).Path
        $safePrefix = $tempBase + [System.IO.Path]::DirectorySeparatorChar
        if (!$resolvedFixture.StartsWith($safePrefix, [System.StringComparison]::OrdinalIgnoreCase) -or [System.IO.Path]::GetFileName($resolvedFixture) -notmatch '^codex-validate-links-[0-9a-f]{32}$') {
            throw "Refusing to remove fixture outside the verified temporary location: $resolvedFixture"
        }
        Remove-Item -LiteralPath $resolvedFixture -Recurse -Force
    }
    exit 0
}
catch {
    Write-Output "FAIL: $($_.Exception.Message)"
    if ($fixtureRoot) { Write-Output "Failure fixture retained: $fixtureRoot" }
    exit 1
}
