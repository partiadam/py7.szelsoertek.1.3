lista = []
while True:
    beker = input('Szám: ')
    if beker == 'x' or beker == 'X':
        break
    else:
        lista.append(int(beker))

legkisebb = min([szamok for szamok in lista if szamok %2 == 0])
legnagyobb = max([szamok for szamok in lista if szamok %2 == 0])
print(f'Legkisebb páros szám: {legkisebb}')
print(f'Legnagyobb páros szám: {legnagyobb}')
