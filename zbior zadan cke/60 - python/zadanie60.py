liczby = []
with open('liczby.txt','r') as file:
	for line in file:
		liczby.append(int(line.strip()))

#1
zad1 = 0
ostatnia = 0
przedostatnia = 0

#2
def dzielniki(n):
	lista = [1,n]
	for i in range(2,n//2 + 1):
		if n % i == 0:
			lista.append(i)
	lista.sort()
	return lista

zad2 = []

#3
def wzg_pierwsze(a, b):
	x = True
	wieksza = max(a,b)
	if a % b == 0 or b % a == 0:
		x = False

	for i in range(2,int(pow(wieksza, (1/2))) + 1):
		if a % i == 0 and b % i == 0:
			x = False
	return x

zad3 = 0
for l in liczby:
	if l < 1000:
		zad1 += 1
		przedostatnia = ostatnia
		ostatnia = l
	d = dzielniki(l)
	if len(d) == 18:
		zad2.append([l,d])
	wzg_p = True
	for k in liczby:
		if k != l:
			if not wzg_pierwsze(l, k):
				wzg_p = False
	if wzg_p and l > zad3:
		zad3 = l



with open('wyniki.txt','w') as w:
	w.write('1)'
			+ str(zad1) + '\n'
			+ str(przedostatnia) + ' ' + str(ostatnia) + '\n'
			+ '2)')
	for x in zad2:
		w.write(str(x)+'\n')
	w.write('3)\n' + str(zad3))