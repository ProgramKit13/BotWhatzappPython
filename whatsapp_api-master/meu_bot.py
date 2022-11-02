"""
NOTE: This example has been presented at the following course: https://www.udemy.com/course/aprenda-a-programar-um-bot-do-whatsapp
"""

# Importar pacotes necessarios

from selenium import webdriver
from time import sleep
from whatsapp_api import WhatsApp


# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
nomes_palavras_chaves = ['Carolina Barbieri Gerente']

# Lista dos nomes que vou me referir na mensagem
# primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chaves]
primeiros_nomes = ['Carolina']

menssagem = ['Teste de invasao 1', 'Teste de invasao 2', 'Teste de invasao 3', 'Teste de invasao 4']

# Loop para mandar mensagens para os clientes
for primeiro_nome, nome_pesquisar, menssagens \
  in zip(primeiros_nomes, nomes_palavras_chaves, menssagem):
    
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    # Mensagem a ser enviada
    mensagem = f"Olá {primeiro_nome}! Voce esta sendo vitma de um teste de invasao! {menssagens}!"
    
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()
