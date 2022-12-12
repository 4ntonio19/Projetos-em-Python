print('Bom dia')
av1 = int(input('AV1:'))
av2 = int(input('AV2:'))
media = (av1 + av2)/2

if (media >= 6):
    print('APROVADO')
if (media >4 and 5.9>=media):
    print('FINAL')
if (media<4):
    print('REPROVADO')
print('Sua média:{}'.format(media))