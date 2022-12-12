print('Bom dia')
maior=0 
numero = int(input("Insira um número:"))
while (numero !=0):
    if(numero>maior):
        maior=numero
    numero = int(input("Insira um número:"))
print ('o maior número digitado:', maior)    