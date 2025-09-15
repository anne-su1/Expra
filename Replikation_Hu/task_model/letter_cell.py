# Klasse für eine Buchstaben-Zelle im Task Grid
class letter_cell:
    letter: str
    rotation_angle: int
    isMirrored: bool

    # Erzeugen einer Zelle mit Buchstabe, Winkel und Spiegelung damit in jeder Buchstaben-Zelle diese drei Werte gebündelt sind
    # Wichtig weil wir so nur ein grid in task_grid benötigen
    def __init__(self, letter:str = "", angle:int = 0, isMirrored:bool = False):
            self.letter = letter
            self.rotation_angle = angle
            self.isMirrored = isMirrored
                   