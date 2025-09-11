from psychopy import visual, core, monitors
import pyglet
import pandas as pd
from random import Random
import os

from task_model.task_grid import Task_grid
from experiments.experiment_1 import E1
from experiments.experiment_2 import E2
from experiments.experiment_3 import E3
from experiments.experiment_4 import E4
from experiments.experiment_5 import E5
from experiments.experiment_6 import E6


from instruction import Instruction
from questionnaires import Questionnaire

def main():
    behav_data_1 = pd.DataFrame({
        'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
        'age' : [],                 # [] leere Liste
        'sex' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
        'normal or corrected sight' : [],
        'handedness' : [],
        'block' : [],
        'trial' : [],
        'reaction_time' : [],
        'E_amount_answer' : [],
        'E_counter' : [],
        'is_corr' : []
    })

    behav_data_2 = pd.DataFrame({
        'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
        'age' : [],                 # [] leere Liste
        'sex' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
        'normal or corrected sight' : [],
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
    
    questionnaire = Questionnaire()

    # Sub Datenabfrage und sub-Ordner Erstellung
    sub_info = questionnaire.sub_input()

    if sub_info is None:
        core.quit() 

    sub_folder_path = os.getcwd() + f'/sub-{sub_info.get("sub_id")}'
    if not os.path.exists(sub_folder_path):         # wenn Pfad nicht existiert, mache diesen ordner (makedirs)
        os.makedirs(sub_folder_path)                # if Statement nötig, wenn pfad nicht existiert, um nicht weiter um nicht zu überschreiben

    questionnaire.sub_folder_path = sub_folder_path

    # Begrüssung
    display = pyglet.canvas.get_display()
    screen = display.get_default_screen()
    width, height = screen.width, screen.height
    win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
        color='grey',                       # Hintergrundfarbe (auch rgb mgl)
        size=[width, height],                  # Anzahl Pixel (Größe Pixel)
        fullscr=False,
        useRetina=True) 
    instruction = Instruction(win)

    instruction.initalHellos()


    # Vorbereitung
    random = Random()
    taskGrid = Task_grid(8, 16, random)

    e1 = E1(taskGrid, 10, win, behav_data_1, sub_info, sub_folder_path)
    e2 = E2(taskGrid, 10, win, behav_data_1, sub_info, sub_folder_path)
    e3 = E3(taskGrid, 10, win, behav_data_1, sub_info, sub_folder_path)
    e4 = E4(taskGrid, 10, win, behav_data_2, sub_info, sub_folder_path)
    e5 = E5(taskGrid, 10, win, behav_data_2, sub_info, sub_folder_path)
    e6 = E6(taskGrid, 10, win, behav_data_2, sub_info, sub_folder_path)

    sequence_groups = { # in der Liste ist die erste Liste die Reihnfolge für Phase 1, die zweite für Phase 2 dann
        1: [[e1, e2, e3], [e6, e4, e5]],
        2: [[e2, e3, e1], [e5, e6, e4]],
        3: [[e3, e1, e2], [e4, e5, e6]]
    }

    sub_group = (int(sub_info.get("sub_id")) % 3) + 1
    phase_1_sequence =  sequence_groups[sub_group][0]
    phase_2_sequence = sequence_groups[sub_group][1]

    questionnaire.sequence_for_phase_1, questionnaire.sequence_for_phase_2 = phase_1_sequence, phase_2_sequence
    
    # Phase 1
    instruction.instruction_for_phase_1()

    for experiment in phase_1_sequence:
        #experiment.practice()
        experiment.start()

    # ...

    # fatigue questionnare 1
    win.flip()
    questionnaire.fatigue_questionnaire_1()

    # Phase 2
    # Berechnen von individuellen Rektionszeiten für Phase 2
    mean_rt = behav_data_1['reaction_time'].mean()
    mean_rt_plus_sd = behav_data_1['reaction_time'].mean()+ behav_data_1['reaction_time'].std()
    mean_rt_minus_sd = behav_data_1['reaction_time'].mean()- behav_data_1['reaction_time'].std()

    e4.mean_rt_plus_sd = mean_rt_plus_sd 
    e5.mean_rt = mean_rt
    e6.mean_rt_minus_sd = mean_rt_minus_sd 

    instruction.instruction_for_phase_2()

    for experiment in phase_2_sequence:
        experiment.practice()
        experiment.start()

    # ...

    # fatigue questionnare 2
    win.flip()
    questionnaire.fatigue_questionnaire_2()

    # Danke

    instruction.say_goodbye()


if __name__ == "__main__":
    main()