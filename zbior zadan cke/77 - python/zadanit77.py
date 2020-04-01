dane_dokad = ''
with open('dokad.txt','r') as file:
	for line in file:
			dane_dokad += line.strip()

dane_szyfr = []
with open('szyfr.txt','r') as file:
	for line in file:

		dane_szyfr.append(line.strip())


def szyfrowanie_litery(litera, klucz):
	l = 0
	k = ord(klucz) - 65
	if litera in [' ',',','.']:
		return litera
	else:
		l = ord(litera)+k
	if l > 90:
		l -= 26
	return chr(l)

def szyfrowanie_slowa(slowo, klucz):
	slowo = list(slowo)
	szyfr = ''
	klucz = list(klucz)
	i = 0
	for l in slowo:
		szyfr += szyfrowanie_litery(l,klucz[i%3])
		if l not in [' ',',','.']:
				i += 1	
	return szyfr

def deszyfrowanie_litery(litera, klucz):
	l = 0
	k = ord(klucz) - 65
	if litera in [' ',',','.']:
		return litera
	else:
		l = ord(litera)-k
	if l < 65:
		l += 26
	return chr(l)

def deszyfrowanie_slowa(slowo, klucz):
	slowo = list(slowo)
	szyfr = ''
	klucz = list(klucz)
	i = 0
	for l in slowo:
		szyfr += deszyfrowanie_litery(l,klucz[i%len(klucz)])
		if l not in [' ',',','.']:
				i += 1	
	return szyfr
#1
zad1_klucz = 'LUBIMYCZYTAC'
zad1 = szyfrowanie_slowa(dane_dokad, zad1_klucz)
dl = 0
for z in dane_dokad:
	if z not in ['.',',',' ']:
		dl += 1
zad1_powtorzenia = int(dl/len(zad1_klucz)) + 1

#2

zad2 = deszyfrowanie_slowa(dane_szyfr[0],dane_szyfr[1])

#3
n = 0
zad3_litery = []
for i in range(26):
	zad3_litery.append(0)
for l in list(dane_szyfr[0]):
	if l not in [' ',',','.']:
		zad3_litery[ord(l)-65] += 1
		n += 1
zad3_odp = ''
for i in range(26):
	zad3_odp += chr(i+65) + '-' + str(zad3_litery[i]) + '\n'

Ko1 = 0
for i in range(26): 
	Ko1 += zad3_litery[i] * (zad3_litery[i] - 1)

Ko = Ko1 / (n * (n - 1))

d = round(0.0285/ (Ko - 0.0385), 2)
dd = len(dane_szyfr[1])

with open('Vigenere_wyniki.txt','w') as w:
	w.write('1)\n' + str(zad1_powtorzenia) + '\n' + str(zad1)
			+ '\n\n2)\n' + str(zad2)
			+ '\n\n3)\n' + zad3_odp + f'\nszacowana dl - {d}\ndokladna dl - {dd}')
