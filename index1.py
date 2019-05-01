import threading
import time

print(' \n')
print('############# START PROJECT ############# \n')

#
# Leitura dos automotos
# http://www.devfuria.com.br/python/manipulando-arquivos-de-texto/
#
entrada_automotos = open('arquivos/ler/entrada_automotos.txt', 'r')

#Estados dos automotos:

q1 = 'Q1'
q2 = 'Q2'
q3 = 'Q3'
q4 = 'Q4'

#Array de saida
array_resposta = []

#Informa o estado inicial do automato
array = [q1]

def alterar_estado( entrada):

    for i in range(len(array)):   
        if(array[i] == q1):
            if(entrada == '0'):
                array.append(q1)
            if(entrada == '1'):
                pass
        if(array[i] == q2):
            pass


print('##### Estados AUTOMOTOS ##### \n')

print('Estado inicial: ' + q1)
 

for linha in entrada_automotos:
    for entrada in linha:
        print('Estado lido da entrada ===> ' + entrada)
        alterar_estado(entrada)
        print('Estados correntes ===> ', end="" )
        print(array)
        time.sleep(0.5)

print('\n')
print('############# END PROJECT #############')