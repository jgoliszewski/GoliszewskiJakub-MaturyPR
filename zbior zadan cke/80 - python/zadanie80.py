dane =  []
with open('dane_trojkaty.txt','r') as file:
	for line in file:
		dane.append(int(line.strip()))



#1
zad1 = []
def pitagoras(a,b,c):
	boki = [x*x  for x in [a, b, c]]
	if sum(boki) == 2 * max(boki):
		return True
	return False

for i in range(len(dane) - 2):
	if pitagoras(dane[i],dane[i+1],dane[i+2]):
		zad1.append([f"{dane[i]} {dane[i+1]} {dane[i+2]}"])

#2
def boki_trojkata(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return True
	return False

dane_malejaco = sorted(dane,reverse=True)
a = dane_malejaco[0]
b = dane_malejaco[1]
c = dane_malejaco[2]
i = 3
while not boki_trojkata(a, b, c):
	a = b
	b = c
	c = dane_malejaco[i]
	i += 1
zad2 = sum([a, b, c])
#3
zad3_trojkaty = []
d = len(dane)
for i in range(d):
	for j in range(i+1,d):
		for k in range(j+1,d):
			if boki_trojkata(dane[i], dane[j], dane[k]):
				zad3_trojkaty.append([i, j, k])
zad3 = len(zad3_trojkaty)

with open('wyniki.txt','w') as w:
	w.write('1)\n')
	for x in zad1:
		w.write(str(x) + '\n')
	w.write('1)\n' + str(zad2)
		+ '\n2)\n' + str(zad3))
