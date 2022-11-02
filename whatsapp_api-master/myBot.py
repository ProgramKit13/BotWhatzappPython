# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 23:10:59 2022

@author: Rodrigo
"""

#pacotes necessarios! Os pacotes são baixados e inseridos na pasta do programa
#e o from fara a busca destes pacotes


#para enviar menssagens para numeros diferentes https://web.whatsapp.com/send?phone=xxxx

from time import sleep
from whatsapp_api import WhatsApp

wp = WhatsApp()

input("Pressione enter após escanear o Qr Code.")


#lista de nomes ou numeros pesquisados
nomes_palavras_chaves = ['Carolina Barbieri', 'Natalia Barbieri', 'Gabriela Barbieri']

#loop para pegar apenas os primeiros nomes de cada
primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chaves]


for primeiro_nome, nome_pesquisar in zip(primeiros_nomes, nomes_palavras_chaves):
    #para procurar o contato o qr deve ser carregado primeiro
    wp.search_contact(nome_pesquisar)
    menssagem = f"Ola {primeiro_nome}!Este é um teste de automatização de whatzzap! Ignore esta menssagem."
    sleep(2)
    wp.send_message(menssagem)

#esperar 10s e fechar
sleep(60)
wp.driver.close()