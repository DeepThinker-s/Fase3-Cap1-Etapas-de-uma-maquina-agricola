# Script de inicialização automática do projeto
# Executa todas as etapas necessárias e inicia o sistema

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Sistema de Monitoramento de Colheita  " -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# 1. Verificar se o ambiente virtual existe
if (-Not (Test-Path ".\.venv")) {
    Write-Host "[1/4] Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "      Ambiente virtual criado!" -ForegroundColor Green
} else {
    Write-Host "[1/4] Ambiente virtual encontrado!" -ForegroundColor Green
}

# 2. Ativar ambiente virtual
Write-Host "[2/4] Ativando ambiente virtual..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# 3. Instalar/atualizar dependências
Write-Host "[3/4] Instalando dependências..." -ForegroundColor Yellow
python -m pip install -q --upgrade pip
python -m pip install -q -r requirements.txt
Write-Host "      Dependências instaladas!" -ForegroundColor Green

# 4. Verificar arquivo .env
Write-Host "[4/4] Verificando configuração..." -ForegroundColor Yellow
if (-Not (Test-Path ".\config\.env")) {
    Write-Host "`n" -ForegroundColor Red
    Write-Host "ATENÇÃO: Arquivo .env não encontrado!" -ForegroundColor Red
    Write-Host "1. Copie config\.env.example para config\.env" -ForegroundColor Yellow
    Write-Host "2. Edite config\.env com suas credenciais Oracle" -ForegroundColor Yellow
    Write-Host "`nPressione qualquer tecla para sair..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit
} else {
    Write-Host "      Configuração encontrada!" -ForegroundColor Green
}

# 5. Iniciar o sistema
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Iniciando o sistema...               " -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

python -m src.main
