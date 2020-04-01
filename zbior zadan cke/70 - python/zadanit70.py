y1 = 19 + 61/125
y2 = -32 - 2/3
x1 = 2
def f(x):
	y = pow(x,4)/500 - pow(x,2)/200 - 3/250
	return y

def g(x):
	y = (-1) * pow(x, 3)/30 + x/20 + 1/6
	return y
#1
def calka(x1,x2):
	d = 1/1000
	i = x1
	suma = 0
	while i < x2:
		p1 = abs(d * f(i))
		p2 = abs(d * f(i+d))

		p3 = abs(d * g(i))
		p4 = abs(d * g(i+d))
		
		P = (p1 + p2 + p3 + p4) / 2 
		suma += P
		i += d

	return round(suma, 3) 

zad1 = str(calka(2,10))

#2
def dl_krzywych(x1,x2):
	d = 1/1000
	i = x1
	suma = 0
	while i < x2:
		a = pow(pow(abs(f(i) - f(i+d)),2) + pow(d, 2),1/2)
		suma += a
		b = pow(pow(abs(g(i) - g(i+d)),2) + pow(d, 2),1/2)
		suma += b
		i += d

	return suma
obwod = y1 - y2 + 16 + dl_krzywych(2, 10) 
zad2 = str(int(obwod) + 1)

#3
def pasy(x1,x2, grubosc):
	suma_dl = 0
	x = x2 - grubosc
	while x >= x1:
		h = f(x) - g(x)
		suma_dl += int(h)
		x -= grubosc
	return suma_dl
zad3 = str(pasy(2,10,1/4))

with open('zadanie_zaslona.txt','w') as w:
	w.write(f'1)\n{zad1}\n\n2)\n{zad2}\n\n3)\n{zad3}')