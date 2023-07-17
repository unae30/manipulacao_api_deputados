import json
from api import API

class Grafo_Deputados:
    def __init__(self):
        self.adj_list = {}
        self.contados_nos = 0
        self.contador_aresta = 0

    def adicionar_no(self, no):
        if no not in self.adj_list:
            self.adj_list[no] = {}
            self.contados_nos += 1

    def adicionar_aresta1(self, no1, no2, peso):
        if no1 not in self.adj_list:
            self.adicionar_no(no1)
        if no2 not in self.adj_list:
            self.adicionar_no(no2)
        try:
            self.adj_list[no1][no2] = peso
            self.contador_aresta += 1
        except KeyError as e:
            print(f"AVISO: No {e} nÃ£o existe")
  
    def there_is_edge(self, node1, node2):
        try:
            return node2 in self.adj_list[node1]
        except KeyError as e:
            return False

    def criar_grafo_ponderado(self):
        dados_filtrados = self.get_filtered_data()
        for item in dados_filtrados:
            for item2 in dados_filtrados:
                if item['IdVotacao'] == item2['IdVotacao'] and item['Voto'] == item2['Voto'] and item != item2:
                    existe = self.there_is_edge(item['Nome'], item2['Nome'])
                    if existe == False:
                        self.adicionar_aresta1(item['Nome'], item2['Nome'], 1)
                    else:
                        self.adj_list[item['Nome']][item2['Nome']] += 1


    def get_filtered_data(self):
        api = API()
        data = api.get_data()

        if data is not None:
            filtered_data = []

            for item in data['dados']:
                nome = item['deputado_']['nome'] 
                partido = item['deputado_']['siglaPartido'] 
                id_votacao = item['idVotacao'] 
                voto = item['voto']
                id_deputado = item['deputado_']['id']
                filtered_data.append({
                    'Nome': nome,
                    'Partido': partido,
                    'IdVotacao': id_votacao,
                    'Voto': voto,
                    'IdDeputado': id_deputado
                })

            return filtered_data
        else:
            return []
        
    def obter_deputados_com_votos_em_comum(self):
        deputados_com_votos = {}
        for deputado in self.adj_list:
            deputados_com_votos[deputado] = []
            for outro_deputado in self.adj_list[deputado]:
                votos_em_comum = self.adj_list[deputado][outro_deputado]
                if votos_em_comum > 0:
                    deputados_com_votos[deputado].append((outro_deputado, votos_em_comum))
        return deputados_com_votos
    
    def escrever_resultados_em_arquivo(self, nome_arquivo):
        deputados_com_votos = self.obter_deputados_com_votos_em_comum()

        n_nos = self.contados_nos
        n_arestas = self.contador_aresta

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f'{n_nos} {n_arestas}\n\n')
            for deputado, votos_em_comum in deputados_com_votos.items():
                if len(votos_em_comum) > 0:
                    #arquivo.write(f"Deputado: {deputado}\n")
                    for outro_deputado, quantidade in votos_em_comum:
                        arquivo.write(f"{deputado} {outro_deputado}: {quantidade}\n")
                    arquivo.write("\n")

    def obter_numero_total_votacoes(self, nome_arquivo):
        numero_total_votacoes = {}
        dados_filtrados = self.get_filtered_data()

        for item in dados_filtrados:
            nome = item['Nome']
            if nome not in numero_total_votacoes:
                numero_total_votacoes[nome] = 1
            else:
                numero_total_votacoes[nome] += 1

        with open(nome_arquivo, 'w') as arquivo:
            for deputado, numero_votacoes in numero_total_votacoes.items():
                arquivo.write(f"{deputado}: {numero_votacoes}\n")

