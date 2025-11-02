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
  - `main.py` - Programa principal com menu interativo
  - `banco.py` - Conexão e operações com Oracle Database
  - `colheita.py` - Registro de colheitas (apenas perdas)
  - `relatorios.py` - Geração de relatórios em JSON, TXT e CSV

- **scripts/** - Scripts auxiliares
  - `utils.py` - Funções utilitárias (validação, formatação de tabelas)
  - `teste_conexao.py` - Teste de conexão com banco

- **config/** - Configurações
  - `.env` - Variáveis de ambiente (não commitar!)
  - `.env.example` - Exemplo de configuração

- **document/** - Documentação complementar

## Funcionalidades

### 1. Registrar Colheita
O sistema permite registrar dados de perdas na colheita:
- Tipo (manual ou mecânica)
- Produtividade estimada e real (t/ha)
- Valor por tonelada

**Importante:** Apenas registros com **perda** são salvos. Se a produtividade real superar a estimada, o sistema informa que houve ganho e não salva o registro.

### 2. Gerar Relatórios
Gera automaticamente relatórios em três formatos na pasta `document/`:
- `relatorio.json` - Dados estruturados
- `relatorio.txt` - Relatório completo com sumário
- `relatorio.csv` - Planilha para Excel

## Notas Importantes

- O arquivo `.env` com credenciais reais **NÃO** deve ser commitado no Git
- Os relatórios são salvos automaticamente na pasta `document/`
- Execute sempre a partir da raiz do projeto usando `python -m`
- O sistema **só registra perdas**: se a produtividade real for maior que a estimada, o registro não é salvo
- Verifique mensagens de sucesso/erro ao registrar colheitas:
  - [OK] = dados salvos com sucesso
  - [ERRO] = problema na conexão ou banco de dados
