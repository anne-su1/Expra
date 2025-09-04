import os                                       # Dateien mit python anlegen etc
import glob                                     # systematisches Einlesen von Dateien auf Festplatte
import pandas as pd                             # besser als numpy für uns
from psychopy import core, visual, gui, event   # core: basisfkt (timing), visual: fenster/bilder anzeigen, intruktionen, event: mgl das VP alle mgl eingaben machen kann
import random                                   # ähnlich numpy.random.shuffle
import time                                     # kann, muss aber nicht verwendet werden

from task_model.task_grid import task_grid

supervisor_input = gui.Dlg(title="Participant Data", pos=(0, 0))
supervisor_input.addField("sub_id")
supervisor_input.addField("age")
supervisor_input.addField("sex", choices=["male", "female"])
supervisor_input.addField("normal or corrected sight", choices=["yes", "no"])
supervisor_input.addField("handedness", choices=["right", "left"])
supervisor_input.show()

sub_data = supervisor_input.data
sub_id = sub_data[0]

# create a folder and a dataframe to store the output
output_path = os.getcwd() + f'/sub-{sub_id}'
if not os.path.exists(output_path):         # wenn Pfad nicht existiert, mache diesen ordner (makedirs)
    os.makedirs(output_path)                # zweites if Statement nötig, wenn pfad nicht existiert, um nicht weiter um nicht zu überschreiben
    
behav_data = pd.DataFrame({'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
                            'age' : [],                 # [] leere Liste
                            'sex' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
                            'normal or corrected sight' : [],
                            'handedness' : [],
                            'block' : [],
                            'trial' : [],
                            'reaction_time' : [],
                            'key_pressed' : []
                            })

quest_data = pd.DataFrame({'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
                            'Q1E1' : [],                 # [] leere Liste
                            'Q1E2' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
                            'Q1E3' : [],
                            'Q1E4' : [],
                            'Q1E5' : [],
                            'Q1E6' : [],
                            'Q2Phase1' : [],
                            'Q2Phase2' : []
                            })
        
file_path = output_path + f'/sub-{sub_id}_task-catshumans.tsv' # TO DO: change task_catsHuman to real name

# window specific to our hardware
win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
    color='black',                      # Hintergrundfarbe (auch rgb mgl)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# start introduction
text_stim_1 = visual.TextStim(win,
                              height=0.085)                              # text stimuli_grid win aus Zeile 15
text_stim_1.setText('''Willkommen zu unserem Experiment! 
                    \n\n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
                    \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
                    \n In jedem Durchgang verändert sich die Anzahl der "E's".
                    \n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(keyList=['space'])     

#second part introduction
text_stim_2 = visual.TextStim(win,
                              height=0.085)                              # text stimuli_grid win aus Zeile 15
text_stim_2.setText('''Willkommen zu unserem Experiment! 
                    \n\n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
                    \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
                    \n In jedem Durchgang verändert sich die Anzahl der "E's".
                    \n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(keyList=['space']) 

# Grid Test
grid_rows = 8
grid_cols = 16
cell_width = 0.12
cell_height = 0.12

tg = task_grid(grid_rows, grid_cols)
rnd = random.Random(42)
tg.generate_experiment_task(rnd)
#print(tg.display())

grid_width = grid_cols * cell_width
grid_height = grid_rows * cell_height

stimuli_grid = []

for row in range(grid_rows):
    for col in range(grid_cols):
        letter_data = tg.grid[row][col]

        x = (col + 0.5) * cell_width - grid_width/2
        y = grid_height/2 - (row + 0.5) * cell_height

        stim = visual.TextStim(
            win,
            text = letter_data.value,
            height = 0.1,
            pos = (x, y),
            ori = letter_data.rotation_angle,
            color = "white",
            flipHoriz = letter_data.isMirrored
        )
        stimuli_grid.append(stim)

for stim in stimuli_grid:
    stim.draw()

win.flip()
event.waitKeys(keyList=["space"])

