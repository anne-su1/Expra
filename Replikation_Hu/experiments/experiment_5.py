from task_model.task_grid import Task_grid
from psychopy import core, visual, event, gui

import pandas as pd

class E5:

    task: Task_grid
    experiment_duration: int
    win: visual.Window
    behav_data: pd.DataFrame
    sub_info: dict 
    sub_folder_path: str
    mean_rt : float
    color = "black"

    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window, behav_data: pd.DataFrame, sub_info: dict, sub_folder_path: str):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
        self.behav_data = behav_data
        self.sub_info = sub_info
        self.sub_folder_path = sub_folder_path 

    def getExperimentNumber(self) -> int:
        return 5

    def start(self):
        text = visual.TextStim(
            self.win,
            text="0:00",
            pos=(0, 0.85),
            height=0.07,
            color=self.color
        )

        text_stim_e5 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color)
        text_stim_e5.setText(
            '''Start Block 5
            \n\n Zum Starten bitte die Leertaste drücken.
        ''')
        text_stim_e5.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])

        trial_counter = 0
        timer = core.Clock()

        while timer.getTime() < self.experiment_duration:
            self.draw_fixation((0., 0.))

            trial_counter = trial_counter + 1
            self.task.generate_experiment_task()
            self.task.draw(self.win)

            countdown = core.CountdownTimer(self.mean_rt +1)
            elapsed = countdown.getTime()
            mins = int(elapsed // 60)
            secs = int(elapsed % 60)
            time_str = f"{mins:02d}:{secs:02d}"
            text.setText(time_str)
            text.draw()

            self.win.flip()
            countdown.reset()
           
            trial_start_time = timer.getTime()
            trial_reaction_time = float("NaN")
            while countdown.getTime() > 0:
                keys = event.getKeys(keyList='space')
                if keys:
                    trial_reaction_time = timer.getTime() - trial_start_time
                    break

                self.task.draw(self.win)

                elapsed = countdown.getTime()
                mins = int(elapsed // 60)
                secs = int(elapsed % 60)
                time_str = f"{mins:02d}:{secs:02d}"
                text.setText(time_str)
                text.draw()

                self.win.flip()

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
                "block": 5,
                "trial": trial_counter,
                "reaction_time": trial_reaction_time,
                "max_time": self.mean_rt,
                "E_amount_answer": E_amount_answer,
                "E_counter": self.task.E_counter,
                "is_corr": int(E_amount_answer == self.task.E_counter) if E_amount_answer is not None else 0,
                "answer_in_time": int(trial_reaction_time <= self.mean_rt)
            }
            
            self.behav_data.loc[len(self.behav_data)] = trial_data
            self.behav_data.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_behav_data_2.csv')

        text_stim_e5.setText(
                '''Sie haben Block 5 geschafft!''')
        text_stim_e5.draw()
        self.win.flip()
        core.wait(3)

        text_stim_e5.setText(
            '''Sie haben nun 2 min Pause.
            \n\n Wenn Sie früher bereit sind fortzufahren, drücken Sie die Leertaste.'''
        )
        text_stim_e5.draw()
        self.win.flip()
        event.waitKeys(maxWait = 120, keyList = ['space'])

    def practice(self):
        print("practice e5")

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