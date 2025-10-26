Como rodar o projeto (mínimo)

1) Crie um ambiente virtual e instale dependências:

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt

2) Copie o arquivo de exemplo e edite com suas credenciais Oracle:

   copy .env.example .env
   # editar .env e inserir DB_USER, DB_PASSWORD, DB_DSN

3) Execute o programa:

   python main.py

Observações:
- Não comite seu `.env` com credenciais reais.
- Se preferir usar cx_Oracle, remova `oracledb` e instale as dependências do Instant Client; porém `oracledb` em modo "thin" dispensa o Instant Client.
- `requirements.txt` contém as dependências necessárias: oracledb, python-dotenv e tabulate.
