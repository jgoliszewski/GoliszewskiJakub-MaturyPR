ulamki = []
with open('dane_ulamki.txt','r') as file:
	for line in file:
		l, m = line.strip().split(" ")
		l = int(l)
		m = int(m)
		ulamki.append([l, m])
#1
zad1 = 120000
odp1 = []
#2
zad2 = 0

def wzgledna_pierwszosc(a, b):
	if a > b:
		a, b = b, a
	for i in range(2,int(a)+1):
		if a % i == 0 and b % i == 0:
			return False
	return True

#3
zad3 = 0
def skracanie(a, b):
	d = 2
	while not wzgledna_pierwszosc(a, b):
		while a % d == 0 and b % d == 0:
			a /= d 
			b /= d
		d += 1
	return int(a), int(b)
#4
def NWD(a, b):
	while b != 0:
		b, a = a % b, b
	return a

def najmniejszaWW(a, b):
	return (a * b) / NWD(a, b)

def dodawanie_ulamkow(a, b):
	if a == [0, 0]:
		return b
	m = najmniejszaWW(a[1], b[1])
	l = ((m / a[1]) * a[0]) + ((m / b[1]) * b[0])
	return [l, m]
zad4 = [0,0]
		
for ul in ulamki:
	ulamek = ul[0] / ul[1] 
	if ulamek < zad1:
		zad1 = ulamek
		odp1 = ul
	if ulamek == zad1 and ul[1] < odp1[1]:
		odp1 = ul
	if wzgledna_pierwszosc(ul[0], ul[1]):
		zad2 += 1
	zad3 += skracanie(ul[0], ul[1])[0]
	zad4 = dodawanie_ulamkow(zad4, ul)
b = 2*2*3*3*5*5*7*7*13
zad4 = int(dodawanie_ulamkow(zad4, [0,b])[0])

with open('wyniki_ulamki.txt','w') as w:
	w.write('1)\n' + str(zad1) + '\n'
			+ '2)\n' + str(zad2) + '\n'
			+ '3)\n' + str(zad3) + '\n'
			+ '4)\n' + str(zad4))