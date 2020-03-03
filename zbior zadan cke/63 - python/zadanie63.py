licznik1 = 0
zad1 = []
licznik2 = 0
licznik3 = 0
maks = min = 5500
def rozklad(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki

with open('ciagi.txt','r') as file:
    for line in file:
        line = line.strip()
        d = len(line)
        dec = int(line,2)
        # 1
        if d % 2 == 0:
            n = int(d/2)

            if line[:n] == line[n:]:
                licznik1 += 1
                zad1.append(line)

        # 2
        dobry = 1
        for i in range(d - 1):
            if line[i] == '1' and line[i+1] == '1':
                dobry = 0
        if dobry:
            licznik2 += 1

        #3
        if len(rozklad(dec)) == 2:
            licznik3 += 1
            if dec < min:
                min = dec
            if dec > maks:
                maks = dec

with open('wynik_ciagi.txt','w') as w:
    w.write('63.1\n')
    for liczba in zad1:
        w.write(liczba+'\n')
    w.write('63.2\n'
            + str(licznik2)+'\n'
            + '63.3\n'
            + str(licznik3) + '\n'
            + str(min) + '\n'
            + str(maks) + '\n')
