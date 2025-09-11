class letter_cell:
    letter: str
    rotation_angle: int
    isMirrored: bool

    def __init__(self, letter:str = "", angle:int = 0, isMirrored:bool = False):
            self.letter = letter
            self.rotation_angle = angle
            self.isMirrored = isMirrored
                   