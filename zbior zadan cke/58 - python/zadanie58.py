systemy1 = []
systemy2 = []
systemy3 = []

with open('dane_systemy1.txt','r') as file1,\
	open('dane_systemy2.txt','r') as file2,\
	open('dane_systemy3.txt','r') as file3 :
	for line1 in file1:
		line1 = line1.strip()
		systemy1.append(line1)
	for line2 in file2:
		line2 = line2.strip()
		systemy2.append(line2)
	for line3 in file3:
		line3 = line3.strip()
		systemy3.append(line3)
#1
s1_min = 1000
s2_min = 1000
s3_min = 1000

for i in range(len(systemy1)):
	a, temp1 = systemy1[i].split(" ")
	b, temp2 = systemy2[i].split(" ")
	c, temp3 = systemy3[i].split(" ")
	temp1 = int(temp1)
	temp2 = int(temp2)
	temp3 = int(temp3)
	if temp1 < s1_min:
		s1_min = temp1
	if temp2 < s2_min:
		s2_min = temp2
	if temp3 < s3_min:
		s3_min = temp3

s2_min = '-' + bin(int(str(s2_min),4))[3:]
s3_min = '-' + bin(int(str(s3_min),8))[3:]

#2
zad2 = 0
pierwszy1 = int(systemy1[0].split(" ")[0],2)
pierwszy2 = int(systemy2[0].split(" ")[0],4)
pierwszy3 = int(systemy3[0].split(" ")[0],8)
for i in range(1, len(systemy1)):
	time1 = int(systemy1[i].split(" ")[0],2)
	time2 = int(systemy2[i].split(" ")[0],4)
	time3 = int(systemy3[i].split(" ")[0],8)
	if (time1 - pierwszy1) % 24 != 0 and\
		(time2 - pierwszy2) % 24 != 0 and\
		(time3 - pierwszy3) % 24 != 0:
		zad2 += 1

#3
zad3 = 0
max1 = -1000000
max2 = -1000000
max3 = -1000000
for i in range(len(systemy1)):
	x = 0
	temp1 = int(systemy1[i].split(" ")[1],2)
	temp2 = int(systemy2[i].split(" ")[1],4)
	temp3 = int(systemy3[i].split(" ")[1],8)
	if temp1 > max1:
		x = 1
		max1 = temp1
	if temp2 > max2:
		x = 1
		max2 = temp2
	if temp3 > max3:
		x = 1
		max3 = temp3
	zad3 += x

#4
zad4_naj = 0
for i in range(len(systemy1)):
	for j in range(len(systemy1)):
		if j != i:
			temp_i = int(systemy1[i].split(" ")[1],2)
			temp_j = int(systemy1[j].split(" ")[1],2)
			r = (temp_i - temp_j) ** 2
			d = abs(i - j)
			skok = r / d
			if skok > r // d:
				skok = r // d + 1
			if skok > zad4_naj:
				zad4_naj = skok

with open('wyniki_systemy.txt','w') as w:
	w.write('1)\n')
	w.write(str(s1_min) + "\n"
			+ str(s2_min) + "\n"
			+ str(s3_min) + "\n" 
			+ '2)\n'
			+ str(zad2) + "\n"
			+ '3)\n'
			+ str(zad3) + "\n"
			+ '4)\n' 
			+ str(zad4_naj) + "\n")