import random
from sys import argv

def td_array(breite: int, hoehe: int):
    """
    Es wird ein zwei dimensionales Array zurückgegeben
    
    Returns: list
    """
    return [[None] * breite for index in range(hoehe)]


def vertikaler_auszug(spalte: int, zeilen_startpunkt: int, wort_laenge: int, array: list):
    """
    Diese Funktion gibt einen vertikalen Ausschnitt eines zwei dimensionalem Array wieder als Liste.
    Es wird eine Start Koordinate gegeben (Xn|Yn), dann wird über die y-Kooridinate iteriert (Xn, Yn+wort_laenge)

    Args:
        spalte (int): [X-Koordinate eines zwei dimensionalem Array]
        zeilen_startpunkt (int): [Y-Koordinate eines zwei dimensionalem Array]
        wort_laenge (int): [die größe über diese dann iteriert wird]
        array (list): [das zwei dimensionale Array]
    
    Returns: [list]
    """
    return [array[zeilen_startpunkt + index][spalte] for index in range(wort_laenge)]


def horizontaler_auszug(zeile: int, spalten_startpunkt: int, wort_laenge: int, array: list):  
    """
    Diese Funktion ähnelt der Funktion: vertikaler_auszug, nur das hier über die x-Koordinate iteriert wird.
    Returns: [list]
    """
    return [array[zeile][spalten_startpunkt + index] for index in range(wort_laenge)]


def woerter_einsetzen(richtung: str, wort: str, array: list):
    """
    Diese Funktion setzt die Woerter in das zwei dimensinales array ein. Es werden zwei zufällige Koordinaten bestimmt (x,y).
    Ist die Richtung vertikal, bekommt die x-Koordinate einen Offset und wenn die Richtung horizontal ist bekommt y einen Offset 
    von der laenge des Wortes, damit das Wort nicht abgeschnitten wird und keine (out of index Error) auslöst.
    
    Args:
        richtung (str): [sagt, ob das Wort vertikal oder horizontal eingesetzt wird]
        wort (str): [Das Wort was eingesetzt wird]
        array (list): [Das zwei dimensionale Array, in welches das Wort eingesetz wird]
        
    Returns: [list]
    """
    
    versuche = 100

    hoehe = len(array)
    breite = len(array[0])

    if richtung == "vertikal":

        for y in range(versuche):

            zufaellige_spalte = random.choice(range(breite))
            zufaellige_reihe = random.choice(range(hoehe - len(wort) + 1))

            if all(ele is None for ele in vertikaler_auszug(zufaellige_spalte, zufaellige_reihe, len(wort), array)):

                for index, element in enumerate(wort):
                    array[zufaellige_reihe + index][zufaellige_spalte] = wort[index]
                break

            if y == versuche - 1:
                woerter_die_nicht_reinpassen.append(wort)

    elif richtung == "horizontal":

        for z in range(versuche):

            zufaellige_spalte = random.choice(range(breite - len(wort) + 1))
            zufaellige_reihe = random.choice(range(hoehe))

            if all(ele is None for ele in horizontaler_auszug(zufaellige_reihe, zufaellige_spalte, len(wort), array)):

                for index, element in enumerate(wort):
                    array[zufaellige_reihe][zufaellige_spalte + index] = wort[index]
                break

            if z == versuche - 1:
                woerter_die_nicht_reinpassen.append(wort)


if __name__ == "__main__":

    with open(argv[1], "r") as file:

        """
        In diesem Abschnitt, werden die einzelnen Informationen aus der test.txt Datein extrahiert
        """
        
        f = file.read().splitlines()
        goeße = f[0].split(" ")
        woerter = f[2:len(f)]
        main_grid = td_array(int(goeße[0]), int(goeße[1]))
        

    woerter_die_nicht_reinpassen = []
    """
    in "woerter_die_nicht_reinpassen", werden alle wörter reingeschrieben die Nach n-Versucehn keinen Platz gefunden haben
    """

    richtung = ["vertikal" for x in argv if x == "--v"] + ["horizontal" for x in argv if x == "--h"]
    
    def einsetzen():
        if "--v" or "--h" in richtung:
            for wort in woerter:
                woerter_einsetzen(random.choice(richtung), wort, main_grid)       
    einsetzen()    
    
    
    """
    Falls Wörter nicht in das Array gepasst haben, wird dieser Vorgang wiederholt.
    Falls es zu viele Wörter für das Array gibt, so dass es überhaupt nicht möglich ist alle rein zu bekommen, 
    hört der Algorithmus nach 10 Versuchen auf und gibt sie dann in Zeile 137 in der Konsole aus. 
    Diese könne aber in der Zeile 121 angepasst werden.
    """
    for x in range(10):
        if woerter_die_nicht_reinpassen != []:
            woerter_die_nicht_reinpassen = []
            main_grid = td_array(int(goeße[0]), int(goeße[1]))
            einsetzen()
        else:
            break
    
    """
    Es werden alle None Objekte durch wählbare Symbole ersetzt und in der Konsole ausgegeben.
    """
    for array in main_grid:
            print(*[i if i != None else random.choice(list(argv[2])) for i in array])
    
    if woerter_die_nicht_reinpassen != []:
        print(woerter_die_nicht_reinpassen)