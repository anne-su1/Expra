from task_model.task_grid import Task_grid
from psychopy import core, visual, event 

class E3:

    task: Task_grid
    experiment_duration: int
    timer: core.CountdownTimer
    win: visual.Window

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
    
    def start(self):
        print("E3 gestartet")
    
    def practice(self):
        for i in range(3):
            self.task.generate_experiment_task()
            self.task.draw(self.win)
            keys = event.waitKeys(maxWait = 10)