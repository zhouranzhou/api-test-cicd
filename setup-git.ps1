# Refresh environment variables and test Git
Write-Host "Refreshing environment variables..." -ForegroundColor Green

# Get updated PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "Verifying Git installation..." -ForegroundColor Green
git --version

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nSuccess! Git is now configured." -ForegroundColor Green
    Write-Host "`nYou can now run these commands to fix the push issue:" -ForegroundColor Cyan
    Write-Host "1. git pull origin main" -ForegroundColor Yellow
    Write-Host "2. git push origin main" -ForegroundColor Yellow
} else {
    Write-Host "`nGit not found. Please restart PowerShell and try again." -ForegroundColor Red
}
