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
    size=[2000, 1000],                    # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# start introduction
text_stim_1 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
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
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_2.setText('''Willkommen zu unserem Experiment! 
                    \n\n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
                    \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
                    \n In jedem Durchgang verändert sich die Anzahl der "E's".
                    \n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(keyList=['space']) 