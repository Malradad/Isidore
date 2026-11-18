# Izzy alert waiter — waits (using no Claude usage) until a TradingView alert arrives, prints it, exits.
# Run it as a BACKGROUND command from Claude Code; when it exits, Claude wakes up with the alert.
#
#   powershell -NoProfile -ExecutionPolicy Bypass -File tools\waiter\wait-alert.ps1
#
# The relay topic is read from tools\waiter\.topic (one line, never committed).
# TradingView alert → Webhook URL: https://ntfy.sh/<topic>
param([int]$MaxMinutes = 0)   # 0 = wait forever

$ErrorActionPreference = "Stop"
$dir   = $PSScriptRoot
$topic = (Get-Content (Join-Path $dir ".topic") -ErrorAction Stop | Select-Object -First 1).Trim()
$state = Join-Path $dir ".last-id"
$since = if (Test-Path $state) { (Get-Content $state | Select-Object -First 1).Trim() } else { "1m" }
$start = Get-Date
Add-Type -AssemblyName System.Net.Http

while ($true) {
    if ($MaxMinutes -gt 0 -and ((Get-Date) - $start).TotalMinutes -ge $MaxMinutes) {
        Write-Output '{"izzy":"TIMEOUT"}'; exit 3
    }
    try {
        $client = [System.Net.Http.HttpClient]::new()
        $client.Timeout = [System.Threading.Timeout]::InfiniteTimeSpan
        $url    = "https://ntfy.sh/$topic/json?since=$since"
        $stream = $client.GetStreamAsync($url).GetAwaiter().GetResult()
        $reader = [System.IO.StreamReader]::new($stream)
        while ($null -ne ($line = $reader.ReadLine())) {
            if (-not $line) { continue }
            $o = $line | ConvertFrom-Json
            if ($o.event -eq "message") {
                Set-Content -Path $state -Value $o.id
                Write-Output $o.message
                exit 0
            }
        }
    } catch {
        Start-Sleep -Seconds 3   # network blip: reconnect
    } finally {
        if ($client) { $client.Dispose() }
    }
}
