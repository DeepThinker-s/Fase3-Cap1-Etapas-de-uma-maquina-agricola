import json
import csv
import os
from src.banco import listar_dados
from datetime import datetime
from scripts.utils import print_table

def gerar_relatorio():
    """
    Gera relatórios formatados (TXT e JSON) a partir dos dados de colheita do banco.
    O relatório TXT é humanamente legível e inclui um sumário.
    O relatório JSON é estruturado com chaves descritivas.
    Também exibe uma tabela formatada no console para visualização imediata.
    """
    dados_brutos = listar_dados()
    if not dados_brutos:
        print("Nenhum dado de colheita encontrado para gerar relatórios.")
        return

    # --- Preparação dos dados e cálculos para o sumário ---
    registros_formatados_json = []
    registros_formatados_tabela = []  # Para exibição em tabulate
    prejuizo_total = 0
    soma_percentual_perda = 0
    contagem_manual = 0
    contagem_mecanica = 0
    
    # Mapeia os índices da tupla do banco para nomes de colunas claros
    colunas = [
        "ID",
        "PROD_ESTIMADA",
        "TIPO_COLHEITA",
        "PROD_REAL",
        "VALOR_POR_TONELADA",
        "PERDA_PERCENTUAL",
        "PREJUIZO",
        "DATA_HORA"
    ]

    for linha in dados_brutos:
        # Formata os valores para exibição
        tipo = str(linha[1]).capitalize()
        prod_est = f"{linha[2]:.2f}"
        prod_real = f"{linha[3]:.2f}"
        valor_ton = f"{linha[4]:.2f}"
        perda_perc = f"{linha[5]:.2f}"
        prejuizo = f"{linha[6]:.2f}"

        # Cria um dicionário para o JSON com nomes descritivos
        registro_dict = {
            "ID": linha[0],
            "Tipo de Colheita": tipo,
            "Prod. Estimada (t/ha)": prod_est,
            "Prod. Real (t/ha)": prod_real,
            "Valor por Tonelada (R$)": valor_ton,
            "Perda Percentual (%)": perda_perc,
            "Prejuízo (R$)": prejuizo,
            "Data e Hora": linha[7]
        }
        registros_formatados_json.append(registro_dict)

        # Cria uma lista formatada para a tabela
        registro_tabela = [
            linha[0], prod_est, tipo, prod_real,
            valor_ton, perda_perc, prejuizo, linha[7]
        ]
        registros_formatados_tabela.append(registro_tabela)

        # Cálculos para o sumário do relatório TXT
        prejuizo_total += linha[6]
        soma_percentual_perda += linha[5]
        if linha[1].lower() == 'manual':
            contagem_manual += 1
        elif linha[1].lower() == 'mecanica':
            contagem_mecanica += 1
    
    perda_media = soma_percentual_perda / len(dados_brutos) if dados_brutos else 0

    # Define o diretório para salvar os relatórios (pasta document)
    diretorio_relatorios = os.path.join(os.path.dirname(__file__), '..', 'document')

    # --- Geração do Relatório em JSON ---
    caminho_json = os.path.join(diretorio_relatorios, "relatorio.json")
    with open(caminho_json, "w", encoding="utf-8") as f:
        # O JSON agora é uma lista de objetos com chaves descritivas
        json.dump(registros_formatados_json, f, ensure_ascii=False, indent=4)

    # --- Geração do Relatório em TXT ---
    # Exibe a tabela formatada no console
    print("\n=== REGISTROS ===")
    print_table(colunas, registros_formatados_tabela)
    print(f"\nTotal: {len(dados_brutos)} | Perda média: {perda_media:.2f}% | Prejuízo: R$ {prejuizo_total:,.2f}\n")

    # Gera o arquivo CSV com todos os dados
    caminho_csv = os.path.join(diretorio_relatorios, "relatorio.csv")
    with open(caminho_csv, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(colunas)  # Cabeçalho
        writer.writerows(registros_formatados_tabela)  # Dados
    
    caminho_txt = os.path.join(diretorio_relatorios, "relatorio.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write("=========================================================\n")
        f.write("      RELATÓRIO DE MONITORAMENTO DE PERDAS NA COLHEITA\n")
        f.write("=========================================================\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

        f.write("------------------ REGISTROS INDIVIDUAIS ------------------\n\n")
        for reg in registros_formatados_json:
            f.write(f"{reg['Data e Hora']}\n")
            f.write(f"  - ID do Registro.........: {reg['ID']}\n")
            f.write(f"  - Tipo de Colheita.......: {reg['Tipo de Colheita']}\n")
            f.write(f"  - Prod. Estimada.........: {reg['Prod. Estimada (t/ha)']} t/ha\n")
            f.write(f"  - Prod. Real.............: {reg['Prod. Real (t/ha)']} t/ha\n")
            f.write(f"  - Valor por Tonelada.....: {reg['Valor por Tonelada (R$)']}\n")
            f.write(f"  - Percentual de Perda....: {reg['Perda Percentual (%)']}\n")
            f.write(f"  - PREJUÍZO FINANCEIRO....: {reg['Prejuízo (R$)']}\n")
            f.write("---------------------------------------------------------\n\n")

        f.write("===================== SUMÁRIO EXECUTIVO =====================\n\n")
        f.write(f"Total de Registros de Perda...: {len(dados_brutos)}\n")
        f.write(f"  - Colheitas Manuais........: {contagem_manual}\n")
        f.write(f"  - Colheitas Mecânicas......: {contagem_mecanica}\n\n")
        f.write(f"Média de Perda Percentual.....: {perda_media:.2f}%\n")
        f.write(f"PREJUÍZO TOTAL ACUMULADO......: R$ {prejuizo_total:,.2f}\n\n")
        f.write("=========================================================\n")

    print("\n[OK] Relatórios gerados com sucesso!")
    print(f"  Localização: document/")
    print(f"  - relatorio.json (dados estruturados)")
    print(f"  - relatorio.txt  (relatório completo)")
    print(f"  - relatorio.csv  (planilha)")