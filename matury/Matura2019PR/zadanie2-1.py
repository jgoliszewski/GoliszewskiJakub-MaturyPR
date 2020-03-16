s = ''
n = 0
k = 0
lines = []
with open('dane2.txt', 'r') as dane:
	for line in dane:
		line = line.strip()
		lines.append(line)

s += lines[0]
n = int(lines[1])
k = int(lines[2])

kolejnosc = []
l = 1
def pisz(a, b, c):
	global l
	if len(a) == b:
		print(a)
	else:
		for i in range(c):
			kolejnosc.append(f"{l} - pisz({a + str(i)}, {b}, {c})")
			pisz(a + str(i), b, c)
			l += 1
pisz(s, n, k)

with open('wynik2.txt', 'w') as wynik:
	for line in kolejnosc:
		wynik.write(str(line) + '\n')