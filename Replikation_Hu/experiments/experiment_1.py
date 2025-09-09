from task_model.task_grid import Task_grid
from psychopy import core, visual, event 

class E1:

    task: Task_grid
    experiment_duration: int
    timer: core.CountdownTimer
    win: visual.Window

    # Dataframe vom sub

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win

    def start(self):
        print("E1 gestartet")


        #self.timer = core.CountdownTimer(self.experiment_duration)
        #while self.timer.getTime() > 0:
            #self.task.generate_experiment_task()
        # starten, displays generieren, input/ reaction time sub speichern, neues display bis 4min um, dann aktuelles display beenden, 
         # textfeld anzeigen Ende Block 1
    
    def practice(self):
        for i in range(3):
            self.task.generate_experiment_task()
            self.task.draw(self.win)
            self.win.flip()
            keys = event.waitKeys()
