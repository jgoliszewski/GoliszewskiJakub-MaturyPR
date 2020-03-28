dane_geny = []
with open('dane_geny.txt','r') as file:
	for line in file:
		dane_geny.append(line.strip())

#1
gatunki = []
osobniki = []
for i in range(500):
	osobniki.append(0)

#2
zad2 = 0

def geny_z_genotypu(a):
	gen = ''
	ile_gen = 0
	max_dl = 0
	while a.find('AA') != -1 and a.find('BB') != -1:
		x = a.find('AA')
		y = a.find('BB')
		if x < y:
			gen += a[x:y+2]
			ile_gen += 1
			if y - x + 2 > max_dl:
				max_dl = y - x + 2
		a = a[y+2:]
	return gen, ile_gen, max_dl

#3
zad3_naj_l = 0
zad3_naj_dl = 0

#4
zad4_odporne = 0
zad4_silnie_odporne = 0

for genotyp in dane_geny:
	dl = len(genotyp)
	if dl not in gatunki:
		gatunki.append(dl)
	osobniki[dl] += 1
	gen, ile_gen, max_dl_gen = geny_z_genotypu(genotyp)
	if gen.find('BCDDC') != -1:
		zad2 += 1

	if max_dl_gen > zad3_naj_dl:
		zad3_naj_dl = max_dl_gen
	if ile_gen > zad3_naj_l:
		zad3_naj_l = ile_gen

	if genotyp == genotyp[::-1]:
		zad4_silnie_odporne +=1
	if gen == geny_z_genotypu(genotyp[::-1])[0]:
		zad4_odporne += 1
zad1_max = max(osobniki)
zad1_gatunki = len(gatunki) - 1

with open('wyniki_gen.txt','w') as w:
	w.write('1)\n' + str(zad1_gatunki) + '\n' + str(zad1_max)
			+ '\n2)\n' + str(zad2) 
			+ '\n3)\n' + str(zad3_naj_l) + '\n' + str(zad3_naj_dl)
			+ '\n4)\n' + str(zad4_odporne) + '\n' + str(zad4_silnie_odporne))

