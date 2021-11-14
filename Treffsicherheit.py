Ada = [0, 0, 0, 0, 0, 0, 0]
Nancy = [1, 0, 0, 1, 1, 0, 0]
Niklaus = [2, 2, 2, 1, 2, 2, 2]
Grace = [2, 1, 2, 2, 1, 0, 0]
Edsger = [0, 1, 2, 2, 1, 0, 0]
Rosza = [1, 2, 1, 2, 0, 1, 1]

Freunde = [Ada, Nancy, Niklaus, Grace, Edsger, Rosza]

a = []
for Freund in Freunde:
    for index, element in enumerate(Freund):
        if element == 0:
            a.append(index)
a.sort()
print(a)


anzahl = lambda x, y: x.count(y)
