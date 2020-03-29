dane = []
with open('napisy.txt','r') as file:
	for line in file:
		dane.append(line.strip().split(' '))
#1
zad1 = 0
zad1_p = []

#2
zad2 = []

#3
zad3 = []
zad3_max = 0
def koncowka(a,b):
	d = 0
	for i in range(1,len(min(a,b))+1):
		if a[-i] == b[-i]:
			d += 1
		else:
			return d
	return d

for x in dane:
	a, b = x
	if len(b) > len(a):
		a, b = b, a
	if len(a) >= len(b) * 3:
		zad1 += 1
		if len(zad1_p) == 0:
			zad1_p.append(x)
	if a.find(b) == 0:
		zad2.append([x,a[len(b):]])

	d = koncowka(a, b)
	if d > zad3_max:
		zad3_max = d

for x in dane:
	a, b = x
	dl_zakonczenia = koncowka(a,b)
	if dl_zakonczenia == 15:
		zad3.append(x)

with open('wyniki.txt','w') as w:
	w.write('1)\n' + str(zad1) + '\n' + str(zad1_p)
		+ '\n2)\n')
	for x in zad2:
		w.write(str(x) + '\n')
	w.write('zad3\n')
	for x in zad3:
		w.write(str(x) + '\n')
