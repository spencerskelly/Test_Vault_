param(
  [Parameter(Mandatory=$true)][string]$Name,
  [Parameter(Mandatory=$true)][string]$AuthorCode
)

if ($AuthorCode -notmatch '^[a-z-]{13}$') {
  throw "AuthorCode must be exactly 13 lowercase ASCII letters/dashes."
}

if (Test-Path ".vault.yaml") {
  $existing = Get-Content ".vault.yaml" -Raw
  if ($existing -notmatch "UNINITIALIZED") {
    throw ".vault.yaml already appears initialized. Refusing to overwrite."
  }
}

$now = [DateTime]::UtcNow
$ts = $now.ToString("yyyyMMddHHmmss") + $now.Millisecond.ToString("000")
$uid = $ts + $AuthorCode

@"
vault_uid: $uid
name: $Name
default_branch: main
"@ | Set-Content ".vault.yaml" -Encoding utf8

Write-Host "Initialized vault UID: $uid"
