import os
import requests
import logging

from datetime import datetime
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError
from sqlalchemy.exc import SQLAlchemyError, OperationalError, ProgrammingError

from database import Projeto_clima2
from Banco_conexões import Session

def extrair_dados_api(woeid):

    try:

        url = (f"https://api.hgbrasil.com/weather?format=json&array_limit=2&fields=only_results,city_name,time,rain,"
               f"wind_speedy,humidity,description,cloudiness,date,temp&key={os.getenv('KEY')}&woeid={woeid}")
        dados = requests.get(url)
        dados = dados.json()
        return dados

    except RequestException as e:
        logging.error(f"Erro ao fazer a requisição para a API: {e}")

    except JSONDecodeError:
        logging.error("Erro ao decodificar a resposta JSON. A resposta pode não ser válida.")

    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")


def reestrutura_dados(dado):

    try:

        dado["wind_speedy"] = dado["wind_speedy"].replace("km/h","")
        dado["wind_speedy"] = float(dado["wind_speedy"])
        dado["date"] = datetime.strptime(dado["date"], "%d/%m/%Y").date()
        return dado

    except ValueError:
        logging.error("Erro de argumento. Verifique os valores passo na função reestrutura_dados.")



def enviar_dados_banco(dados):

    try:

        with Session() as session:
            registro = Projeto_clima2(**dados)
            session.add(registro)
            session.commit()

    except OperationalError:
        logging.error("Erro de conexão: o banco de dados pode estar fora do ar ou inacessível.")
    except ProgrammingError:
        logging.error(
            "Erro de programação: verifique se o banco de dados existe e se os nomes das tabelas/colunas estão corretos.")
    except SQLAlchemyError as e:
        logging.error(f"Ocorreu um erro ao tentar salvar no banco: {e}")

def atualizar_banco():

    try:

        for i in range(3):

            cidades = [455827,455823,456379]
            extraido = extrair_dados_api(cidades[i])
            reestruturado = reestrutura_dados(extraido)
            enviar_dados_banco(reestruturado)

    except IndexError:
        logging.error("Erro de acesso aos índices. Sugiro verificar a função atualizar_banco e a lista cidades.")
