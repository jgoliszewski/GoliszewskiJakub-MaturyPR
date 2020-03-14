ciagi = []
with open('ciagi.txt','r') as file:
	k = 1
	for line in file:
		if k % 2 == 0:
			ciagi.append(line.strip())
		k += 1
bledne = []
with open('bledne.txt','r') as file:
	k = 1
	for line in file:
		if k % 2 == 0:
			bledne.append(line.strip())
		k += 1

#1
zad1 = 0
zad1_naj = 0

#2
szesciany = [x**3 for x in range(101)]

def szescian(list):
	x = 0
	for l in list:
		if l in szesciany:
			if l > x:
				x = l
	if x != 0:
		return x

zad2 = []


for c in ciagi:
	aryt = True
	ciag = c.split(" ")
	ciag = [int(x) for x in ciag]
	s = szescian(ciag)
	if s != None:
		zad2.append(s)
	
	r = ciag[1] - ciag[0]
	for i in range(0,len(ciag) - 1):
		if ciag[i] + r != ciag[i + 1]:
			aryt = False
	if aryt:
		zad1 += 1
		if r > zad1_naj:
			zad1_naj = r	

#3
def bledny_wyraz(ciag):
	r = 0

	l = len(ciag)
	if ciag[1] - ciag[0] == ciag[2] - ciag[1]:
		r = ciag[1] - ciag[0]
	if r == 0:
		r = ciag[l-1] - ciag[l-2]

	for i in range(1,l - 2):
		if (ciag[i] - r != ciag[i-1]) and (ciag[i] + r != ciag[i+1]):
			return ciag[i]

	if ciag[0] + r != ciag[1]:
		return ciag[0]
	if ciag[l-1] - r != ciag[l-2]:
		return ciag[l-1]

zad3 = []
for c in bledne:
	ciag = c.split(" ")
	ciag = [int(x) for x in ciag]
	zad3.append(bledny_wyraz(ciag))

with open('wynik1.txt','w') as w:
	w.write(str(zad1)+ '\n' + str(zad1_naj))
with open('wynik2.txt','w') as w:
	for x in zad2:
		w.write(str(x) + '\n')
with open('wynik3.txt','w') as w:
	for x in zad3:
		w.write(str(x) + '\n')

	