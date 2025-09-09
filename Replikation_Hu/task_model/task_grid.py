from random import Random
from psychopy import visual
from task_model.letter_cell import letter_cell

# Bauplan für ein Grid ohne E´s und F´s (class)
class Task_grid:

    max_E_count = 13

    rows : int
    columns : int
    grid : list[list[letter_cell]]
    E_counter : int
    random_seed: Random

    def __init__(self, rows, cols, random_seed):
        self.rows = rows
        self.columns = cols
        self.grid = [[letter_cell() for _ in range(cols)] for _ in range(rows)]
        self.E_counter = 0
        self.random_seed = random_seed

    # Generierung eines Displays mit E´s und F´s und zählt E´s
    def generate_experiment_task(self):
        angles = [0, 90, 180, 270]
        max_E_for_task = self.random_seed.randint(0, self.max_E_count)
        self.E_counter = 0

        positions = [(r, c) for r in range(self.rows) for c in range(self.columns)]
        self.random_seed.shuffle(positions)

        E_positions = []
        for r, c in positions:
            if len(E_positions) >= max_E_for_task:
                break
            if self.is_E_valid(r, c, E_positions):
                E_positions.append((r, c))
        self.E_counter = len(E_positions)

        for r in range(self.rows):
            for c in range(self.columns):
                letter = "E" if (r, c) in E_positions else "F"
                angle = self.random_seed.choice(angles)
                isMirrored = self.random_seed.choices([True, False], weights=[50, 50])[0]
                self.grid[r][c] = letter_cell(letter, angle, isMirrored)

    # Überprüfung keine benachbarten E´s
    def is_E_valid(self, current_row, current_col, E_positions) -> bool:
        neighbors = [
            (current_row - 1, current_col),
            (current_row + 1, current_col),
            (current_row, current_col - 1),
            (current_row, current_col + 1)
        ]

        for r, c in neighbors:
            if (r, c) in E_positions:
                return False

        return True

    def draw(self, win: visual.Window):
        cell_width = 0.12
        cell_height = 0.12

        grid_width = self.columns * cell_width
        grid_height = self.rows * cell_height

        stimuli_grid = []

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
                    color = "white",
                    flipHoriz = letter_data.isMirrored
                )
                stimuli_grid.append(stim)

        for stim in stimuli_grid:
            stim.draw()

        win.flip()

    # Umwandlung Grid in String für Ausgabe  
    def display(self) -> str:
        lines = []
        for row in self.grid:
            lines.append(" ".join(str(c) for c in row))
        return "\n".join(lines)
