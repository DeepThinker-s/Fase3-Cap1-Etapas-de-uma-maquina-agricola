"""Script para testar conexões e funcionalidades básicas do sistema."""
import os
from banco import conectar_oracle, criar_tabela, listar_dados
from utils import print_table
from dotenv import load_dotenv

def teste_ambiente():
    """Testa variáveis de ambiente."""
    load_dotenv()
    print("\n=== Teste de Variáveis de Ambiente ===")
    tem_user = bool(os.environ.get("DB_USER"))
    tem_pwd = bool(os.environ.get("DB_PASSWORD"))
    tem_dsn = bool(os.environ.get("DB_DSN"))
    
    print(f"DB_USER definido: {'✓' if tem_user else '✗'}")
    print(f"DB_PASSWORD definido: {'✓' if tem_pwd else '✗'}")
    print(f"DB_DSN definido: {'✓' if tem_dsn else '✗'}")
    
    return all([tem_user, tem_pwd, tem_dsn])

def teste_conexao():
    """Testa conexão com o banco."""
    print("\n=== Teste de Conexão Oracle ===")
    conn = conectar_oracle()
    if conn:
        print("Conexão bem sucedida! ✓")
        conn.close()
        return True
    else:
        print("Falha na conexão ✗")
        return False

def teste_tabela():
    """Testa criação da tabela."""
    print("\n=== Teste de Criação da Tabela ===")
    try:
        criar_tabela()
        print("Tabela verificada/criada com sucesso! ✓")
        return True
    except Exception as e:
        print(f"Erro ao criar tabela: {e} ✗")
        return False

def teste_consulta():
    """Testa consulta de dados."""
    print("\n=== Teste de Consulta ===")
    try:
        dados = listar_dados()
        if dados is None:
            print("Consulta executada, sem dados ainda ✓")
        else:
            print(f"Consulta retornou {len(dados)} registros ✓")
            if dados:
                headers = ["ID", "Tipo", "Prod.Est", "Prod.Real", "Valor/t", "Perda%", "Prejuízo", "Data"]
                print("\nPrimeiros registros:")
                # Mostra até 3 registros como exemplo
                print_table(headers, dados[:3])
        return True
    except Exception as e:
        print(f"Erro na consulta: {e} ✗")
        return False

if __name__ == "__main__":
    print("Iniciando testes do sistema...")
    
    # Testa na ordem: ambiente → conexão → tabela → consulta
    if teste_ambiente():
        if teste_conexao():
            if teste_tabela():
                teste_consulta()
    
    print("\nTestes concluídos!")