from random import Random
from task_model.letter_cell import letter_cell

class task_grid:

    max_E_count = 13

    rows : int
    columns : int
    grid : list[list[letter_cell]]
    E_counter : int

    def __init__(self, rows, cols):
        self.rows = rows
        self.columns = cols
        self.grid = [[letter_cell() for _ in range(cols)] for _ in range(rows)]
        self.E_counter = 0

    def generate_experiment_task(self, random_seed : Random):
        angles = [0, 90, 180, 270]
        max_E_for_task = random_seed.randint(0, self.max_E_count)
        self.E_counter = 0

        positions = [(r, c) for r in range(self.rows) for c in range(self.columns)]
        random_seed.shuffle(positions)

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
                angle = random_seed.choice(angles)
                isMirrored = random_seed.choices([True, False], weights=[10, 90])[0]
                self.grid[r][c] = letter_cell(letter, angle, isMirrored)

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

    
    def display(self) -> str:
        lines = []
        for row in self.grid:
            lines.append(" ".join(str(c) for c in row))
        return "\n".join(lines)
