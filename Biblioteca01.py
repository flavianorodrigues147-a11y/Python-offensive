# Retorna a ultima ocorrência das moedas selecionadas.
# Ex.: https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

#A AwesomeAPI é uma plataforma brasileira que oferece APIs públicas e gratuitas para acesso a dados como: Cotação de moedas, mais de 150 moedas disponíveis em tempo real. Inclui dólar, euro, bitcoin e outras. Suporte a cotações comerciais, turismo e PTAX (referência do Banco Central).

#O get serve para pegar informações de um site.
#Pegar informações - GET

import requests
requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)
print(requisicao.json())

#o que é json? json é um formato de dados leve, usado para troca de informações entre sistemas.
#json tem o formato de dicionário por isso podemos acessar os valores pelas chaves
#o json retornado é um dicionário com outros dicionários dentro.

# Envia dados em formato JSON usando requests.
# O parâmetro 'json=' converte automaticamente o dicionário Python em JSON
# e adiciona o cabeçalho 'Content-Type: application/json' à requisição.
# A resposta pode ser convertida de volta com .json() para manipulação dos dados.


