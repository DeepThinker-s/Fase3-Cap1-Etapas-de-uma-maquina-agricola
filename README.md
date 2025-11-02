# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Fase 3: Cap 1 - Etapas de uma Máquina Agrícola

## DeepThinker's

## 👨‍🎓 Integrantes Grupo 11: 
- <a href="https://www.linkedin.com/in/andrégaidzakian">André Pessoa Gaidzakian - RM567877</a>
- <a href="https://www.linkedin.com/in/erick-prados-97171a237">Erick Prados Pereira - RM566833</a>
- <a href="https://www.linkedin.com/in/guilherme-ferreira-santos-94619b23a">Guilherme Ferreira Santos - RM568523</a> 
- <a href="https://www.linkedin.com/in/viviane-de-castro-98764656">Viviane de Castro - RM567367</a> 
## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>


## 📜 Descrição

## [Link do GitHub](https://github.com/DeepThinker-s/Fase3-Cap1-Etapas-de-uma-maquina-agricola)

### 1. Introdução
O agronegócio brasileiro é um dos setores mais dinâmicos e estratégicos da economia nacional, representando cerca de 27% do PIB (IBGE, 2024). A modernização do campo, impulsionada por tecnologias digitais, sensores e automação, permite ganhos de produtividade, sustentabilidade e eficiência. Neste contexto, a FarmTech Solutions, startup fictícia, desenvolveu um sistema de monitoramento e automação agrícola, integrando sensores ambientais, lógica de decisão e banco de dados Oracle para armazenamento e análise dos dados coletados.
Este relatório detalha o processo de importação dos dados coletados na Fase 2 para o Oracle SQL Developer, explorando as etapas, boas práticas e evidências do funcionamento do sistema.

### 2. Objetivo
Demonstrar, de forma prática e documentada, a importação, consulta e manipulação dos dados agrícolas simulados (Fase 2) em um banco de dados Oracle, utilizando o Oracle SQL Developer, conforme orientações do PBL do curso de Inteligência Artificial.

### 3. Materiais Utilizados
- **Base de dados:** dados_agro.xlsx (simulada a partir de dados plausíveis do agro brasileiro, conforme CONAB, IBGE, Embrapa, etc.)
- **Ferramenta de banco de dados:** Oracle SQL Developer
- **Documentação e códigos:** Repositório GitHub do grupo
- **Sistema de sensores:** ESP32, sensores DHT22, botões NPK, LDR (pH), módulo relé (detalhado na Fase 2)
- **Códigos de integração:** C/C++ (ESP32) e Python (API clima)

