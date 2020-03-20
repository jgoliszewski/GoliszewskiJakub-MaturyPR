dane = []
with open('hasla.txt','r') as file:
    for password in file:
        dane.append(password.strip())
