# Como Executar o Projeto

## Pré-requisitos
- Python 3.8 ou superior
- Oracle Database (pode ser Oracle XE)

## Instalação

1. **Clone o repositório e navegue até a pasta:**
   ```powershell
   cd Fase6Modificada
   ```

2. **Crie e ative um ambiente virtual:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   python -m pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**
   - Edite o arquivo `config/.env` com suas credenciais Oracle
   - Use o arquivo `config/.env.example` como referência

## Executando o Projeto

### Executar o sistema principal:
```powershell
python -m src.main
```

### Executar testes de conexão:
```powershell
python -m scripts.teste_conexao
```

## Estrutura do Projeto

- **src/** - Código fonte principal
  - `main.py` - Programa principal com menu
  - `banco.py` - Conexão e operações com Oracle
  - `colheita.py` - Registro de colheitas

- **document/** - Documentação e relatórios
  - `relatorios.py` - Geração de relatórios
  - Relatórios gerados: `relatorio.json`, `relatorio.txt`, `relatorio.csv`

- **scripts/** - Scripts auxiliares
  - `utils.py` - Funções utilitárias
  - `teste_conexao.py` - Teste de conexão com banco

- **config/** - Configurações
  - `.env` - Variáveis de ambiente (não commitar!)
  - `.env.example` - Exemplo de configuração

## Notas Importantes

- O arquivo `.env` com credenciais reais **NÃO** deve ser commitado no Git
- Os relatórios são salvos automaticamente na pasta `document/`
- Execute sempre a partir da raiz do projeto usando `python -m`
