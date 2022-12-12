print('Bom dia')
nome = input("Seu nome:")
idade = int(input('Sua idade:'))
ano = 2022 - idade
txt = 'nome:{}, ano:{}'
print(txt.format(nome, ano))