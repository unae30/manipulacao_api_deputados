import requests
#------------------------Funcionando--------------------------
class API:  
    def __init__(self):
        self.url = 'https://dadosabertos.camara.leg.br/arquivos/votacoesVotos/json/votacoesVotos-2023.json'

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200: #200 é uma convensão para quando a requisição funciona
            data = response.json()
            return data
        else:
            print('Falha na requisição:', response.status_code)
            return None

    def get_data(self):
        data = self.fetch_data()
        if data is None:
            print("Falha ao obter os dados da API.")
            return None

        return data



















    # def obter_votacoes(self):   #Está funcionando corretamente 

    #     url = 'https://dadosabertos.camara.leg.br/arquivos/votacoesVotos/json/votacoesVotos-2023.json'  

    #     response = requests.get(url)
    #     if response.status_code == 200: #teste para saber se funcionou direito. 200 é uma convenção do HTTP
    #         votacoes = response.json()
    #         print("Funcionou direito")
    #         return votacoes
    #     else:
    #         print('Falha na requisição:', response.status_code)
    #         return None

    # def obter_dados_api(self):
    #     dados_api = self.obter_votacoes()
    #     if dados_api is None:
    #         print("Falha ao obter os dados da API.")
    #         return None

    #     return dados_api
