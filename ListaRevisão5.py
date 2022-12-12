print('Bom dia')
count=0
for idade in range(10):
    idade = int(input('Digite sua idade:'))
    if(idade>=18):
        count=count+1
print('Maiores de idade:', count)