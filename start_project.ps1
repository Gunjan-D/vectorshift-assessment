# VectorShift Project Startup Script (No Admin Required)
# Run this script to start everything

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "VectorShift Project Startup" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Add portable tools to PATH
$env:Path += ";C:\Users\gdeshpande\portable_tools\node-v20.18.1-win-x64;C:\Users\gdeshpande\portable_tools\redis"

# Check if Redis is running
Write-Host "Checking Redis..." -ForegroundColor Yellow
$redisRunning = Get-Process redis-server -ErrorAction SilentlyContinue
if (-not $redisRunning) {
    Write-Host "Starting Redis server..." -ForegroundColor Green
    Start-Process -FilePath "C:\Users\gdeshpande\portable_tools\redis\redis-server.exe"
    Start-Sleep -Seconds 2
} else {
    Write-Host "Redis is already running!" -ForegroundColor Green
}

# Test Redis
$redisPing = & C:\Users\gdeshpande\portable_tools\redis\redis-cli.exe ping
if ($redisPing -eq "PONG") {
    Write-Host "✓ Redis is working!" -ForegroundColor Green
} else {
    Write-Host "✗ Redis is NOT working!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Node.js: $(node --version)" -ForegroundColor Green
Write-Host "NPM: $(npm --version)" -ForegroundColor Green
Write-Host "Python: $(python --version)" -ForegroundColor Green
Write-Host "Redis: Running" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Ready to start!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Terminal 1: cd backend; uvicorn main:app --reload" -ForegroundColor White
Write-Host "2. Terminal 2: cd frontend; npm install; npm start" -ForegroundColor White
Write-Host ""
