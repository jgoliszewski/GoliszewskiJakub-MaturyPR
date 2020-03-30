dane = []
with open('okregi.txt','r') as file:
	for line in file:
		line = line.strip().split()
		line = [float(x) for x in line]
		dane.append(line)

#1
zad1_I = 0
zad1_II = 0
zad1_III = 0
zad1_IV = 0
zad1_zadna = 0
def cwiartka(x, y, r):
	odp = ''
	if x > 0 and y > 0:
		odp = 'I'
	if x < 0 and y > 0:
		odp = 'II'
	if x < 0 and y < 0:
		odp = 'III'
	if x > 0 and y < 0:
		odp = 'IV'

	if odp:
		if abs(x) > r and abs(y) > r:
			return odp
	return 'zadna'

#2
zad2 = 0
def lustrzane(x1, y1, r1, x2, y2, r2):
	if r1 == r2:
		if x1 == x2 and y1 == -y2: 
			return True
		if x1 == -x2 and y1 == y2: 
			return True
	return False
#3	
zad3 = 0
def prostopadle(x1, y1, r1, x2, y2, r2):
	if r1 == r2:
		if [x1, y1] == [y2, -x2]\
		or [x1, y1] == [-y2, x2]:
			return True
	return False
#4
zad4_naj = 0
zad4 = []
def lancuch(x1, y1, r1, x2, y2, r2):
	odl = pow(pow(x2-x1,2)+pow(y2-y1,2),1/2)

	if r1 + r2 >= odl and odl > max(r1,r2) - min(r1,r2):
		return True
	return False


dl = 1
ostatni = True
for i, line in enumerate(dane):
	x ,y, r = line
#1
	cw = cwiartka(x, y, r)
	if cw == 'I':
		zad1_I += 1
	if cw == 'II':
		zad1_II += 1
	if cw == 'III':
		zad1_III += 1
	if cw == 'IV':
		zad1_IV += 1
	if cw == 'zadna':
		zad1_zadna += 1
#4	
	if i < 999:

		if lancuch(x, y, r, dane[i+1][0], dane[i+1][1], dane[i+1][2]):
			dl += 1
		else:
			if dl > zad4_naj:
				zad4_naj = dl
			zad4.append(dl)
			dl = 1
	if i == 1000 and ostatni:
		zad4.append(dl)
		ostatni = False
	for i in range(i+1,len(dane)):
#2
		if lustrzane(x, y, r, dane[i][0], dane[i][1], dane[i][2]):
			zad2 += 1
#3
		if prostopadle(x, y, r, dane[i][0], dane[i][1], dane[i][2]):
			zad3 += 1
with open('okregi_wyniki.txt','w') as w:
	w.write('1)\n' + 'I - ' + str(zad1_I) + '\n' 
		+ 'II - ' + str(zad1_II) + '\n'
		+ 'III - ' + str(zad1_III) + '\n' 
		+ 'IV - ' + str(zad1_IV) + '\n' 
		+ 'zadna - ' + str(zad1_zadna)
		+ '\n\n2)\n' + str(zad2)
		+ '\n\n3)\n' + str(zad3)
		+ '\n\n4)\n' + str(zad4_naj) + '\n' 
		+ str(zad4))