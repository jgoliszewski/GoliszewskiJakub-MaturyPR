dane = []
with open('hasla.txt','r') as file:
    for password in file:
        dane.append(password.strip())
#1
zad1 = 0
#2
powtorzone = []
#3
zad3 = 0
def rosnace4(haslo):
	ascii = [ord(x) for x in list(haslo)]
	for i in range(len(haslo)-3):
		frag = sorted(ascii[i:i+4])
		if frag[0] + 1 == frag[1] and\
			frag[1] + 1 == frag[2] and\
			frag[2] + 1 == frag[3]:
			return True 
	return False

#4
zad4 = 0
def dobre_haslo(haslo):
	cyfra = False
	mala_l = False
	duza_l = False
	for z in haslo:
		try:
			int(z)
			cyfra = True
		except:
			if z == z.lower():
				mala_l = True
			else:
				duza_l = True
	if cyfra and mala_l and duza_l:
		return True
	return False

for i, haslo in enumerate(dane):
	try:
		int(haslo)
		zad1 += 1
	except:
		pass
	if rosnace4(haslo):
		zad3 += 1
	if dobre_haslo(haslo):
		zad4 += 1
	for j in range(i,len(dane)):
		if i != j:
			if dane[i] == dane[j]:
				powtorzone.append(haslo)
powtorzone = sorted(powtorzone)

with open('wyniki_hasla.txt','w') as w:
	w.write('1)\n' + str(zad1)
		+ '\n2)\n')
	for h in powtorzone:
		w.write(h + '\n')
	w.write('3)\n' + str(zad3)
		+ '\n4)\n' + str(zad4))