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
