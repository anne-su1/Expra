# ------- Betreutes Programmieren: Aufgabe 2 --------
# Erstellt eine Funktion die 4 zufällig positionierte rote Kreise und 1 zufällig positioniertes T präsentiert
# Positionen dürfen sich nicht überschneiden
# Das Suchdisplay soll so lange präsentiert werden bis A gedrückt wird
from psychopy import visual, event
import numpy as np

win = visual.Window(
    color = "grey",
    size = [700, 700],
    fullscr = False,
    useRetina = True,
)

x_min, x_max = -300, 300
y_min, y_max = -300, 300
radius = 10
minAbstand = radius * 2

def squaredDistanceBetweenPositions(pos1, pos2):                               # euklidische Abstand ohne Wurzel im zweidimensionalen 
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2                     # Hypothenuse zwischen zwei Punkten über (x1-  x2)^2 + (y1 - y2)^2 -> a^2 + b^2 = c^2 (=Abstand)

def isFreePosition(posToEvaluate, current_position, minAbstand):               # 
    for position in current_position:                                          # ist Position die wir haben schon "vergeben" an vorherigen Positionen?
        if squaredDistanceBetweenPositions(posToEvaluate, position) < minAbstand**2: # indem schauen ob Position die wir haben über Mindestabstand liegt
            return False                                                       # wenn Position kleiner minAbstand**2, dann ist Position schon vergeben, da Abstand zu gering, def ist vorbei
    return True                                                                # wenn Position größer, dann ist Position möglich

def positionFourCircles():
    Kreisliste = {}                                 # leere Kreisliste als dict (-> {})
    while len(Kreisliste) < 4:                      # solange keine 4 Elemente (0,1,2,3) in Kreisliste, wird Liste gefüllt mit Kreisen
        x = np.random.uniform(x_min, x_max)         # randomisierte Position, für jeden Kreis neu
        y = np.random.uniform(y_min, y_max)         # randomisierte Position, für jeden Kreis neu
        position = (x ,y)
        if not isFreePosition(position, Kreisliste.keys(), minAbstand):  # wenn Position nicht frei ist, wird erneuter Kreis ermittelt
            continue
        else:                                       # wenn Position frei, dann wird Kreis mit entsprechender Position gebaut und ins Dict eingefügt
            Kreis = visual.Circle(
                win,
                fillColor = "red",
                units = "pix",
                radius = radius,
                pos = position
            )
            Kreisliste[position] = Kreis            # einfügen Kreis ins dict (Kreisliste)
    return Kreisliste                               # wenn while schleife vorbei (4 Elemente im dict), dann wird Kreisliste zurückgegeben

def positionTStim(circlePositions):                 # Funktion heißt "positionTStim" und möchte als Parameter "circlePosition"
    while True:                                     # unendlichkeitsschleife, wird mit break abgebrochen, wenn Position für T gefunden wurde
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(y_min, y_max)
        position = (x, y)
        if not isFreePosition(position, circlePositions, minAbstand):   # ist Platz für das T unter den vorher gewählten 4 Kreisen?
            continue                                                    # wenn nicht, neu suchen
        else:                                                           # wenn ja, T wird mit gefundener Position gebaut
            stim_T = visual.TextStim(
                win,
                units = "pix",
                text = "T",
                color = "black",
                pos = position
            )
            break                                                      # T gefunden, Schleife wird abgebrochen
    return stim_T                                                      # T wird zurückgegeben

Kreisliste_final = positionFourCircles()                  # wir definieren die finale Kreisliste als Ergebnis der Funktion "positionFourCircles", hier wird Funktion erst aufgerufen und ausgeführt (def wird nicht ausgeführt, ist nicht sichtbar)
stim_T_final = positionTStim(Kreisliste_final.keys())     # wir definieren das finale T als Ergebnis der Funktion "positionTStim", und geben zusätzliche die Position der Kreise an (mit .keys), damit das T nicht unter einem Kreis liegt (Parameter circle Position ist in def gefordert, geben wir mit Kreisliste_final.keys)

for Kreis in Kreisliste_final.values():             # jedes Element in den values (Kreise) werden gemalt
    Kreis.draw()

stim_T_final.draw()                                 # das T wird gemalt

win.flip()                                          # window wird geflipt
event.waitKeys(maxWait=20.0, keyList=["a"])         # Schließbedingungen für Fenster