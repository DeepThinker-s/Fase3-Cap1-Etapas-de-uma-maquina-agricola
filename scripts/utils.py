from tabulate import tabulate


def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido! Digite um número.")


def print_table(headers, rows):
    """Imprime uma lista de tuplas/listas como tabela legível.

    Args:
        headers (list[str]): Lista de nomes de colunas.
        rows (list[tuple] | list[list]): Linhas de dados.
    """
    if not rows:
        print("Nenhum registro para exibir.")
        return

    print(tabulate(rows, headers=headers, tablefmt="grid"))
