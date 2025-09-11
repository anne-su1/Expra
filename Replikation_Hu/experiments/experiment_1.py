from task_model.task_grid import Task_grid
from psychopy import core, visual, event, gui

import pandas as pd

class E1:

    task: Task_grid
    experiment_duration: int
    win: visual.Window
    behav_data: pd.DataFrame
    sub_info: dict 
    sub_folder_path: str
    color = "black"

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window, behav_data: pd.DataFrame, sub_info: dict, sub_folder_path: str):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
        self.behav_data = behav_data
        self.sub_info = sub_info
        self.sub_folder_path = sub_folder_path 

    def getExperimentNumber(self) -> int:
        return 1

    def start(self):
        text_stim_e1 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color,
                                       wrapWidth= 1.8)
        text_stim_e1.setText(
            '''Start Block 1
            \n\n Zum Starten bitte die Leertaste drücken.
        ''')
        text_stim_e1.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])

        trial_counter = 0
        timer = core.Clock()

        while timer.getTime() < self.experiment_duration:
            self.draw_fixation((0., 0.))
            trial_counter = trial_counter + 1
            self.task.generate_experiment_task()

            self.task.draw(self.win)
            self.win.flip()
           
            trial_start_time = timer.getTime()
            trial_reaction_time = float("NaN")
            while timer.getTime() < self.experiment_duration:
                keys = event.getKeys(keyList='space')
                if keys:
                    trial_reaction_time = timer.getTime() - trial_start_time
                    break

            self.win.flip()
            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()
            try:
                E_amount_answer = int(trial_answer.data[0])
            except (ValueError, TypeError):
                E_amount_answer = None

            trial_data = {
                **self.sub_info,
                "block": 1,
                "trial": trial_counter,
                "reaction_time": trial_reaction_time,
                "E_amount_answer": E_amount_answer,
                "E_counter": self.task.E_counter,
                "is_corr": int(E_amount_answer == self.task.E_counter) if E_amount_answer is not None else 0
            }
            
            self.behav_data.loc[len(self.behav_data)] = trial_data
            self.behav_data.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_behav_data_1.csv')

        text_stim_e1.setText(
                '''Sie haben Block 1 geschafft!''')
        text_stim_e1.draw()
        self.win.flip()
        core.wait(3)

        text_stim_e1.setText(
            '''Sie haben nun 2 min Pause.
            \n\n Wenn Sie früher bereit sind fortzufahren, drücken Sie die Leertaste.'''
        )
        text_stim_e1.draw()
        self.win.flip()
        event.waitKeys(maxWait = 120, keyList = ['space'])
        
    
    def practice(self):
        text_stim_e1 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color,
                                       wrapWidth= 1.8)
        text_stim_e1.setText(
            '''Sie beginnen nun mit 3 Übungsaufgaben für Block 1.
            \n Bitte zählen Sie die vorhandenen E's und drücken Sie danach auf die Leertaste.
            \n Es öffnet sich ein Fenster in dem Sie bitte die Anzahl der gezählten E's eintragen und mit "OK" bestätigen.
            \n\n Zum Starten der Übung bitte die Leertaste drücken.
            ''')
        text_stim_e1.draw()
        self.win.flip()
        event.waitKeys(keyList='space')

        for i in range(3):
            self.draw_fixation((0.0, 0.0))
            self.task.generate_experiment_task()
            self.task.draw(self.win)
            self.win.flip()
            
            while True:
                keys = event.getKeys(keyList='space')
                if keys:
                    self.win.flip()
                    break

            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()



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
        