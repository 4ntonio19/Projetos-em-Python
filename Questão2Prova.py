somai=0
somaa=0
count=0
menor=0
for idade in range (3):
    idadae=int(input('Digite sua idade:'))
    altura=float(input('Digite sua altura:'))
    
    somai=somai+idade
    somaa=altura+somaa
    if(idade>count):
        count=idade 
    if(idade<menor):
        menor=idade
mediai=somai/30 
mediah=somaa/30
print('A media das idade e',mediai,'A media das alturas e',mediah,'A maior idade:',count,'menor idade',menor)