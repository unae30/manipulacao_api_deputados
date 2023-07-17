import json
import requests
from api import API
from verificador_json import verificar_estrutura_json
from WeightedGraph import Grafo_Deputados 

def main():

    graph = Grafo_Deputados()
    graph.criar_grafo_ponderado()
    graph.escrever_resultados_em_arquivo("resultados.txt")
    graph.obter_numero_total_votacoes("resultados_votacoes.txt")

if __name__ == "__main__": #Encapsulou o main
    main()


