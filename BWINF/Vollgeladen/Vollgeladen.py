
Startpunkt = 0
Max_Fahrdauer = 360 #min
Max_Fahrtage = 5
Zielentfernung = 1200

with open("hotels5.txt", "r") as h:
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
    """
    Es wird eine Hotel nach den gegeben Kriterien ausgewählt, entweder nach der Distanz, der Bewertung oder dem Score.

    Args:
        method (str): [nach welchen Kriterien ausgewählt werden soll.]

    Raises:
        Exception: [Falls keine Methode angegeben wurde.]
    """
    
    print(f"Startpunkt: {Startpunkt}\nMaximale Fahrdauer am Tag: {Max_Fahrdauer}\nMaximale anzahl an Reisetagen {Max_Fahrtage}\n")
    global Startpunkt
    durchschnitts_Bewertung = []
    
    """
    Ein Hotel ist immer so aufgebaut. [Entfernug, Bewertung, Score]
    """
    
    for index in range(Max_Fahrtage):
        zuauswahlstehende_hotels = verfügbare_hotels(Startpunkt, Max_Fahrdauer)
        if method == "geringste Reisezeit":
            ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[0]))
        elif method == "beste Bewertet":
            ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[1]))
        elif method == "beste Bewertung bei geringer Reisezeit":
            ausgewähltes_hotel = zuauswahlstehende_hotels.index(max(zuauswahlstehende_hotels, key=lambda x: x[2]))
        else:
            raise Exception("Keien Reiseart angegeben!")
        Startpunkt = zuauswahlstehende_hotels[ausgewähltes_hotel][0]
        durchschnitts_Bewertung.append(zuauswahlstehende_hotels[ausgewähltes_hotel][1])
        print(f"Stop {index+1} nach {Startpunkt} Minuten: Hotel{zuauswahlstehende_hotels[ausgewähltes_hotel]}")

hotel_auswahl("geringste Reisezeit")
