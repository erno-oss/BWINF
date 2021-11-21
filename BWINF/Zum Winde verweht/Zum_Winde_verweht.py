import math

with open("landkreis4.txt","r") as l:
    """
    Extrahiert die Infromationen aus der Test-Datei.
    """
    Landkreis = l.read().splitlines()
    n_m = Landkreis[0].split(" ")

    Koordinaten_Häuser = Landkreis[1:int(n_m[0])+1]
    Koordinaten_Windräder = Landkreis[int(n_m[0])+1:len(Landkreis)]
 
 
"""
Die Koordianten müssen von ["x y"] in [x, y] umgewandelt werden.
"""   
WindRäder = [(int(y.split(" ")[0]), int(y.split(" ")[1])) for y in Koordinaten_Windräder]
Häuser = [(int(y.split(" ")[0]), int(y.split(" ")[1])) for y in Koordinaten_Häuser]


"""
Für jedes Windrad wird die Distanz du jedem Haus gemessen und die geringeste Distanz / 10 ist die maximale Höhe des Windrades
"""
for index, Windrad in enumerate(WindRäder):
    print(f"Windrad:{index+1} ",(min([math.sqrt((Windrad[0]-Haus[0])**2+(Windrad[1]-Haus[1])**2) for Haus in Häuser]))/10)