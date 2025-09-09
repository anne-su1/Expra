from psychopy import visual, core
import pandas as pd
from random import Random

from task_model.task_grid import Task_grid
from experiment_1 import E1
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
        'key_pressed' : [],
        'E_counter' : [],
        'corr_key_pressed' : []
    })
    
    quest_data = pd.DataFrame({
        'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
        'Q1E1' : [],                 # [] leere Liste
        'Q1E2' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
        'Q1E3' : [],
        'Q1E4' : [],
        'Q1E5' : [],
        'Q1E6' : [],
        'Q2Phase1' : [],
        'Q2Phase2' : []
    })

    questionnaire = Questionnaire(quest_data)

    # Sub Datenabfrage
    sub_info = questionnaire.sub_input()

    if sub_info is None:
        core.quit() 
    
    print(sub_info)

    sub_folder_path = questionnaire.create_sub_data_folder(sub_info.get("sub_id"))
    print(sub_folder_path)

    win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
        color='grey',                       # Hintergrundfarbe (auch rgb mgl)
        size=[2000, 1000],                  # Anzahl Pixel (Größe Pixel)
        fullscr=True,
        useRetina=True) 
    
    instruction = Instruction(win)

    # Begrüssung
    instruction.initalHellos()

    # Phase 1

    random = Random(42)
    taskGrid = Task_grid(8, 16, random)
    e1 = E1(taskGrid, 240, win)

    e1.practice()

    # fatigue questionnare 1
    # Phase 2
    # fatigue questionnare 2
    # Danke


if __name__ == "__main__":
    main()