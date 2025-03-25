import random

print('===========================================')
print('Bem Vindo(a) ao Jogo De Adivinhações Master')
print('===========================================')

numero = round(random.randrange(1,51))
total_de_tentativas = 5
pontos= 100

print('Qual o nivel desejado?\n')
print('(1) Facil (2) Medio (3) Dificil')

nivel = int(input('Digite o nivel Desejado '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5    



for rodada in range (1,total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite um numero entre 1 e 30: '))

    if(chute < 1 or chute > 30):
        print('você deve digitar um número entre 1 e 30')
        continue

    acertou = numero == chute
    chute_maior = chute > numero
    chute_menor = chute < numero

    print(f'Você Digitou {chute}')
        
    if(acertou):
        print(f'Você Acertou!!! Sua Pontuação foi {pontos} pontos ')
        break
        
    else: 
        if(chute_maior):
            (print('Seu Número foi maior que o Número Escolhido'))

        elif(chute_menor):
            (print('Seu número foi menor que o Número Escolhido'))
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

print('==============')
print('Fim De Jogo!!!')
print('==============')