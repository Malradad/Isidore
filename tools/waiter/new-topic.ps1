# Creates a long random relay topic in tools\waiter\.topic and prints the TradingView webhook URL.
$bytes = New-Object byte[] 18
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
$topic = "izzy-" + (($bytes | ForEach-Object { $_.ToString("x2") }) -join "")
Set-Content -Path (Join-Path $PSScriptRoot ".topic") -Value $topic
Write-Output "Webhook URL for TradingView: https://ntfy.sh/$topic"
