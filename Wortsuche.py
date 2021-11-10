import random


def td_array(breite, hoehe):
    return [[None] * breite for i in range(hoehe)]


def vertikaler_auszug(spalte, zeilen_startpunkt, wort_laenge, array):

    return [array[zeilen_startpunkt + i][spalte] for i in range(wort_laenge)]


def horizontaler_auszug(zeile, spalten_startpunkt, wort_laenge, array):

    return [array[zeile][spalten_startpunkt + i] for i in range(wort_laenge)]

def woerter_einsetzen(richtung, wort, breite, hoehe, array):

    versuche = 100

    if richtung == "vertikal":

        for y in range(versuche):

            zufaellige_spalte = random.choice(range(breite))
            zufaellige_reihe = random.choice(range(hoehe - len(wort) + 1))

            if all(ele is None for ele in vertikaler_auszug(zufaellige_spalte, zufaellige_reihe, len(wort), array)):

                for i, element in enumerate(wort):
                    array[zufaellige_reihe + i][zufaellige_spalte] = wort[i]
                break

        if y == versuche:
            print("keien Möglichkeit gefunden")

    elif richtung == "horizontal":

        for z in range(versuche):

            zufaellige_spalte = random.choice(range(breite - len(wort) + 1))
            zufaellige_reihe = random.choice(range(hoehe))

            if all(ele is None for ele in horizontaler_auszug(zufaellige_reihe, zufaellige_spalte, len(wort), array)):

                for i, element in enumerate(wort):
                    array[zufaellige_reihe][zufaellige_spalte + i] = wort[i]
                break

        if z == versuche:
            print("keine Möglichkeit gefunden")

    else:
        print("richtung muss: vertikal oder horizontal sein.")


main_grid = td_array(11, 11)


words = ["Apfel", "Banane", "Baum", "Menschen", "Essen", "Schüler", "Hosen", "Pandas", "Pflanzen", "Hüte", "Blumen"]

for word in words:
    woerter_einsetzen("vertikal", word, 11, 11, main_grid)

for u in main_grid:
    print(*u)
