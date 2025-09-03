import os                                       # Dateien mit python anlegen etc
import glob                                     # systematisches Einlesen von Dateien auf Festplatte
import pandas as pd                             # besser als numpy für uns
from psychopy import core, visual, gui, event   # core: basisfkt (timing), visual: fenster/bilder anzeigen, intruktionen, event: mgl das VP alle mgl eingaben machen kann
import random                                   # ähnlich numpy.random.shuffle
import time                                     # kann, muss aber nicht verwendet werden


supervisor_input = gui.Dlg(title="Participant Data", pos=(0, 0))
supervisor_input.addField("sub_id")
supervisor_input.addField("age")
supervisor_input.addField("sex", choices=["male", "female"])
supervisor_input.addField("normal or corrected sight", choices=["yes", "no"])
supervisor_input.addField("handedness", choices=["right", "left"])
supervisor_input.show()

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
    size=[400, 400],                    # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 
