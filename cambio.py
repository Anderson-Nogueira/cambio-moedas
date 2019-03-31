#Teste de programa para acessar uma url

import requests # importando a biblioteca de acessos url
import json

url="http://data.fixer.io/api/latest?access_key=27434bfe92edde6a5a5d68303ef4b443"

print("Acessando Base de Dados ....")
response = requests.get(url)

if response.status_code == 200: # "status.code é uma resposta de uma lista"
    print("Acesso Bem Sucedido !!!")
    print("Buscando informações das moedas ....")

    dados = response.json() #todo json é um dicionário
    day = dados['date']
    print("Acessando dados do dia %s / %s / %s" % (day[8:],day[5:7],day[0:4]))

    print("Valor do Euro.: %.2f" % dados['rates']['EUR'])
    print("Valor do Real.: %.2f" % dados['rates']['BRL'])
    print("Valor do Dolar.: %.2f" % dados['rates']['USD'])
    print("Valor do BitCoin.: ", dados['rates']['BTC'])

    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']

    print("Convertendo ....")

    print("%.2f" % euro_real)
    print("%.2f" % dollar_real)
    print("%.2f" % btc_real)
else:
    print("Error na conexão !!!")


print(response)

# resposta [200] significa que houve conexão
# [404] significa que não, enfim, só olhar a lista
