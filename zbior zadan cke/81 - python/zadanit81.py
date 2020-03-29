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
	l = [a**2 for a in [x,y,z]]
	if sum(l) == 2 * max(l):
		return True
	else:
		return False

zad4 = 0
#5
zad5 = []
def srodek(xa,ya,xb,yb):
	xs = (xa + xb) / 2
	ys = (ya + yb) / 2
	return xs, ys

def punktD(xb, yb, xs, ys):
	xd = 2 * xs - xb
	yd = 2 * ys - yb
	return xd, yd

for wierzcholki in dane2:
	Xa, Ya, Xb, Yb, Xc, Yc, = wierzcholki
	obwod = obwod_trojkata(wierzcholki)
	if obwod > zad3_dl:
		zad3_dl = obwod
		zad3_wsp = f"A({Xa};{Ya}), B({Xb};{Yb}), C({Xc};{Yc})"

	a = dlugosc_odcinka(Xa, Ya, Xb, Yb)
	b = dlugosc_odcinka(Xa, Ya, Xc, Yc)
	c = dlugosc_odcinka(Xb, Yb, Xc, Yc)
	if pitagoras(a, b, c):
		zad4 += 1
	Xs, Ys = srodek(Xa, Ya, Xc, Yc)
	Xd, Yd = punktD(Xb, Yb, Xs, Ys)
	if Xd == Yd:
		zad5.append(f'A({Xa};{Ya}), B({Xb};{Yb}), C({Xc};{Yc}), D({Xd};{Yd}),')

zad3_dl = round(zad3_dl,2)

with open('wyniki.txt','w') as w:
	w.write('1)\n' + str(zad1)
		+ '\n2)\n' + str(zad2)
		+ '\n3)\n' + str(zad3_dl) + '\n' + zad3_wsp)
	w.write('\n4)\n' + str(zad4)
		+ '\n5)\n')
	for wsp in zad5:
		w.write(str(wsp) + '\n')
