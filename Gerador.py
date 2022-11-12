import random

while True:

    print('\n[=-=-=-=-=[Gerador de senhas]=-=-=-=-=]\n')

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&çÇ'

    qnt_senha = int(input('Quantas senhas você quer gerar? '))

    qnt_caracteres = int(input('Quantos caracteres terá essa senha? '))

    print('\n------Senhas geradas------\n')

    for senha in range(qnt_senha):
        senhas = ''
        for tamanho in range(qnt_caracteres):
            senhas += random.choice(chars)
        print(senhas, '\n')
        arquivo = open('senhas.txt', 'a', encoding='utf-8')
        linhas = [senhas]
        for senhas in linhas:
            arquivo.write(senhas)
            arquivo.write('\n\n')

    op = str(input('Deseja sair do Gerador <S>im ou <N>ão: '))
    if not op == "N" or op == "n":
        print('\nPrograma finalizado...\n')
        break
