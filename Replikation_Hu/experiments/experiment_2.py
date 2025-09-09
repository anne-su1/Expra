from task_model.task_grid import Task_grid
from psychopy import core, visual, event 

class E2:

    task: Task_grid
    experiment_duration: int
    timer: core.CountdownTimer
    win: visual.Window

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
    
    def start(self):
        print("E2 gestartet")

    def practice(self):
        timer = core.Clock()
        text = visual.TextStim(
            self.win,
            text="0:00",
            pos=(0, 0.9),
            height=0.05,
            color="white"
        )

        for i in range(3):
            self.task.generate_experiment_task()
            
            event.clearEvents()
            keys = None
            while timer.getTime() < 240:
                self.task.draw(self.win)

                elapsed = timer.getTime()
                mins = int(elapsed // 60)
                secs = int(elapsed % 60)
                time_str = f"{mins:02d}:{secs:02d}"

                text.setText(time_str)
                text.draw()

                self.win.flip()

                keys = event.getKeys()
                if keys:
                    break