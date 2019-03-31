#Teste de programa para acessar uma url

import math
import requests # importando a biblioteca de acessos url
import json
import pandas as pd #importar a biblioteca pandas, dando o alias (apelido) pd

url="http://data.fixer.io/api/latest?access_key=27434bfe92edde6a5a5d68303ef4b443"

print("Acessando Base de Dados ....")
response = requests.get(url)

if response.status_code == 200: # "status.code é uma resposta de uma lista"
    print("Acesso Bem Sucedido !!!")
    print("Buscando informações das moedas ....")

    dados = response.json() #todo json é um dicionário
    day = dados['date']
    print("Acessando dados do dia %s/%s/%s" % (day[8:],day[5:7],day[0:4]))

#    print("Valor do Euro.: %.2f" % dados['rates']['EUR'])
#    print("Valor do Real.: %.2f" % dados['rates']['BRL'])
#    print("Valor do Dolar.: %.2f" % dados['rates']['USD'])
#    print("Valor do BitCoin.: ", dados['rates']['BTC'])

    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
    dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
    btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)

    print("Convertendo ....")

    print("%.2f" % euro_real)
    print("%.2f" % dollar_real)
    print("%.2f" % btc_real)

    #criando a tabela de dados
    df = pd.DataFrame({'Moedas': ['Euro', 'Dollar', 'Bitcoin'], 'Valores':[euro_real, dollar_real, btc_real]})
    #exportando para csv - arquivo de tabelas que o excel entende, sem coluna de indice e
    #utilizando o ";" como separador das colunas

    #Se quiser dar um nome ao índice
    #df.index.name = "Item" 
    print("Gerando Arquivo CSV....")

    df.to_csv("valores.csv", index=False, sep=";") #aqui ele desconsidera a colona de índice

    print("Arquivo CSV gerado com SUCESSO !!!")

    
else:
    print("Error na conexão !!!")


print(response)

# resposta [200] significa que houve conexão
# [404] significa que não, enfim, só olhar a lista
