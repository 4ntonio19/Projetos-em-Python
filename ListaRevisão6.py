print('Bom dia')
count=0
soma =0
for idade in range(10):
    idade=int(input('Digite sua idade:'))
    if(idade>=18):
        count=count+1
soma=idade+soma  
media=soma/10
print('a quantidade de pessoas é:',count)
print('A media:', media)
