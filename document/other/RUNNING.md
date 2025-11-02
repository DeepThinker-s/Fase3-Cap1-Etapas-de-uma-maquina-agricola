Como rodar o projeto (mínimo)

1) Crie um ambiente virtual e instale dependências:

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt

2) Configure suas credenciais Oracle no arquivo .env:

   # O arquivo .env está em config/.env
   # Edite config/.env e insira DB_USER, DB_PASSWORD, DB_DSN

3) Execute o programa a partir da raiz do projeto:

   python -m src.main

Observações:
- Não comite seu `config/.env` com credenciais reais.
- Se preferir usar cx_Oracle, remova `oracledb` e instale as dependências do Instant Client; porém `oracledb` em modo "thin" dispensa o Instant Client.
- `requirements.txt` contém as dependências necessárias: oracledb, python-dotenv e tabulate.
- Os relatórios são gerados na pasta `document/` (relatorio.json, relatorio.txt, relatorio.csv)
- Para executar scripts de teste: `python -m scripts.teste_conexao`

## Estrutura do Projeto

- **src/** - Código fonte
  - `main.py` - Menu principal
  - `banco.py` - Conexão Oracle
  - `colheita.py` - Registro de colheitas (apenas perdas)
  - `relatorios.py` - Geração de relatórios

- **document/** - Relatórios gerados
  - `relatorio.json` - Dados estruturados
  - `relatorio.txt` - Relatório completo
  - `relatorio.csv` - Planilha Excel

- **scripts/** - Utilitários
  - `teste_conexao.py` - Teste de conexão
  - `utils.py` - Funções auxiliares

- **config/** - Configurações
  - `.env` - Credenciais (NÃO commitar!)

## Troubleshooting - Colheitas Não Estão Sendo Salvas

Se você registrar uma colheita e ela não aparecer nos relatórios, verifique:

1. **Você está registrando um GANHO em vez de PERDA?**
   - O sistema **só salva registros com perda** (prod_real < prod_estimada)
   - Se prod_real > prod_estimada, o sistema mostra mensagem de ganho e NÃO salva

2. **Verifique a mensagem de confirmação:**
   - [OK] "Colheita registrada com sucesso!" = SALVO
   - [ERRO] "Não foi possível salvar" = NÃO SALVO (problema no banco)

3. **Teste a conexão com o banco:**
   ```powershell
   python -m scripts.teste_conexao
   ```

4. **Verifique suas credenciais no `config/.env`:**
   - DB_USER está correto?
   - DB_PASSWORD está correto?
   - DB_DSN está correto? (ex: localhost:1521/XE)

5. **O Oracle Database está rodando?**
   - Verifique se o serviço Oracle está ativo no Windows

