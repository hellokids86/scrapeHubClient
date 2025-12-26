# Regenerate ScraperHub Python Client
# This script downloads the latest OpenAPI spec and regenerates the client

Write-Host "ScraperHub Client Regenerator" -ForegroundColor Cyan
Write-Host ("=" * 50) -ForegroundColor Cyan
Write-Host ""


# Step 1: Generate the Python client
Write-Host "Step 1: Generating Python client..." -ForegroundColor Yellow
Write-Host "This may take a moment..." -ForegroundColor Gray
Write-Host ""

npx @openapitools/openapi-generator-cli generate -i openapi.json -g python -o . --package-name scrapehub_client

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Client generated successfully!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Failed to generate client (exit code: $LASTEXITCODE)" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host ("=" * 50) -ForegroundColor Cyan
Write-Host "Client regeneration complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Review any changes to the generated files"
Write-Host "2. Reinstall the package: pip install -e ."
Write-Host "3. Test your code with the updated client"
Write-Host ""
