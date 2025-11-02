from psychopy import core, visual, event, gui
import pandas as pd
import numpy as np 

# erstellte Klasse importieren
from task_model.task_grid import Task_grid      # Aufgabendisplay

# Klasse für Experiment 2 erstellen
class E2:

    task: Task_grid
    experiment_duration: int
    win: visual.Window
    behav_data: pd.DataFrame
    sub_info: dict 
    sub_folder_path: str
    color = "black"

    # Konstruktor für neue Elemente in dieser Klasse
    def __init__(self, taskGrid: Task_grid, duration: int, win: visual.Window, behav_data: pd.DataFrame, sub_info: dict, sub_folder_path: str):
        self.task = taskGrid
        self.experiment_duration = duration
        self.win = win
        self.behav_data = behav_data
        self.sub_info = sub_info
        self.sub_folder_path = sub_folder_path

    # gibt die Experimentnummer zurück
    def getExperimentNumber(self) -> int:
        return 2
       
    # Methode für Experiment 2
    def start(self):
        # Darstellung des Timers festlegen
        text = visual.TextStim(
            self.win,
            text="0:00",
            pos=(0, 0.85),
            height=0.07,
            color=self.color
        )

        text_stim_e2 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color,
                                       wrapWidth= 1.8)
        text_stim_e2.setText(
            '''Start Block β
            \n\n Zum Starten bitte die Leertaste drücken.
        ''')
        text_stim_e2.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])

        # zählt die angefangenen Trials, beginnt bei 0
        trial_counter = 0
        # startet eine Uhr, die im Hintergrund läuft
        timer = core.Clock()

        # Schleife, die neue Trials startet solange die Experimentdauer noch nicht erreicht ist
        while timer.getTime() < self.experiment_duration:
            self.draw_fixation((0., 0.))
            trial_counter = trial_counter + 1
            self.task.generate_experiment_task()
            
            self.task.draw(self.win)

            # vergangene Zeit wird im Format einer Digitaluhr mit Minuten und Sekunden angezeigt
            elapsed = timer.getTime()
            mins = int(elapsed // 60)
            secs = int(elapsed % 60)
            time_str = f"{mins:02d}:{secs:02d}"
            text.setText(time_str)
            text.draw()
        
            self.win.flip()
           
            # Startzeit wird genommen, nachdem das Display erscheint
            trial_start_time = timer.getTime()
            trial_reaction_time = float("NaN")

            # Schleife wartet, bis Proband Leertaste drückt, um Eingabe zu tätigen
            event.clearEvents(eventType='keyboard')
            while timer.getTime() < self.experiment_duration:
                keys = event.getKeys(keyList='space')
                if keys:
                    trial_reaction_time = timer.getTime() - trial_start_time
                    break

                self.task.draw(self.win)

                # Timeranzeige aktualisiert sich sekündlich
                elapsed = timer.getTime()
                mins = int(elapsed // 60)
                secs = int(elapsed % 60)
                time_str = f"{mins:02d}:{secs:02d}"
                text.setText(time_str)
                text.draw()
        
                self.win.flip()

            self.win.flip()

            # Dialogfenster zum Antworten
            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()
            try:
                E_amount_answer = int(trial_answer.data[0])
            except (ValueError, TypeError):
                E_amount_answer = None

            # Daten aus dem Trial werden gespeichert
            trial_data = {
                **self.sub_info,
                "block": "clock timer",
                "trial": trial_counter,
                "reaction_time": "NA" if np.isnan(trial_reaction_time) else trial_reaction_time,
                "E_amount_answer": int(E_amount_answer) if E_amount_answer is not None else "NA",
                "E_counter": self.task.E_counter,
                "is_corr": int(E_amount_answer == self.task.E_counter) if E_amount_answer is not None else "NA"
            }
            
            # Daten aus dem Trial werden an Dataframe mit Daten aus Phase 1 angehängt und als .csv gespeichert
            self.behav_data.loc[len(self.behav_data)] = trial_data
            self.behav_data.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_behav_data_1.csv')

        # Ende von Experiment 2
        text_stim_e2.setText(
                '''Sie haben den Block β geschafft!''')
        text_stim_e2.draw()
        self.win.flip()
        core.wait(3)

        text_stim_e2.setText(
            '''Sie haben nun 2 min Pause.
            \n Bitte notieren Sie auf dem beiliegenden Zettel Ihren Erschöpfungsgrad für Block β!
            \n\n Wenn Sie früher bereit sind fortzufahren, drücken Sie die Leertaste.'''
        )
        text_stim_e2.draw()
        self.win.flip()
        event.waitKeys(maxWait = 120, keyList = ['space'])

    # Methode für Übungsdurchgänge (verworfen, nur noch 1x Übung ganz am Anfang)
    def practice(self):
        text_stim_e2 = visual.TextStim(self.win,
                                       height=0.085,
                                       color=self.color,
                                       wrapWidth= 1.8)
        text_stim_e2.setText(
            '''Sie beginnen nun mit 3 Übungsaufgaben für Block 2.
            \n Bitte zählen Sie die vorhandenen E's und drücken Sie danach auf die Leertaste.
            \n Es öffnet sich ein Fenster in dem Sie bitte die Anzahl der gezählten E's eintragen und mit "OK" bestätigen.
            \n\n Zum Starten der Übung bitte die Leertaste drücken.
            ''')
        text_stim_e2.draw()
        self.win.flip()
        event.waitKeys(keyList='space')

        # Schleife für 3 Übungsdurchgänge
        for i in range(3):
            self.draw_fixation((0.0, 0.0))
            self.task.generate_experiment_task()
            self.task.draw(self.win)
            self.win.flip()
            
            # wartet auf Eingabe des Probanden, blendet dann das Display aus
            while True:
                keys = event.getKeys(keyList='space')
                if keys:
                    self.win.flip()
                    break

            # Dialogfenster zum Antworten, kein Speichern der Übungsdurchgänge
            trial_answer = gui.Dlg(title = "Trial Answer")
            trial_answer.addField("Wie viele 'E's' waren auf dem Display zu sehen?")
            trial_answer.show()

    # Methode für Fixationskreuz
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