### 4. [Vídeo do projeto](https://youtu.be/w_iDfc6KNrY)


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.8 ou superior** - [Download Python](https://www.python.org/downloads/)
- **Oracle Database** - Oracle XE 21c ou superior ([Download Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html))
- **Oracle SQL Developer** (opcional, para gerenciar o banco) - [Download SQL Developer](https://www.oracle.com/database/sqldeveloper/technologies/download/)
- **Git** - Para clonar o repositório

### Bibliotecas Python utilizadas

- `oracledb` - Conexão com Oracle Database
- `python-dotenv` - Gerenciamento de variáveis de ambiente
- `tabulate` - Formatação de tabelas no terminal

---

### Passo 1: Clonar o Repositório

```powershell
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/Fase6Modificada
```

### Passo 2: Configurar Ambiente Virtual

Crie e ative um ambiente virtual Python para isolar as dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Nota:** Se houver erro de política de execução, execute: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Passo 3: Instalar Dependências

```powershell
pip install -r requirements.txt
```

### Passo 4: Configurar o Banco de Dados Oracle

1. **Copie o arquivo de exemplo de configuração:**
   ```powershell
   copy config\.env.example config\.env
   ```

2. **Edite o arquivo `config/.env` com suas credenciais Oracle:**
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_DSN=localhost:1521/XE
   ```
   
   > **Importante:** O arquivo `.env` contém credenciais sensíveis e **NÃO** deve ser commitado no Git (já está no `.gitignore`).

3. **Teste a conexão com o banco:**
   ```powershell
   python -m scripts.teste_conexao
   ```

### Passo 5: Executar o Sistema

**Executar o programa principal (menu interativo):**
```powershell
python -m src.main
```

O sistema apresentará um menu com as seguintes opções:
- **1. Registrar colheita** - Cadastra nova colheita no banco
- **2. Gerar relatório** - Gera relatórios em JSON, TXT e CSV
- **3. Sair** - Encerra o sistema

---

### Funcionalidades Principais

#### 📊 Registrar Colheita
Permite registrar dados de colheita com informações de:
- Tipo de colheita (manual ou mecânica)
- Produtividade estimada (t/ha)
- Produtividade real (t/ha)
- Valor por tonelada (R$)

**Observação importante:** O sistema **apenas registra perdas**. Se a produtividade real for maior que a estimada (ganho), o sistema informará o usuário e **não salvará** o registro, pois o foco é monitorar perdas agrícolas. Verifique as mensagens de confirmação:
- [OK] = Dados salvos com sucesso
- [ERRO] = Problema na conexão/banco de dados

#### 📈 Gerar Relatórios
Gera relatórios automáticos em três formatos:
- **JSON** (`document/relatorio.json`) - Dados estruturados
- **TXT** (`document/relatorio.txt`) - Relatório completo com sumário executivo
- **CSV** (`document/relatorio.csv`) - Planilha para análise

---

### Estrutura de Execução por Fase

#### **Fase 1** - Coleta de Dados com Sensores
- Sistema físico com ESP32 e sensores (DHT22, LDR, botões NPK)
- Código Arduino/C++ para leitura de sensores

#### **Fase 2** - Integração com Oracle Database
- Conexão com Oracle Database via `oracledb`
- CRUD completo de colheitas
- Geração de relatórios analíticos
- Sistema de menu interativo

---

## 📸 Evidências de Execução

### Evidência 1 - Exportação do relatório no programa
![Evidência 1](assets/Evidência%20de%20execução%201.png)

### Evidência 2 - Local dos arquivos
![Evidência 2](assets/Evidência%20de%20execução%202.png)

### Evidência 3 - Conexão com o banco de dados da FIAP via Oracle
![Evidência 3](assets/Evidência%20de%20execução%203.png)

### Evidência 4 - Conectado e importando dados para a DB
![Evidência 4](assets/Evidência%20de%20execução%204.png)

### Evidência 5 - Buscando arquivos de registro
![Evidência 5](assets/Evidência%20de%20execução%205.png)

### Evidência 6 - Verificando dados
![Evidência 6](assets/Evidência%20de%20execução%206.png)

### Evidência 7 - Criando tabela
![Evidência 7](assets/Evidência%20de%20execução%207.png)

### Evidência 8 - Confirmando colunas
![Evidência 8](assets/Evidência%20de%20execução%208.png)

### Evidência 9 - Finalizando exportação
![Evidência 9](assets/Evidência%20de%20execução%209.png)

### Evidência 10 - Dados importados
![Evidência 10](assets/Evidência%20de%20execução%2010.png)

---

### Comandos Úteis

**Verificar versão do Python:**
```powershell
python --version
```

**Listar pacotes instalados:**
```powershell
pip list
```

**Atualizar pip:**
```powershell
python -m pip install --upgrade pip
```

**Desativar ambiente virtual:**
```powershell
deactivate
```

---

### Solução de Problemas

**Erro ao ativar ambiente virtual:**
- Execute: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Erro de conexão Oracle:**
- Verifique se o Oracle Database está rodando
- Confirme as credenciais no arquivo `.env`
- Teste com: `python -m scripts.teste_conexao`

**Módulo não encontrado:**
- Certifique-se de que o ambiente virtual está ativado
- Reinstale as dependências: `pip install -r requirements.txt`



## 🗃 Histórico de lançamentos

* 2.0.0 - 02/11/2025 (Versão Atual)
    * **Refatoração completa baseada no feedback do professor**
    * Migração de `cx_Oracle` para `oracledb` (biblioteca moderna)
    * Implementação de variáveis de ambiente (.env) para credenciais Oracle
    * Tratamento robusto de exceções (try/except) em todas operações de I/O e banco
    * Sistema de commit/rollback para garantir integridade transacional
    * Funções modulares com docstrings, parâmetros e retornos bem definidos
    * Operações CRUD completas em memória com listas/dicionários
    * Formatação tabular de consultas (biblioteca `tabulate`)
    * Geração de relatórios em três formatos: JSON, TXT e CSV
    * Estrutura modular organizada (src/, config/, document/, scripts/)
    * Scripts de teste de conexão e utilitários
    * Documentação completa de execução no README
    * Evidências de execução com exemplos de relatórios

* 1.0.0 - 12/10/2025 (Primeira Entrega)
    * Versão inicial do sistema de monitoramento agrícola
    * Integração básica com Oracle Database
    * Problema bem definido e solução coerente para o agronegócio
    * Sistema de colheita com registro de perdas
    * Geração de relatórios em TXT e JSON
    * Organização modular do código
    * Persistência básica de dados
    * Menu interativo para operações do sistema
    * **Recebeu ponto extra por equipe com 4 integrantes**

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


