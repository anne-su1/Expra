from task_model.task_grid import Task_grid
from psychopy import core, visual, event, gui
import pandas as pd

class E2:

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
        self.behav_data: pd.DataFrame
        self.sub_info: dict 
        self.sub_folder_path: str
       
    
    def start(self):
        text = visual.TextStim(
            self.win,
            text="0:00",
            pos=(0, 0.9),
            height=0.05,
            color="white"
        )

        text_stim_e2 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color)
        text_stim_e2.setText(
            '''Start Block 2
            \n\n Zum Starten bitte die Leertaste drücken.
        ''')
        text_stim_e2.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])

        trial_counter = 0
        timer = core.Clock()

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

        while timer.getTime() < self.experiment_duration / 10:       # /10 weg  
            self.draw_fixation((0., 0.))
            trial_counter = trial_counter + 1
            self.task.generate_experiment_task()

            self.task.draw(self.win)
            self.win.flip()
           
            trial_start_time = timer.getTime()
        
            while timer.getTime() < 240:
                keys = event.getKeys(keyList='space')
                if keys:
                    trial_reaction_time = timer.getTime() - trial_start_time
                    self.win.flip()
                    break


            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()

            trial_data = {
                **self.sub_info,
                "block": 2,
                "trial": trial_counter,
                "reaction_time": trial_reaction_time,
                "E_amount_answer": int(trial_answer.data[0]),
                "E_counter": self.task.E_counter,
                "is_corr": int(int(trial_answer.data[0]) == self.task.E_counter)
            }
            
            self.behav_data = pd.concat([self.behav_data, pd.DataFrame([trial_data])], ignore_index=True)
            self.behav_data.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_behav_data.csv')

        text_stim_e2.setText(
                '''Sie haben Block 2 geschafft!''')
        text_stim_e2.draw()
        self.win.flip()
        core.wait(5)



    def practice(self):
        timer = core.Clock()

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