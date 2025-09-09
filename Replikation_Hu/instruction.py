from psychopy import event, visual, gui
import os
import pandas as pd

class Instruction:
    win: visual.Window

    def __init__(self, win:visual.Window):
       self.win = win

    

    def initalHellos(self):

        text_stim_1 = visual.TextStim(self.win,
                                      height=0.085)                              # text stimuli_grid self.win aus Zeile 15
        text_stim_1.setText('''Willkommen zu unserem Experiment! 
                            \n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
                            \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
                            \n In jedem Durchgang verändert sich die Anzahl der "E's". Zählen Sie, wie viele "E's" enthalten sind und geben Sie die entsprechende Zahl ein. Danach drücken Sie die Leertaste, um zur nächsten Aufgabe zu gelangen.
                            \n\n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
        text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space'])     
        event.getKeys()

        text_stim_2 = visual.TextStim(self.win,
                                      height=0.085)                              # text stimuli self.win aus Zeile 15
        text_stim_2.setText('''Es gibt 2 Phasen mit je 3 separaten Blöcken. 
                            \n Stellen Sie sich vor, dass Sie in einer Notsituation sind, in der es auf Schnelligkeit und Genauigkeit ankommt. 
                            \n Versuchen Sie also in jedem Durchgang die Suchaufgabe so schnell und so genau wie möglich durchzuführen.
                            \n Nach jedem Block können Sie eine kleine Pause machen.
                            \n\n\n Zum Fortfahren bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
        text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space']) 


        text_stim_3 = visual.TextStim(self.win,
                                      height=0.085)                              # text stimuli self.win aus Zeile 15
        text_stim_3.setText('''Wir starten jetzt mit Phase 1. 
                            \n Phase 1 besteht aus 3 Blöcken. Vor jedem der Blöcke absolvieren Sie 3 Übungsdurchgänge. Nach jedem Block haben Sie 2 Minuten Pause.
                            \n\n\n Zum Starten des Experiments bitte die Leertaste drücken.''')        # Funktion die setTxt heißt
        text_stim_3.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space']) 