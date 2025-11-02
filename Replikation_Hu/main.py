from psychopy import visual, core
import pyglet
import pandas as pd
from random import Random
import os

# Erstelle Klassen importieren
from task_model.task_grid import Task_grid  # Aufgabendisplay
from experiments.experiment_1 import E1     # Ablauf Experiment 1
from experiments.experiment_2 import E2     # Ablauf Experiment 2
from experiments.experiment_3 import E3     # Ablauf Experiment 3
from experiments.experiment_4 import E4     # Ablauf Experiment 4
from experiments.experiment_5 import E5     # Ablauf Experiment 5
from experiments.experiment_6 import E6     # Ablauf Experiment 6
from instruction import Instruction         # Displayfenster mit Instruktionen
from questionnaires import Questionnaire    # Dialogfenster für Fragebögen

# ------- Experiment---------------------------
def main():
    # Dataframe für Verhaltensdaten aus Phase 1
    behav_data_1 = pd.DataFrame({
        'sub_id' : [],                
        'age' : [],                
        'sex' : [],                 
        'normal / corrected sight' : [],
        'handedness' : [],
        'block' : [],
        'trial' : [],
        'reaction_time' : [],
        'E_amount_answer' : [],
        'E_counter' : [],
        'is_corr' : []
    })

    # Dataframe für Verhaltensdaten aus Phase 2
    # Basiert auf Dataframe Phase 1, enthält zusätzlich maximale mögliche Antwortszeit und ob diese eingehalten wurde
    behav_data_2 = pd.DataFrame({
        'sub_id' : [],               
        'age' : [],                 
        'sex' : [],                 
        'normal / corrected sight' : [],
        'handedness' : [],
        'block' : [],
        'trial' : [],
        'reaction_time' : [],
        'max_time' : [],
        'E_amount_answer' : [],
        'E_counter' : [],
        'is_corr' : [],
        'answer_in_time' : []
    })
    
    # Variable mit Klasse Questionnaire
    # Benutzt für alle Anfragen für Fragebögen
    questionnaire = Questionnaire()

    # Sub Datenabfrage und Sub-Ordner Erstellung
    sub_info = questionnaire.sub_input()

    if sub_info is None:
        core.quit() 

    sub_folder_path = os.getcwd() + f'/sub-{sub_info.get("sub_id")}'
    if not os.path.exists(sub_folder_path):         
        os.makedirs(sub_folder_path)                

    # Kreierter Pfad wird an Questionnaire Objekt weitergegeben
    questionnaire.sub_folder_path = sub_folder_path

    # ---- Begrüssung ------

    # Berechnung Fenstergröße angepasst an Bildschirmgröße
    display = pyglet.canvas.get_display()
    screen = display.get_default_screen()
    width, height = screen.width, screen.height
    win = visual.Window(         
        color='grey',                      
        size=[width, height],                  
        fullscr=False,
        useRetina=True) 
    
    # Variable mit Klasse Instruction mit berechnetem Fenster
    instruction = Instruction(win)

    # Instruktionen am Anfang 
    instruction.initalHellos()

    # ---- Vorbereitung ------
    # Randomisierung der Aufgaben
    random = Random()
    # Raster für Aufgaben erstellt
    taskGrid = Task_grid(8, 16, random)

    # Erstellung aller Experimente und Übergeben von Infos
    e1 = E1(taskGrid, 240, win, behav_data_1, sub_info, sub_folder_path)
    e2 = E2(taskGrid, 240, win, behav_data_1, sub_info, sub_folder_path)
    e3 = E3(taskGrid, 240, win, behav_data_1, sub_info, sub_folder_path)
    e4 = E4(taskGrid, 240, win, behav_data_2, sub_info, sub_folder_path)
    e5 = E5(taskGrid, 240, win, behav_data_2, sub_info, sub_folder_path)
    e6 = E6(taskGrid, 240, win, behav_data_2, sub_info, sub_folder_path)

    # Dict welches der Gruppennr. 1-3 eine Sequenz der Experimente in den Phasen 1 und 2 zuordnet (Übernahme Hu et.al.)
    sequence_groups = { 
        1: [[e1, e2, e3], [e6, e4, e5]],
        2: [[e2, e3, e1], [e5, e6, e4]],
        3: [[e3, e1, e2], [e4, e5, e6]]
    }

    # Zuordnung einer Gruppe basierend auf sub_id mit Sicherstellung ähnlicher Gruppengröße
    sub_group = (int(sub_info.get("sub_id")) % 3) + 1
    phase_1_sequence =  sequence_groups[sub_group][0]
    phase_2_sequence = sequence_groups[sub_group][1]

    # ---- Phase 1 -----
    # Instruktionen für Phase 1
    instruction.instruction_for_phase_1()

    # einmalige Übungsaufgaben ohne Zeitangabe (3 Displays)
    e1.practice()

    # Experimente werden in vorher ausgewählter Reihenfolge (nach Gruppe) durchgeführt
    for experiment in phase_1_sequence:
        #experiment.practice()
        experiment.start()

    # ---- fatigue questionnare 1 ------
    # Window Flip damit leerer Hintergrund zu sehen ist während Questionnaire aufgerufen wird
    win.flip()
    questionnaire.fatigue_questionnaire_1()

    # ---- Phase 2 ------
    # Berechnen von individuellen Rektionszeiten für Phase 2
    reaction_time = pd.to_numeric(behav_data_1['reaction_time'], errors='coerce')
    mean_rt = reaction_time.mean()
    mean_rt_plus_sd = reaction_time.mean()+ reaction_time.std()
    mean_rt_minus_sd = reaction_time.mean()- reaction_time.std()

    # Zuweisung ausgerechneter max. Reaktionszeiten an Experimente
    e4.mean_rt_plus_sd = mean_rt_plus_sd 
    e5.mean_rt = mean_rt
    e6.mean_rt_minus_sd = mean_rt_minus_sd 
    
    # Instruktionen für Phase 2
    instruction.instruction_for_phase_2()
    
    # Experimente werden in vorher ausgewählter Reihenfolge (nach Gruppe) durchgeführt
    for experiment in phase_2_sequence:
        #experiment.practice()
        experiment.start()

    # ----- fatigue questionnare 2 ------
    # Window Flip damit leerer Hintergrund zu sehen ist während Questionnaire aufgerufen wird
    win.flip()
    questionnaire.fatigue_questionnaire_2()

    # ----- Verabschiedung -----
    instruction.say_goodbye()


# Python spezifische Kennzeichnung der Hauptdatei
if __name__ == "__main__":
    main()