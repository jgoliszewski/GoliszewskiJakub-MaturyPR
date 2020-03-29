tekst = []
with open('tekst.txt','r') as file:
	for x in file:
		tekst = x.split(" ")

#1
zad1 = 0
def para_liter(s):
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return True
	return False
#2
liter = 0
litery = []
for i in range(26):
	litery.append(0)
zad2 = []
#3		
zad3_naj = 0
zad3_licz = 0
zad3_pier = ''
def ciag_spolglosek(s):
	k = ''
	for z in s:
		if z in ['A','E','I','O','U','Y']:
			k += ' '
		else:
			k += z
	a = [len(x) for x in k.split(' ')]
	return max(a)

for slowo in tekst:
	if para_liter(slowo):
		zad1 += 1
	zad3_d = ciag_spolglosek(slowo)
	if zad3_d > zad3_naj:
		zad3_naj = zad3_d
	for litera in slowo:
		liter += 1
		if ord(litera) != 10:		
			litery[ord(litera)-65] += 1

for slowo in tekst:
	zad3_d = ciag_spolglosek(slowo)
	if zad3_d == zad3_naj:
		zad3_licz += 1

		if zad3_pier == '':
			zad3_pier = slowo

for i, x in enumerate(litery):
	litera = chr(i+65)
	ile = litery[i]
	proc = str(round(ile/liter*100,2)) + '%'
	zad2.append([litera,ile,proc])

with open('wyniki.txt','w') as w:
	w.write('1)\n' + str(zad1)
		+ '\n2)\n')
	for x in zad2:
		w.write(str(x) + '\n')
	w.write('3)\n' + str(zad3_naj) + '\n'
	 + str(zad3_licz) + '\n'
	 + str(zad3_pier) + '\n')

