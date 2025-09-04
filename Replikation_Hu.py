import os                                       # Dateien mit python anlegen etc
import glob                                     # systematisches Einlesen von Dateien auf Festplatte
import pandas as pd                             # besser als numpy für uns
from psychopy import core, visual, gui, event   # core: basisfkt (timing), visual: fenster/bilder anzeigen, intruktionen, event: mgl das VP alle mgl eingaben machen kann
import random                                   # ähnlich numpy.random.shuffle
import time                                     # kann, muss aber nicht verwendet werden

from task_model.task_grid import task_grid

supervisor_input = gui.Dlg(title="Participant Data")
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
    color='grey',                      # Hintergrundfarbe (auch rgb mgl)
    size=[2000, 1000],                    # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# introduction phase 1
text_stim_1 = visual.TextStim(win,
                              height=0.085)                              # text stimuli_grid win aus Zeile 15
text_stim_1.setText('''Willkommen zu unserem Experiment! 
                    \n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
                    \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
                    \n In jedem Durchgang verändert sich die Anzahl der "E's". Zählen Sie, wie viele "E's" enthalten sind und geben Sie die entsprechende Zahl ein. Danach drücken Sie die Leertaste, um zur nächsten Aufgabe zu gelangen.
                    \n\n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space'])     


text_stim_2 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_2.setText('''Es gibt 2 Phasen mit je 3 separaten Blöcken. 
                    \n Stellen Sie sich vor, dass Sie in einer Notsituation sind, in der es auf Schnelligkeit und Genauigkeit ankommt. 
                    \n Versuchen Sie also in jedem Durchgang die Suchaufgabe so schnell und so genau wie möglich durchzuführen.
                    \n Nach jedem Block können Sie eine kleine Pause machen.
                    \n\n\n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space']) 


text_stim_3 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_3.setText('''Wir starten jetzt mit Phase 1. 
                    \n Phase 1 besteht aus 3 Blöcken. Vor jedem der Blöcke absolvieren Sie 3 Übungsdurchgänge. Nach jedem Block haben Sie 2 Minuten Pause.
                    \n\n\n Zum Starten des Experiments bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_3.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space']) 

# function e1
global_duration = 240
global_timer = core.CountdownTimer(global_duration)

#while global_timer.getTime() > 0:


    

# function e2


# function e3


# function e4


# function e5


# function e6



# main experiment phase 1





# questionnaire phase 1
win.close()
supervisor_input = gui.Dlg(title="fatigue questionnaire")
supervisor_input.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
supervisor_input.addField("Erschöpfungslevel nach Block 1", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Erschöpfungslevel nach Block 2", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Erschöpfungslevel nach Block 3", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
supervisor_input.show()

win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
    color='grey',                      # Hintergrundfarbe (auch rgb mgl)
    size=[2000, 1000],                    # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# introduction phase 2
text_stim_4 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_4.setText('''Jetzt beginnt Phase 2.
                    \n Phase 2 besteht ebenso aus 3 Blöcken. Auch hier gibt es vor jedem Block 3 Übungsdurchgänge. Zwischen den Blöcken haben Sie 2 Minuten Pause.
                    \n Behalten Sie die selbe Suchstrategie bei, wie bisher.
                    \n\n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_4.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space'])   

text_stim_5 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_5.setText('''In jedem Durchgang werden Sie einen Countdown-Timer sehen, der anzeigt in welcher Zeit Sie die Suchaufgabe bearbeiten müssen.
                    \n Wenn der Countdown abgelaufen ist verschwinden die Buchstaben. Geben Sie bitte trotzdem eine Zahl ein und drücken die Leertaste, um zur nächsten Aufgabe zu gelangen.
                    \n\n Zum Starten des Experiments bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
text_stim_5.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space'])  

# main experiment phase 2



# questionnaire phase 2
win.close()
supervisor_input = gui.Dlg(title="fatigue questionnaire")
supervisor_input.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
supervisor_input.addField("Erschöpfungslevel nach Block 4", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Erschöpfungslevel nach Block 5", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Erschöpfungslevel nach Block 6", choices=["1", "2", "3", "4", "5"])
supervisor_input.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
supervisor_input.show()

win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
    color='grey',                      # Hintergrundfarbe (auch rgb mgl)
    size=[2000, 1000],                    # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 

# the end
text_stim_6 = visual.TextStim(win,
                              height=0.085)                              # text stimuli win aus Zeile 15
text_stim_6.setText('''Das Experiment ist jetzt beendet.
                    \n\n Vielen Dank für Ihre Teilnahme!''')        # Funktion die setTxt heißt
text_stim_6.draw()                                              # zusagmmengefügt, zeig bitte an
win.flip()                                                      # Fenster wird aktualisiert
event.waitKeys(maxWait= 20.0, keyList=['space']) 

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

