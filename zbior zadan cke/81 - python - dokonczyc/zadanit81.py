dane1 = []
dane2 = []
with open('wspolrzedne.txt','r') as file:
	for line in file:
		line = line.strip().split('	')
		line = [int(x) for x in line]
		dane1.append(line)
with open('wspolrzedneTR.txt','r') as file:
	for line in file:
		line = line.strip().split('	')
		line = [int(x) for x in line]
		dane2.append(line)
#1
zad1 = 0

#2

zad2 = 0
#3
def dlugosc_odcinka(Xa, Ya, Xb, Yb):
	d = pow(pow(Xb-Xa,2)+pow(Yb-Ya,2),1/2)
	return d
def obwod_trojkata(wierzcholki):
	Xa, Ya, Xb, Yb, Xc, Yc = wierzcholki
	obwod = dlugosc_odcinka(Xa, Ya, Xb, Yb)\
	 		+dlugosc_odcinka(Xa, Ya, Xc, Yc)\
	 		+ dlugosc_odcinka(Xb, Yb, Xc, Yc)
	return obwod
zad3_dl = 0
zad3_wsp = []
#4
def pitagoras(x, y, z):
	list = [x**2 for x in [x,y,z]]
	if sum(list) == 2 * max(list):
		return True
	else:
		return False

zad4 = 0
#5
for wierzcholki in dane1:
	Xa, Ya, Xb, Yb, Xc, Yc, = wierzcholki
	z1 = True
	for w in wierzcholki:
		if w <= 0:
			z1 = False
	if z1:
		zad1 += 1
	if (Yb - Ya)*(Xc - Xb) == (Yc - Yb)*(Xb - Xa):
		zad2 += 1 
for wierzcholki in dane2:
	Xa, Ya, Xb, Yb, Xc, Yc, = wierzcholki
	obwod = obwod_trojkata(wierzcholki)
	if obwod > zad3_dl:
		zad3_dl = obwod
		zad3_wsp = wierzcholki
	a = dlugosc_odcinka(Xa, Ya, Xb, Yb)
	b = dlugosc_odcinka(Xa, Ya, Xc, Yc)
	c = dlugosc_odcinka(Xb, Yb, Xc, Yc)
	if pitagoras(a, b, c):
		zad4 += 1
print(zad4)
