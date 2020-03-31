dane = []
with open('funkcja.txt','r') as file:
	for line in file:
		dane.append([float(x) for x in line.strip().split()])

def f(x):
	wsp = []
	if x >=0 and x < 1:
		wsp = dane[0]
	if x >=1 and x < 2:
		wsp = dane[1]
	if x >=2 and x < 3:
		wsp = dane[2]
	if x >=3 and x < 4:
		wsp = dane[3]
	if x >=4 and x <= 5:
		wsp = dane[4]
	a0 = wsp[0]
	a1 = wsp[1]
	a2 = wsp[2]
	a3 = wsp[3]

	y = a0 + a1 * x + a2 * pow(x,2) + a3 * pow(x,3)
	return y

#1
zad1 = round(f(1.5),5)

#2
x = 0
zad2_y = 0 
zad2_x = 0

while x < 5:
	y = f(x)
	if y > zad2_y:
		zad2_y = y
		zad2_x = x
	x += 0.001

zad2_y = round(zad2_y,5)
zad2_x = round(zad2_x,3)

#3
def mz(l, p, blad=0.00001):
	if f(l) * f(p) > 0:
		return False

	while abs(l-p) > blad:
		s = (l + p) / 2

		y = f(s)
		if f(l) * y < 0:
			p = s
		else:
			l = s

	return round((l + p) / 2, 5) 
zad3 = ''
for i in range(5):
	m = mz(i,i+1)
	if m:
		zad3 += str(m) + '\n'

with open('wyniki_funkcja.txt','w') as w:
	w.write(f"1)\n{zad1}\
			\n\n2)\nx= {zad2_x}\ny= {zad2_y}\
			\n\n3)\n{zad3}")