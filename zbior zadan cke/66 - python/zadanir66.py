dane = []
with open('trojki.txt','r') as file:
	for line in file:
		trojka = line.strip().split()
		trojka = [int(x) for x in trojka]
		dane.append(trojka)

#1
zad1 = []

#2
def pierwsza(n):
	pierwsza = True
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, int(pow(n,1/2)) + 1):
		if n % i == 0:
			return False
	return True
zad2 = []

#3
def pitagoras(list):
	x, y, z = list
	c = max(x,y,z)
	a = min(x,y,z)
	b = (x + y + z) - (c + a)

	if a*a + b*b == c*c:
		return True
	else:
		return False

zad3 = []

#4
def boki_trojka(list):
	x, y, z = list
	c = max(x,y,z)
	a = min(x,y,z)
	b = (x + y + z) - (c + a)
	if a + b > c:
		return True
	return False

zad4_ile = 0
zad4_ciag_max = 0
zad4_ciag_aktual = 0
for i, trojka in enumerate(dane):
	suma = 0
	for c in str(trojka[0]):
		suma += int(c)
	for c in str(trojka[1]):
		suma += int(c)
	if suma == trojka[2]:
		zad1.append(trojka)

	if pierwsza(trojka[0]) and pierwsza(trojka[1]):
		if trojka[0] * trojka[1] == trojka[2]:
			zad2.append(trojka)

	if pitagoras(trojka):
		if pitagoras(dane[i+1]):
			zad3.extend([trojka])
			zad3.append(dane[i+1])

	if boki_trojka(trojka):
		zad4_ile += 1
		zad4_ciag_aktual += 1
	else:
		if zad4_ciag_aktual > zad4_ciag_max:
			zad4_ciag_max = zad4_ciag_aktual
		zad4_ciag_aktual = 0

with open('wyniki_trojki.txt','w') as w:
	w.write('1)\n')
	for x in zad1:
		w.write(str(x)+'\n')
	w.write('2)\n')
	for x in zad2:
		w.write(str(x)+'\n')
	w.write('3)\n')
	for x in zad3:
		w.write(str(x)+'\n')
	w.write('4)\n')
	w.write(str(zad4_ile)+'\n'
			+ str(zad4_ciag_max))


for x in zad3:
	print(x)