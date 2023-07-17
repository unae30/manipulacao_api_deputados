import json

def verificar_estrutura_json(dados):
    try:
        dados_json = json.loads(dados)

        # Verifique a estrutura do JSON aqui
        if "deputado_" in dados_json and "nome" in dados_json["deputado_"]:
            print("Estrutura do JSON válida.")
        else:
            print("Estrutura do JSON inválida.") 
            # Esta caindo nesta condição. Algum dado que era para ser filtrado,  está vazio

    except json.JSONDecodeError as e:
        print("Erro na conversão para JSON:", e)
