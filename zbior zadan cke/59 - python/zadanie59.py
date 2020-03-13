liczby = []
with open('liczby.txt','r') as file:
	for line in file:
		line = line.strip()
		liczby.append(int(line))

def rozklad(n):
	czynniki = []
	k = 1
	
	while k < n ** (1/2):
		k += 1
		while n % k == 0:
			czynniki.append(k)
			n /= k
	if n != 1:
		czynniki.append(int(n))
	return czynniki
	
def rozklad2(n):
	ile = 0
	czynnik = 3
	if n % 2 == 0:
		return False
	while n > 1:
		if n % czynnik == 0:
			ile += 1
		while n % czynnik == 0:
			n /= czynnik
		czynnik += 2
		if ile > 3:
			return False
	if ile == 3:
		return True
	if ile > 3:
		return False

def moc(n):
	k = 1
	moc = 0
	while len(str(n)) > 1:
		for c in str(n):
			k *= int(c)
		n = k
		k = 1
		moc += 1
	return moc

x = 0
zad1 = 0
zad2 = 0
zad3 = []
for i in range(1,9):
	zad3.append([i, 0])
zad3_min = 1000000
zad3_max = 0

for l in liczby:
	r = set(rozklad(l))
	if len(r) == 3 and 2 not in r:
		zad1 += 1
	s = str(l + int(str(l)[::-1]))
	if s == s[::-1]:
		zad2 += 1
	m = moc(l)
	zad3[m-1][1] += 1
	if m == 1:
		if l > zad3_max:
			zad3_max = l
		if l < zad3_min:
			zad3_min = l

with open('wyniki_liczby.txt','w') as w:
	w.write('1)\n'
			+ str(zad1) + '\n'
			+'2)\n'
			+ str(zad2) + '\n'
			+'3)\n')
	for x in zad3:
		w.write(str(x) + '\n')
	w.write(str(zad3_min) + '\n'
			+ str(zad3_max))