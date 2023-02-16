def jogar1():

    import random
    print('=== JOGO DE ADIVINHACAO ===')

    valor = random.randrange(1, 101)
    print(valor)
    tentativas = random.randrange(1, 10)
    print(tentativas)
    pontos = 1000

    print(F'=== VOCE TEM {tentativas} TENTATIVAS ===')

    for _ in range(0, tentativas):
        print(f'Tentativa numeron {_}/{tentativas} \n Quantidade de Pontos: {pontos}')
        print(_)
        chute = int(input('Insira o valor do chute entre 0 e 100 >>>   '))

        if chute == valor:
            print(f'VC ACERTOU é o número: {valor} e fez {pontos} pontos')
            break

        else:
            pontos_perdidos = abs(valor - chute)
            pontos = pontos - pontos_perdidos
            if chute < valor:
                print('chute baixo, tente mais alto!')

            elif chute >valor:
                print('chute alto, tente mais baixo')


        if (_ + 1) == tentativas:
            print(f'Acabaram suas tentativas {_+1}/{tentativas} , o número era: {valor}')
            break
if __name__ == '__main__':
    jogar1()