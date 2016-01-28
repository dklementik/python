arabe = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1]
romain = ["M","CM", "D", "CD", "C","XC", "L", "XL","X","V","IV","I"]
nb = 3999
for i in arabe:
    if nb >= i:
        ent = nb / i
        print (romain[arabe.index(i)] * ent),
        nb = nb % i
