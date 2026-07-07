$limitMB = 100
$limitBytes = $limitMB * 1024 * 1024

$files = Get-ChildItem -Recurse -File -Force |
  Where-Object {
    $_.FullName -notmatch "\\.git\\" -and
    $_.FullName -notmatch "\\node_modules\\" -and
    $_.FullName -notmatch "\\.venv\\" -and
    $_.Length -ge $limitBytes
  } |
  Sort-Object Length -Descending

if ($files.Count -eq 0) {
  Write-Host "OK: no files >= $limitMB MB"
  exit 0
}

Write-Host "ERROR: files >= $limitMB MB found:"
$files | ForEach-Object {
  "{0:N2} MB  {1}" -f ($_.Length / 1MB), $_.FullName
}
exit 1
