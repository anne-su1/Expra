class letter_cell:
    value: str
    rotation_angle: int
    isMirrored: bool

    def __init__(self, value:str = "", angle:int = 0, isMirrored:bool = False):
            self.value = value
            self.rotation_angle = angle
            self.isMirrored = isMirrored

    def __str__(self) -> str:
        return f"{self.value}({self.rotation_angle}-{self.isMirrored})"

        