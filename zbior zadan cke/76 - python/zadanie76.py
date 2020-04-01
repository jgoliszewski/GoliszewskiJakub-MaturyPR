dane_szyfr1 = []
dane_szyfr2 = []
dane_szyfr3 = []
with open('szyfr1.txt','r') as file:
	for line in file:
		dane_szyfr1.append(line.strip())
with open('szyfr2.txt','r') as file:
	for line in file:
		dane_szyfr2.append(line.strip())
with open('szyfr3.txt','r') as file:
	for line in file:
		dane_szyfr3.append(line.strip())

def szyfrowanie(napis, P):
	napis = list(napis)
	for i in range(len(napis)):
		k = i % len(P)
		napis[i], napis[P[k]-1] = napis[P[k]-1], napis[i]


	szyfr = ''
	for l in napis:
		szyfr += l
	return szyfr
#1
zad1 = ''
klucz1 = dane_szyfr1[6].split(" ")
klucz1 = [int(x) for x in klucz1]
for i in range(6):
	zad1 += f'{szyfrowanie(dane_szyfr1[i],klucz1)}\n'

with open('wyniki_szyfr1.txt','w') as w:
	w.write(zad1)

#2
napis2 = dane_szyfr2[0]
klucz2 = [int(x) for x in dane_szyfr2[1].split()]
zad2 = f'{szyfrowanie(napis2,klucz2)}'

with open('wyniki_szyfr2.txt','w') as w:
	w.write(zad2)

#3
for x in dane_szyfr3:
	napis3 = x

def deszyfrowanie(napis, P):
	napis = list(napis)
	for i in range(len(napis)-1,-1,-1):
		k = i % len(P)
		napis[i], napis[P[k]-1] = napis[P[k]-1], napis[i]
	
	szyfr = ''
	for l in napis:
		szyfr += l
	return szyfr

zad3 = deszyfrowanie(napis3,[6,2,4,1,5,3])
print(zad3)
with open('wyniki_szyfr3.txt','w') as w:
	w.write(zad3)