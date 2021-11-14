Ada = [0, 0, 0, 0, 0, 0, 0]
Nancy = [1, 0, 0, 1, 1, 0, 0]
Niklaus = [2, 2, 2, 1, 2, 2, 2]
Grace = [2, 1, 2, 2, 1, 0, 0]
Edsger = [0, 1, 2, 2, 1, 0, 0]
Rosza = [1, 2, 1, 2, 0, 1, 1]

Freunde = [Ada, Nancy, Niklaus, Grace, Edsger, Rosza]

anzahl = lambda x, y: x.count(y)


#a = [anzahl(x, 0) for x in Freunde]
for y in Freunde:
    b = [(index, element) for index, element in enumerate(y)]
    print(b)

a = []
for Freund in Freunde:
    for index, element in enumerate(Freund):
        if element == 0:
            a.append(index)
#print(a)

z = dict(zip([0, 1, 2, 3, 4, 5, 6], [anzahl(a, x) for x in [0, 1, 2, 3, 4, 5, 6]]))
#print(z)
