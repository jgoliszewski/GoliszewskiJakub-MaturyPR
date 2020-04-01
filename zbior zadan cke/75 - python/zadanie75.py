dane_tekst = []
with open('tekst.txt','r') as file:
	for line in file:
		for slowo in line.strip().split():
			dane_tekst.append(slowo)

dane_probka = []
with open('probka.txt','r') as file:
	for line in file:
		dane_probka.append(line.strip().split())

def szyfr(slowo, A, B):
	zaszyfrowane = ''
	for l in slowo:
		c = ord(l) - 97
		x = c * A + B
		x %= 26
		sz = chr(x + 97)
		zaszyfrowane += sz
	return zaszyfrowane

#1
zad1 = ''
 
 #2
zad2 = ''

for slowo in dane_tekst:
	if slowo[0] == 'd' and slowo[-1] == 'd':
		zad1 += slowo + '\n'
	if len(slowo) >= 10:
		zaszyfrowane = szyfr(slowo, 5, 2)
		zad2 += f'{zaszyfrowane}\n'

#3
zad3 = ''
for para in dane_probka:
	slowo, zaszyfrowane = para
	for A in range(26):
		for B in range(26):
			if szyfr(slowo, A, B) == zaszyfrowane:
				zad3 += f'{para} - szyfr - {A, B}\n'
				print(f'{para} - szyfr - {A, B}\n')
			if szyfr(zaszyfrowane, A, B) == slowo:
				zad3 += f'{para} - deszyfr - {A, B}\n'
				print(f'{para} - deszyfr - {A, B}\n')
print(zad3)

with open('wyniki.txt','w') as w:
	w.write(f"1)\n{zad1}\n\n2)\n{zad2}\n\n3)\n{zad3}")