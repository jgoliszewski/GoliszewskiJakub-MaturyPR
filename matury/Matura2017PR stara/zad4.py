dane = []
with open('Dane_PR2/binarne.txt','r') as file:
	for line in file:
		dane.append(line.strip())

#1
zad1 = 0
zad1_maks = '0'
#2
zad2 = 0
zad2_najk = 100
def niepoprawny(a):
	for i in range(int(len(a)/4)):
		l = a[i*4 : i*4 + 4]
		if int(l,2) > 9:
			return True
	return False
#3
zad3 = 0
for x in dane:
	d = len(x)
	p = int(d/2)
	if x[0:p] == x[p:]:
		zad1 += 1
		if d > len(zad1_maks):
			zad1_maks = x
	if niepoprawny(x):
		zad2 += 1
		if d < zad2_najk:
			zad2_najk = d
	if int(x) > zad3:
		if int(x,2) < 65535:
			zad3 = int(x)

zad1_dl = len(zad1_maks)


with open('zadanie4.txt','w') as w:
	w.write('1)\n' + str(zad1) + '\n' + str(zad1_maks) + '\n' + str(zad1_dl) 
			+ '\n2)\n' + str(zad2) + '\n' + str(zad2_najk)
			+ '\n3)\n' + str(zad3))