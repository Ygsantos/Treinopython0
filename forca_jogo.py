def jogar1():
    print('===== JOGO DA FORCA ====')

    palavra_secreta = 'caixa'
    palavra_certa   =  ['_','_','_','_','_']
    enforcou        =  False
    acertou         =  False

    palavra_escolhida = input("DIGITE A PALAVRA A SER ENCONTRADA:  ")
    tamanho_da_palavra = len(palavra_escolhida)
    lista = []

    for posicao in range(0,tamanho_da_palavra):




    while not enforcou and not acertou:
        index = 0
        print(f'Indice de acerto da palavra',palavra_certa)
        chute = input(' DIGITE UMA LETRA:  ')
        chute = chute.strip()

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f' Encontrou a letra "{chute.upper()}" na posicao {index}')
                palavra_certa[index]  = letra
            index += 1


if __name__ == '__main__':
    jogar1()
