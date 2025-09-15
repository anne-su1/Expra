from random import Random
from psychopy import visual
from task_model.letter_cell import letter_cell

# Klasse für ein Grid für die Suchdisplays
class Task_grid:

    max_E_count = 13

    rows : int
    columns : int
    grid : list[list[letter_cell]]
    E_counter : int
    random_seed: Random

    # Erstellen des Grid ohne E's und F's
    def __init__(self, rows, cols, random_seed):
        self.rows = rows
        self.columns = cols
        self.grid = [[letter_cell() for _ in range(cols)] for _ in range(rows)]
        self.E_counter = 0
        self.random_seed = random_seed

    # Generierung eines Displays mit E´s und F´s und zählt E´s
    def generate_experiment_task(self):
        angles = [0, 90, 180, 270]
        max_E_for_task = self.random_seed.randint(0, self.max_E_count) # randomisierter Integer zwischen 0 und 13
        self.E_counter = 0

        # Alle Positionen für E's und F's im Grid werden erzeugt und gemischt
        positions = [(row, col) for row in range(self.rows) for col in range(self.columns)]
        self.random_seed.shuffle(positions)

        # Rausnehmen der Positionen von "positions" an denen ein E stehen soll, bis max ANzahl an E's für Aufgabe erreicht ist
        E_positions = []
        for row, col in positions:
            if len(E_positions) >= max_E_for_task:
                break
            if self.is_E_valid(row, col, E_positions):
                E_positions.append((row, col))
        self.E_counter = len(E_positions)

        # Grid wird befüllt mit E's und F's, Buchstaben werden noch gedreht, gespiegelt
        for row in range(self.rows):
            for col in range(self.columns):
                letter = "E" if (row, col) in E_positions else "F"
                angle = self.random_seed.choice(angles)
                isMirrored = self.random_seed.choices([True, False], weights=[50, 50])[0]
                self.grid[row][col] = letter_cell(letter, angle, isMirrored)

    # Überprüfung keine benachbarten E´s
    def is_E_valid(self, current_row, current_col, E_positions) -> bool:
        neighbors = [
            (current_row - 1, current_col),
            (current_row + 1, current_col),
            (current_row, current_col - 1),
            (current_row, current_col + 1)
        ]

        for row, col in neighbors:
            if (row, col) in E_positions:
                return False

        return True

    # Grid wird auf Window "gemalt"
    def draw(self, win: visual.Window):
        cell_width = 0.12
        cell_height = 0.12

        grid_width = self.columns * cell_width
        grid_height = self.rows * cell_height

        stimuli_grid = []

        # Jede Zelle in Grid wird in Textstim umgewandelt
        for row in range(self.rows):
            for col in range(self.columns):
                letter_data = self.grid[row][col]

                x = (col + 0.5) * cell_width - grid_width/2
                y = grid_height/2 - (row + 0.5) * cell_height

                stim = visual.TextStim(
                    win,
                    text = letter_data.letter,
                    height = 0.1,
                    pos = (x, y),
                    ori = letter_data.rotation_angle,
                    color = "black",
                    flipHoriz = letter_data.isMirrored
                )
                stimuli_grid.append(stim)

        for stim in stimuli_grid:
            stim.draw()
