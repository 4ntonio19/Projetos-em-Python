def x():
    count=0
    for idade in range(5):
         idade = int(input('Insira sua idade:'))
         if(idade>=18):
             count=count+1
    print('Quantidade de maiores:', count)
x()