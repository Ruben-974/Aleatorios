def fact(n):
    f = 1
    while n > 1:
        f = f*(n)
        n -= 1
    return f

p = 'nos'.upper()
letras = []
for l in p:
    cont = p.count(l)
    if cont > 1 and [l, cont] not in letras:
        letras.append([l, cont])
ang = fact(len(p))
for c in letras:
    ang //= fact(c[1])
print(ang)