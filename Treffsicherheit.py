Ada = [0, 0, 0, 0, 0, 0, 0]
Nancy = [1, 0, 0, 1, 1, 0, 0]
Niklaus = [2, 2, 2, 1, 2, 2, 2]
Grace = [2, 1, 2, 2, 1, 0, 0]
Edsger = [0, 1, 2, 2, 1, 0, 0]
Rosza = [1, 2, 1, 2, 0, 1, 1]

Freunde = [Ada, Nancy, Niklaus, Grace, Edsger, Rosza]

anzahl = lambda x, y: x.count(y)


a = []
for Freund in Freunde:
    for index, element in enumerate(Freund):
        if element == 0:
            a.append(index)


z = dict(zip([0, 1, 2, 3, 4, 5, 6], [anzahl(a, x) for x in [0, 1, 2, 3, 4, 5, 6]]))
# print(z)


print(max(z, key=lambda x: z[x]))

for index, element in enumerate(Freunde):
    print(element)
    if element[max(z, key=lambda x: z[index])] != 0:
        print(element)
        for index1, element1 in enumerate(element):
            # print(index1)
            if element1 == 0 or element1 == 1:
                print(element1)
