from task_model.task_grid import Task_grid
from psychopy import core, visual, event, gui

import pandas as pd

class E1:

    task: Task_grid
    experiment_duration: int
    timer: core.CountdownTimer
    win: visual.Window
    data: pd.DataFrame

    # Dataframe vom sub

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window, data: pd.DataFrame):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
        self.data = data

    def start(self):
        #print("E1 gestartet")
        text_stim_e1 = visual.textStim(win,
                                       height=0.085)
        text_stim_e1.setText('''Start Block 1
                             \\n Zum Starten bitte die Leertaste drücken''')
        text_stim_e1.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])

        timer = core.Clock()

        while timer < 240:
            self.draw_fixation(self.win, (0., 0.))

            trial_start_time = timer.getTime()

            self.task.generate_experiment_task()
            if event.getKeys == 'space':
                self.win.flip()

            trial_reaction_time = timer.getTime() - trial_start_time

            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()

            self.data['reaction_time'].append(trial_reaction_time)
            self.data['E_amount_answer'].append(trial_answer)

           
        # starten, displays generieren, input/ reaction time sub speichern, neues display bis 4min um, dann aktuelles display beenden, 
        # textfeld anzeigen Ende Block 1
    
    def practice(self):
        for i in range(3):
            self.draw_fixation((0.0, 0.0))
            self.task.generate_experiment_task()
            self.task.draw(self.win)
            self.win.flip()
            keys = event.waitKeys()

    def draw_fixation(self, fixation_position):
        fixation = visual.ShapeStim(self.win,
                                    pos = fixation_position,
                                    vertices = ((0, -0.025),(0, 0.025),(0, 0),(-0.015, 0),(0.015, 0)),
                                    lineWidth = 5,
                                    closeShape = False,
                                    lineColor = 'black')
        fixation.draw()
        self.win.update()
        core.wait(1)
        