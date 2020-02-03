import sys
import requests
import time
from bs4 import BeautifulSoup

# Digite aqui seu código de rastreio como uma string
codigoDeRastreio = ''

payload = {
    'acao': 'track',
    'objetos': codigoDeRastreio,
    'btnPesq': 'Buscar'
}

tam = 0

while True:
    try:
        req = requests.post(
            'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?', data=payload)
        data = req.text
    except Exception as error:
        print('Erro: ', error, '\nEncerrando Script')
        sys.exit()

    soup = BeautifulSoup(data, 'html.parser')

    listaEventos = soup.find_all('td', class_='sroLbEvent')
    listaDatas = soup.find_all('td', class_='sroDtEvent')

    if tam != len(listaEventos):
        print("\t======== ULTIMO LOCAL VISTO DA ENCOMENDA ========")
        ultimoEvento = listaEventos[0].find_all('br')
        for i in ultimoEvento:
            print(i.next_element)

        ultimaData = listaDatas[0].find_all('br')
        for i in ultimaData:
            print(i.next_element)

    tam = len(listaEventos)

    time.sleep(60)
