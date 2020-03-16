n = 0
A = [] 
with open('dane1.txt', 'r') as dane:
	for line in dane:
		line = line.strip()
		if n != 0 and len(A) == 0:
			A = line.split(' ')

		if n == 0:
			n = line

A = [int(x) for x in A]	

p = 0
k = int(n)
while p < k:
	s = (p+k) // 2
	if A[s] % 2 != 0:
		p = s + 1 
	else:
		k = s

w = A[k]
with open('wynik1.txt', 'w') as wynik:
	wynik.write(f'Wynik zad1.1 - {w}')