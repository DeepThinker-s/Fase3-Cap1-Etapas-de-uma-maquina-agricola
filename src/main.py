from src.colheita import registrar_colheita
from document.relatorios import gerar_relatorio
import src.banco as banco

def menu():
    while True:
        print("\n=== Monitoramento de Perdas na Colheita ===")
        print("1. Registrar colheita")
        print("2. Gerar relatório")
        print("3. Sair")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "1":
            registrar_colheita()
        elif opcao == "2":
            gerar_relatorio()
        elif opcao == "3":
            print("\n✓ Sistema encerrado")
            break
        else:
            print("⚠ Opção inválida!")

if __name__ == "__main__":
    banco.criar_tabela()
    menu()
