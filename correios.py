from bs4 import BeautifulSoup
import requests

#Primeiro buscar a pagina
url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaEndereco.cfm"
cep = input('Digite um CEP: ')
requesicao = requests.post(url, data={"CEP":cep})
#buscar o HTML dentro do request
html = requesicao.text
soup = BeautifulSoup(html, 'html.parser')
#Encontrar o elemento de endereço
input_cep = soup.table.contents[3].contents
endereco = [input_cep[1].contents, input_cep[3].contents, input_cep[5].contents, input_cep[7].contents]
for i in range(len(endereco)):
    endereco[i] = endereco[i][0].replace("\xa0","")
print(endereco)

