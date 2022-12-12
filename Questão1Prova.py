numero = [-22,-100,-55,-70,-73,-90]
i = 0
count=0
maior =numero[0]
menor = numero[0]
for i in numero:
    count=count+1
    if( i > maior):
        maior = i

    if(i < menor):
        menor = i
print('menor: ',menor)
print('maior: ', maior)
print('Quantidade: ', count)