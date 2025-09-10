from psychopy import visual, core, monitors
import pyglet
import pandas as pd
from random import Random
import os

from task_model.task_grid import Task_grid
from experiments.experiment_1 import E1
from experiments.experiment_2 import E2
from experiments.experiment_3 import E3


from instruction import Instruction
from questionnaires import Questionnaire

def main():
    behav_data = pd.DataFrame({
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
    
    quest_data = pd.DataFrame({ 
        'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
        'Q1E1' : [],                 # [] leere Liste
        'Q1E2' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
        'Q1E3' : [],
        'Q2Phase1' : [],
        'Q1E4' : [],
        'Q1E5' : [],
        'Q1E6' : [],
        'Q2Phase2' : [],
    })

    questionnaire = Questionnaire(quest_data)

    # Sub Datenabfrage und sub-Ordner Erstellung
    sub_info = questionnaire.sub_input()

    if sub_info is None:
        core.quit() 

    sub_folder_path = os.getcwd() + f'/sub-{sub_info.get("sub_id")}'
    if not os.path.exists(sub_folder_path):         # wenn Pfad nicht existiert, mache diesen ordner (makedirs)
        os.makedirs(sub_folder_path)                # if Statement nötig, wenn pfad nicht existiert, um nicht weiter um nicht zu überschreiben

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

    # Phase 1
    instruction.instruction_for_phase_1()

    random = Random()
    taskGrid = Task_grid(8, 16, random)

    e1 = E1(taskGrid, 240, win, behav_data, sub_info, sub_folder_path)
    e2 = E2(taskGrid, 240, win)
    e3 = E3(taskGrid, 240, win, behav_data, sub_info, sub_folder_path)

    phase_1_sequence = [e3] #[e1, e2, e3] 
   # random.shuffle(phase_1_sequence)

    for experiment in phase_1_sequence:
        experiment.practice()
        experiment.start()

    # ...

    # fatigue questionnare 1

    questionnaire.fatigue_questionnaire_1()

    # Phase 2

    instruction.instruction_for_phase_2()

    # ...

    # fatigue questionnare 2

    questionnaire.fatigue_questionnaire_2()

    # Danke

    instruction.say_goodbye()


if __name__ == "__main__":
    main()