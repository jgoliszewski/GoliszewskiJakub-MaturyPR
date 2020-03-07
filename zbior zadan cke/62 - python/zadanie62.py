l1 = []
l2 = []

with open("liczby1.txt","r") as liczby1:
	for line in liczby1:
		line = line.strip()
		line = int(line)
		l1.append(line)
with open("liczby2.txt","r") as liczby2:
	for line in liczby2:
		line = line.strip()
		line = int(line)
		l2.append(line)

zad1_max = 0
zad1_min = 1_000_000
for l in l1:
	if l > zad1_max:
		zad1_max = l
	if l < zad1_min:
		zad1_min = l
zad2_pierwszy_naj = 0
zad2_najdluzszy = 0
zad2_pierwszy = l2[0]
zad2_dlugosc = 0
for i in range(1,len(l2)):
	if int(l2[i]) >= int(l2[i-1]):
		zad2_dlugosc += 1
		
	else:
		if zad2_dlugosc > zad2_najdluzszy:
			zad2_najdluzszy = zad2_dlugosc + 1
			zad2_pierwszy_naj = zad2_pierwszy
		zad2_pierwszy = l2[i]
		zad2_dlugosc = 0	
zad3a = 0
zad3b = 0
zad4a = 0
zad4b = 0
for i in range(len(l1)):
	if int(str(l1[i]),8) == int(l2[i]):
		zad3a += 1
	if int(str(l1[i]),8) > int(l2[i]):
		zad3b += 1
	for z in str(l2[i]):
		if z == '6':
			zad4a += 1
	for z in str(oct(l2[i])):
		if z == '6':
			zad4b += 1

print(zad1_max)
print(zad1_min)
print(zad3a)
print(zad3b)
print(zad4a)
print(zad4b)
print(zad2_pierwszy_naj)
print(zad2_najdluzszy)