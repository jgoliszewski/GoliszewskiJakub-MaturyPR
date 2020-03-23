dane = []

with open('dane_napisy.txt','r') as file:
	for line in file:
		dane.append(line.strip().split())

def anagram(a,b):
	a = list(a)
	b = list(b)
	for l in a:
		if l in b:
			b.remove(l)
		else:
			return False
	if len(b) == 0:
		return True
	return False

#1
zad1_licznik = 0
#2
zad2_licznik = 0

for line in dane:
	a, b = line
	zad1 = True
	for z in a:
		if z != a[0]:
			zad1 = False
	if not a == b:
		zad1 = False
	if zad1:
		zad1_licznik += 1

	if anagram(a,b):
		zad2_licznik += 1


#3
dane2 = []
k_max = 0
for x in dane:
	a,b = x
	dane2.append(a)
	dane2.append(b)
for i in range(len(dane2)):
	k = 1
	for j in range(len(dane2)):
		if i != j:
			if anagram(dane2[i],dane2[j]):
				k += 1
	if k > k_max:
		k_max = k





with open('wyniki_anagramy.txt','w') as w:
	w.write('1)\n' + str(zad1_licznik)
			+'\n2)\n' + str(zad2_licznik)
			+'\n3)\n' + str(k_max))