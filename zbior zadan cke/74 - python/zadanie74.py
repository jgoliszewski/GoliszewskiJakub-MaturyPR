licznik1 = 0
hasla = []
hasla_powtorzenia = []
licznik3 = 0
liczby = ['1','2','3','4','5','6','7','8','9']
with open('hasla.txt','r') as file:
    for password in file:
        password = password.strip()
        #1
        literkowe = 0
        for z in password:
            if not(z in liczby):
                literkowe = 1
        if literkowe == 0:
            licznik1 += 1
        #2
        if password in hasla:
            hasla_powtorzenia.append(password)
        hasla.append(password)
        #3
        schodki = 0
        for i in range(len(password)-1):
            if schodki != 4:
                if abs(ord(password[i])- ord(password[i+1])) == 1:
                    schodki += 1
                else:
                    schodki = 0
        if schodki == 4:
            licznik3 += 1
        #4


print(licznik1)
print(licznik3)
print(hasla_powtorzenia)
hasla_powtorzenia.sort()

with open('wyniki_hasla.txt','w') as wyniki:
    wyniki.write('74.1\n')
    wyniki.write('74.2\n')
    for x in hasla_powtorzenia:
        wyniki.write(str(x) + '\n')
    wyniki.write('74.3\n')
