soma1=0
soma2=0
maior=0
menor=0
idade= int(input("Insira sua idade:"))
menor=idade
for idade in range(29):
    altura= float(input("insira sua altura;"))
    idade= int(input("Insira sua idade:"))
    
    soma1=idade+soma1
    soma2=altura+soma2
    
    if(idade>maior):
        maior=idade
    if(idade<menor):
        menor=idade
        
media1=soma1/2
media2=soma2/2
print("A idade media do grupo é: ", media1)
print("A altura meedia grupo é:", media2)
print("A maior idade digitada foi: ", maior)
print("A menor idade digitada foi: ", menor)
