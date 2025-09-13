# criar informações - POST
# firebase é uma plataforma do google que oferece diversos serviços para desenvolvimento de aplicativos web e mobile.

# UM BANCO DE DADOS DA GOOGLE.
# Você se comunica com o banco de dados através de requisições.
import requests
requisicao = requests.get(
    'https://my-project-python-fbb7c-default-rtdb.firebaseio.com/.json')
# no firebase toda requisição deve terminar com .json por obrigação.
print(requisicao)
print(requisicao.json())

requisicao01 = requests.post(
    'https://my-project-python-fbb7c-default-rtdb.firebaseio.com/.json')
# no firebase toda requisição deve terminar com .json por obrigação.
print(requisicao01)
print(requisicao01.json())
