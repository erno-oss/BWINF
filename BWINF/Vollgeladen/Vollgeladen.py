from sys import argv

Startpunkt = 0
Max_Fahrdauer = 360 #min
Max_Fahrtage = 5
Zielentfernung = 1200

with open(argv[1], "r") as h:
    """
    Extrahiert die Daten aus der Test-Datei.
    """
    raw_Hotels = h.read().splitlines()
    Hotels = [[int(x.split(" ")[0]), float(x.split(" ")[1])] for x in raw_Hotels[2:len(raw_Hotels)]]

def hotel_score(Entfernung: int, Max_Fahrdauer: int, Bewertung: float):
    """
    Berechnet einen Score für das Hotel, es werden da bei Distanz und Bewertung berücksichtig.

    Args:
        Entfernung (int): [Die Entfernung des Hotels zu dem aktuellen Standort des Autos.]
        Max_Fahrdauer (int): [Die Anzahl von Autominuten, die am Tag zurückgelegt werden können.]
        Bewertung (float): [Die Bewertung des Hotels.]

    Returns:
        [float]: [Es wird ein float zwichen 0-1 zurückgegeben, der für den Score des Hotels steht.]
    """
    return round((Entfernung*((1*Bewertung)/(Startpunkt+Max_Fahrdauer))/5), 3)

    
def verfügbare_hotels(Startpunkt: int, Max_Fahrdauer: int):
    """
    Die Funktion, schaut welche Hotels unter betrachtung der maximalen Fahrzeit zu verfügung stehen.

    Returns:
        [list]: [Die liste von Hotels die zur verfügung stehen.]
    """
    return [[ent, bew, hotel_score(ent, Max_Fahrdauer, bew)] for ent, bew in Hotels if ent < Startpunkt + Max_Fahrdauer and ent > Startpunkt]


def hotel_auswahl(method: str):
    global Startpunkt
    """
    Es wird eine Hotel nach den gegeben Kriterien ausgewählt, entweder nach der Distanz, der Bewertung oder dem Score.

    Args:
        method (str): [nach welchen Kriterien ausgewählt werden soll.]

    Raises:
        Exception: [Falls keine Methode angegeben wurde.]
    """
    
    print(f"Startpunkt: {Startpunkt}\nMaximale Fahrdauer am Tag: {Max_Fahrdauer}\nMaximale anzahl an Reisetagen {Max_Fahrtage}\n")
    
    durchschnitts_Bewertung = []
    
    """
    Ein Hotel ist immer so aufgebaut. [Entfernug, Bewertung, Score]
    """
    
    for index in range(Max_Fahrtage):
        if Startpunkt + Max_Fahrdauer < int(raw_Hotels[1]):
            zuauswahlstehende_hotels = verfügbare_hotels(Startpunkt, Max_Fahrdauer)
            if method == "--r":
                ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[0]))
            elif method == "--b":
                ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[1]))
            elif method == "--s":
                ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[2]))
            else:
                raise Exception("Keien Reiseart angegeben!")
            Startpunkt = zuauswahlstehende_hotels[ausgewähltes_hotel][0]
            durchschnitts_Bewertung.append(zuauswahlstehende_hotels[ausgewähltes_hotel][1])
            print(f"Stop {index+1} nach {Startpunkt} Minuten: Hotel{zuauswahlstehende_hotels[ausgewähltes_hotel]}")
    print(f"\nEntfernung des Reise Zeils: {raw_Hotels[1]}")

hotel_auswahl(argv[2])
