dane = []
with open('napisy.txt','r') as file:
	for line in file:
		dane.append(line.strip().split(' '))
#1
zad1 = 0
zad1_p = []

#2
zad2 = []

#3
zad3 = []
zad3_max = 0
for x in dane:
	a, b = x
	if len(b) > len(a):
		a, b = b, a
	if len(a) >= len(b) * 3:
		zad1 += 1
		if len(zad1_p) == 0:
			zad1_p.append(x)
	if a.find(b) == 0:
		zad2.append([x,a[len(b):]])

	dl_zakonczenia = 0
	for i in range(1,len(b)):
		if a[-i] == b[-i]:
			dl_zakonczenia += 1
		elif dl_zakonczenia > zad3_max:
			zad3_max = dl_zakonczenia


for x in dane:
	a, b = x
	if len(b) > len(a):
		a, b = b, a
	if len(a) >= len(b) * 3:
		zad1 += 1
	dl_zakonczenia = 0
	for i in range(1,len(b)):
		if a[-i] == b[-i]:
			dl_zakonczenia += 1
	if dl_zakonczenia == 16:
		zad3.append(x)
