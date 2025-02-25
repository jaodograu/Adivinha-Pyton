print('=======================================================================================================================')
print('Bem Vindo(a) ao Jogo De Adivinhações Master')

chute = int(input('Digite o seu número: '))

numero = 18
acertou = numero == chute
chute_maior = chute > numero
chute_menor = chute < numero



print(f'Você Digitou {chute}')


if(acertou):
    print('Você Descobriu :o')

else: 
    if(chute_maior):
        (print('Seu Número foi maior que o Número Escolhido'))

    elif(chute_menor):
        (print('Seu número foi menor que o Número Escolhido'))


