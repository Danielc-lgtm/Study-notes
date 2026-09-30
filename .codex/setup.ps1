[CmdletBinding()]
param(
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$ConfigOnly
)

# Read-only verification: no installation, network access, Git operations, or global changes.
& (Join-Path $PSScriptRoot 'tools/validate_setup.ps1') -RepoRoot $RepoRoot -ConfigOnly:$ConfigOnly
exit $LASTEXITCODE
