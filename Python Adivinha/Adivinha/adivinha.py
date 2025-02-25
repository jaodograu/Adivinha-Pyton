print('===========================================')
print('Bem Vindo(a) ao Jogo De Adivinhação!')
print('===========================================')

numero_secreto = 12
total_de_tentativas = 5
rodada = 1

while (rodada <= total_de_tentativas):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    print(f'Você Digitou {chute}')

    if(acertou):
        print('Você Acertou!!!')

    else: 
        if(chute_maior):
            (print('Seu Número foi maior que o Número Escolhido'))

        elif(chute_menor):
            (print('Seu número foi menor que o Número Escolhido'))

        rodada = rodada + 1

print('-----------')
print('Fim de Jogo')
print('-----------')



