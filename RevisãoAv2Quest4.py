lista=[13,23,25,40,55,21,5,7,9,8,6,4]
del lista[:3]
for impares in lista:
    if(impares % 2 !=0):
        print('Os números impares:', impares)
