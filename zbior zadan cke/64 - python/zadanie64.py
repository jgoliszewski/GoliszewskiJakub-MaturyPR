obrazki = []
obrazki_bez_bitow = []
for i in range(200):
	obrazki.append([])
	obrazki_bez_bitow.append([])
k = 0
with open('dane_obrazki.txt','r') as dane:
	for line in dane:
		line = line.strip()
		if line != "":
			obrazki[k].append(line)		
		if line == "":
			k+=1 
for i, obrazek in enumerate(obrazki):
	for k in range(20):
		obrazki_bez_bitow[i].append(obrazek[k][:-1])

"""
for i, obrazek in enumerate(obrazki_bez_bitow):
	print("=========",i,"=========")
	for linia in obrazek:
		print(linia)
	break
"""

zad1 = 0
zad1_max = 0
for obrazek in obrazki:
	czarne = 0
	for x in range(20):
		for y in range(20):
			if obrazek[x][y] == '1':
				czarne += 1
	if czarne > 200:
		zad1 += 1
	if czarne > zad1_max:
		zad1_max = czarne
print("\nZadanie 1")
print(zad1)
print(zad1_max)


zad2 = 0
zad2_obrazek = []
p = 0
for obrazek in obrazki_bez_bitow:
	gora = []
	dol = []
	lewo = []
	prawo = []
	for i in range(0,10):
		gora.append(obrazek[i])
	for i in range(10,20):
		dol.append(obrazek[i])
	for i in range(20):
		lewo.append(obrazek[i][0:10])
		prawo.append(obrazek[i][10:20])
	if gora == dol and lewo == prawo:
		zad2 += 1
		if p == 0:
			zad2_obrazek = obrazek
			p += 1
print("\nZadanie 2")
print(zad2)
for l in zad2_obrazek:
	print(l)

zad3_poprawne = 0
zad3_naprawialne = 0
zad3_nienaprawialne = 0
zad3_naj = 0
zad4 = []
for i in range(len(obrazki)):
	niepoprawne_bity_wierszy = 0
	niepoprawne_bity_kolumn = 0
	for x in range(20):
		l = obrazki_bez_bitow[i][x].count("1")
		if l % 2 == 0 and obrazki[i][x][20] == '1':
			niepoprawne_bity_wierszy += 1
		if l % 2 == 1 and obrazki[i][x][20] == '0':
			niepoprawne_bity_wierszy += 1
	for y in range(20):
		jedynki = 0
		for x in range(20):
			if obrazki[i][x][y] == '1':
				jedynki += 1
		if jedynki % 2 == 0 and obrazki[i][20][y] == '1':
			niepoprawne_bity_kolumn += 1
		if jedynki % 2 == 1 and obrazki[i][20][y] == '0':
			niepoprawne_bity_kolumn += 1
	if niepoprawne_bity_wierszy + niepoprawne_bity_kolumn > zad3_naj:
		zad3_naj = niepoprawne_bity_kolumn + niepoprawne_bity_wierszy
	if niepoprawne_bity_kolumn == 0 and niepoprawne_bity_wierszy == 0:
		zad3_poprawne += 1
	elif (niepoprawne_bity_kolumn + niepoprawne_bity_kolumn) <= 2 and niepoprawne_bity_kolumn < 2 and niepoprawne_bity_wierszy < 2:
		zad3_naprawialne += 1
		#zad4
		pixel = [i+1]

		rzad = 0
		kolumna = 0
		for x in range(20):
			l = obrazki_bez_bitow[i][x].count("1")
			if l % 2 == 0 and obrazki[i][x][20] == '1':
				rzad = x + 1
			if l % 2 == 1 and obrazki[i][x][20] == '0':
				rzad = x + 1
		for y in range(20):
			jedynki = 0
			for x in range(20):
				if obrazki[i][x][y] == '1':
					jedynki += 1
			if jedynki % 2 == 0 and obrazki[i][20][y] == '1':
				kolumna += y + 1
			if jedynki % 2 == 1 and obrazki[i][20][y] == '0':
				kolumna += y + 1
		if rzad != 0 and kolumna != 0:
			pixel.append(rzad)
			pixel.append(kolumna)
		elif rzad == 0:
			pixel.append("21")
			pixel.append(kolumna)
		elif kolumna == 0:
			pixel.append(rzad)
			pixel.append("21")
		zad4.append(pixel.copy())


	if niepoprawne_bity_kolumn >= 2 or niepoprawne_bity_wierszy >= 2:
		zad3_nienaprawialne += 1
print("\nZadanie 3") 
print(zad3_poprawne)
print(zad3_naprawialne)
print(zad3_nienaprawialne)
print(zad3_naj)
print("\nZadanie 4")
for x in zad4:
	print(x)