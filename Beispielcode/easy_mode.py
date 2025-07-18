import os                                   # Dateien mit python anlegen etc
import glob                                 # systematisches Einlesen von Dateien auf Festplatte
import pandas as pd                         # besser als numpy für uns
from psychopy import core, visual, event    # core: basisfkt (timing), visual: fenster/bilder anzeigen, intruktionen, event: mgl das VP alle mgl eingaben machen kann
import random                               # ähnlich numpy.random.shuffle
import time                                 # kann, muss aber nicht verwendet werden

# easy input
sub_id = '01'               # white-format
age = 23
sex = 'm'
glasses = True

# window specific to our hardware
win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
    color='black',                      # Hintergrundfarbe (auch rgb mgl)
    size=[2560, 1440],                  # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# paths to visual stimuli
img_dir = os.getcwd() + '/session_3/exp_stim/'
img_list = glob.glob(img_dir + '*.jpg')  # alle jpg als Liste wiedergeben

# usefull stuff
max_trials = len(img_list)      # len() als length -> max Anzahl Versuchsdurchgänge ist gleich der Listenlänge
trial_tracker = 0               #für white format

# create a folder and a dataframe to store the output
output_path = os.getcwd() + f'/sub-{sub_id}'
if not os.path.exists(output_path):         # wenn Pfad nicht existiert, mache diesen ordner (makedirs)
    os.makedirs(output_path)                # zweites if Statement nötig, wenn pfad nicht existiert, um nicht weiter um nicht zu überschreiben
    
behav_data = pd.DataFrame({'sub_id' : [],               # dictionary nur dann verwenden bzw verändern wenn wirklich nötig 
                            'age' : [],                 # [] leere Liste
                            'sex' : [],                 # dataframe wird mit jedem versuchsdurchgang gefüllt
                            'glasses' : [],
                            'block' : [],
                            'trial' : [],
                            'reaction_time' : [],
                            'key_pressed' : []
                            })
        
file_path = output_path + f'/sub-{sub_id}_task-catshumans.tsv'

# start introduction
text_stim_1 = visual.TextStim(win)                              # text stimuli win aus Zeile 15
text_stim_1.setText('Willkommen zu unserem Experiment!')        # Funktion die setTxt heißt
text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
core.wait(5)                                                    # Fenster wird 5s angezeigt

stext_stim_2.setText('Das Experiment läuft momentan auf Basis von Spaghetti Code. Funktioniert aber trotzdem. Irgendwie. \n\n Drücken Sie die Leertaste um zu beginnen!')
text_stim_2.draw()
win.flip()
event.waitKeys(maxWait=20.0, keyList=['space'])                 # warte 20s bis schließen (kann man auch einfach nicht definieren), oder VP drückt Taste (eckige Klammer: Liste)

# start actual experiment
for block in range(1, 4):               # block: alle (trials?) oder eher stimuli # bei range funktion wird letztes (4 nicht mit ausgegeben-> hier nur 3 Blöcke)
    # randomize trial order after each block
    shuffled_list = random.sample(img_list, len(img_list))   # Alternative zur numpy shuffle, nach Block schreiben, sonst alle Blöcke gleich randomisiert, nicht nach trials, damit alle bilder in einem block vorhanden

    for trial in range(1, max_trials+1):
        trial_tracker += 1 # add one per loop to keep track of trials
        image_stim = visual.ImageStim(win, image=shuffled_list[trial])
        image_stim.draw()
        win.flip()

        # start timer at the beginning of each trial
        start_time = time.process_time()

        # get user input
        response = event.waitKeys(maxWait=20.0, keyList=['a', 'l'])

        if response == ['a'] or response == ['l']:
            reaction_time = (time.process_time() - start_time)

        # collect user input
        trial_column = pd.DataFrame({'sub_id' : [sub_id], 
                                     'age' : [age],
                                     'sex' : [sex],
                                     'glasses' : [glasses],
                                     'block' : [block],
                                     'trial' : [trial_tracker],
                                     'reaction_time' : [reaction_time],
                                     'key_pressed' : [response]
                                     })
        
        behav_data = behav_data.append(trial_column)
        behav_data.to_csv(file_path, index=False, sep='\t')

        # ITI
        win.flip()
        core.wait(0.5)

    if block < 3:
        text_stim_3 = visual.TextStim(win)                      # Fixationskreuz auch mit TextStim mgl
        text_stim_3.setText(f'Block {block} ist nun beendet. Sie können nun eine Pause einlegen. \n\n Drücken Sie die Leertaste sobald sie fortfahren möchten!')
        text_stim_3.draw()
        win.flip()
        event.waitKeys(maxWait=float('inf'), keyList=['space'])

text_stim_4 = visual.TextStim(win)
text_stim_4.setText('Das Experiment ist nun zu Ende. \n\n Vielen Dank für Ihre Teilnahme!')
text_stim_4.draw()
win.flip()
event.waitKeys(maxWait=50.0, keyList=['escape'])

# end experiment
core.quit()

# Abgabe 3 Wochen vor 1.Oktober