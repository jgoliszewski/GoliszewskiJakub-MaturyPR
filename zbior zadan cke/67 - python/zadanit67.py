def czy_pierwsza(n):
	if n == 1:
		return False
	if n == 2 or n == 3:
		return True
	for i in range(2,int(pow(n,1/2)) + 1):
		if n % i == 0:
			return False
	return True

pierwsze40 = [1,1]
pierwsze40_bin = []
for i in range(38):
	x = pierwsze40[-1] + pierwsze40[-2]
	pierwsze40.append(x)
#1
f10 = pierwsze40[9]
f20 = pierwsze40[19]
f30 = pierwsze40[29]
f40 = pierwsze40[39]
 
#2
zad2 = []
for x in pierwsze40:
	if czy_pierwsza(x):
		zad2.append(x)
#3
	pierwsze40_bin.append(bin(x)[2:])
#4	
zad4 = []
for x in pierwsze40_bin:
	if str(x).count('1') == 6:
		zad4.append(x)
with open('wyniki.txt','w') as w:
	w.write('1)\n' + str(f10) + '\n'
					+str(f20) + '\n'
					+str(f30) + '\n'
					+str(f40) + '\n'
					+ '2)\n')
	for x in zad2:
		w.write(str(x) + '\n')
	w.write('3)\n')
	for x in pierwsze40_bin:
		w.write(str(x) + '\n')
	w.write('4)\n')
	for x in zad4:
		w.write(str(x) + '\n')