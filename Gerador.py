import random

print('\n[=-=-=-=-=[Gerador de senhas]=-=-=-=-=]\n')


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_-=+çÇ[]().,;:'

qnt_senha = int(input('Quantas senhas você quer gerar? '))

qnt_caracteres = int(input('Quantos caracteres terá essa senha? '))


print('\n------Senhas geradas------\n')

for senha in range(qnt_senha):
    senhas = ''
    for tamanho in range(qnt_caracteres):
        senhas += random.choice(chars)
    print(senhas, '\n')

    