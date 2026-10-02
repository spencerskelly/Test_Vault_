param(
  [Parameter(Mandatory=$true)][string]$Name,
  [Parameter(Mandatory=$true)][string]$AuthorCode
)

if ($AuthorCode -notmatch '^[a-z-]{13}$') {
  throw "AuthorCode must be exactly 13 lowercase ASCII letters/dashes."
}

if (-not (Test-Path ".vault.yaml")) {
  throw ".vault.yaml is missing. Start from a generated MDSE base vault."
}

$existing = Get-Content ".vault.yaml" -Raw
if ($existing -notmatch "UNINITIALIZED") {
  throw ".vault.yaml already appears initialized. Refusing to overwrite."
}

$m = [regex]::Match($existing, '(?m)^mdse_release:\s*["'']?([^"''#\r\n]+)')
if (-not $m.Success) {
  throw ".vault.yaml has no mdse_release. Refusing to initialize an unpaired base."
}
$release = $m.Groups[1].Value.Trim()

$now = [DateTime]::UtcNow
$ts = $now.ToString("yyyyMMddHHmmss") + $now.Millisecond.ToString("000")
$uid = $ts + $AuthorCode

@"
vault_uid: $uid
name: $Name
default_branch: main
mdse_release: "$release"
"@ | Set-Content ".vault.yaml" -Encoding utf8

Write-Host "Initialized vault UID: $uid"
Write-Host "Preserved MDSE release: $release"
