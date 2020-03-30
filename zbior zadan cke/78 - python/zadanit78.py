dane_podpisy = []
dane_wiad = []

with open('podpisy.txt','r') as file:
	for line in file:
		dane_podpisy.append([int(x) for x in line.strip().split()])

with open('wiadomosci.txt','r') as file:
	for line in file:
		dane_wiad.append(line.strip())

def skrot(wiad):
	S = []
	for l in "ALGORYTM":
		S.append(ord(l))
	x = len(wiad) % 8
	if x != 0:
		for x in range(8-x):
			wiad += '.'
	dl = len(wiad)
	tab_wiad = []
	while wiad != '':
		tab_wiad.append(wiad[0:8])
		wiad = wiad[8:]

	for p in tab_wiad:
		for j in range(8):
			S[j] = (S[j] + ord(p[j])) % 128
	wynik = ""
	for j in range(8):
		wynik += chr(65 + (S[j] % 26))
	return wynik, dl, S

def deszyfrA(podpis, d=3, n=200):
	t = []
	odp = ''
	for l in podpis:
		t.append((l * d) % n)
	for x in t:
		odp += chr(x)
	return odp

#1
zad1_skrot, zad1_dl, zad1_tablicaS = skrot(dane_wiad[0])

#2
zad2 = ''
for x in dane_podpisy:
	zad2 += str(deszyfrA(x))+'\n'

#3
zad3 = ''
for i in range(11):
	if skrot(dane_wiad[i])[0] == deszyfrA(dane_podpisy[i]):
		zad3 += str(i+1)+' '

with open('epodpis_wynik.txt','w') as w:
	w.write('1)\n' + str(zad1_dl) + '\n'
		+ str(zad1_tablicaS) + '\n'
		+ str(zad1_skrot)
		+ '\n\n2)\n' + zad2
		+ '\n\n3)\n' + zad3)