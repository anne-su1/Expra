from psychopy import event, visual

class Instruction:
    win: visual.Window
    color = "black"

    def __init__(self, win:visual.Window):
       self.win = win

    def update_instance_of_win(self, win):
        self.win = win

    def initalHellos(self):
        text_stim_1 = visual.TextStim(self.win, height=0.085, color= self.color)
        text_stim_1.setText(
            '''Willkommen zu unserem Experiment! 
            \n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
            \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
            \n In jedem Durchgang verändert sich die Anzahl der E's. Zählen Sie, wie viele E's enthalten sind und geben Sie die entsprechende Zahl ein. Danach drücken Sie die Leertaste, um zur nächsten Aufgabe zu gelangen.
            \n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        # Funktion die setTxt heißt
        text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(keyList=['space'])     

        text_stim_2 = visual.TextStim(self.win, height=0.085, color= self.color)                              # text stimuli self.win aus Zeile 15
        text_stim_2.setText(
            '''Es gibt 2 Phasen mit je 3 separaten Blöcken. 
            \n Stellen Sie sich vor, dass Sie in einer Notsituation sind, in der es auf Schnelligkeit und Genauigkeit ankommt. 
            \n Versuchen Sie also in jedem Durchgang die Suchaufgabe so schnell und so genau wie möglich durchzuführen.
            \n Nach jedem Block können Sie eine kleine Pause machen.
            \n\n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        # Funktion die setTxt heißt
        text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(keyList=['space']) 

    def instruction_for_phase_1(self):
        text_stim = visual.TextStim(self.win, height=0.085, color= self.color)                              # text stimuli self.win aus Zeile 15
        text_stim.setText(
            '''Wir starten jetzt mit Phase 1. 
            \n Phase 1 besteht aus 3 Blöcken. Vor jedem der Blöcke absolvieren Sie 3 Übungsdurchgänge. Nach jedem Block haben Sie 2 Minuten Pause.
            \n\n\n Zum Starten des Experiments bitte die Leertaste drücken.
        ''')        # Funktion die setTxt heißt
        text_stim.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space']) 

    def instruction_for_phase_2(self):
        text_stim_1 = visual.TextStim(self.win, height=0.085, color= self.color)                              # text stimuli win aus Zeile 15
        text_stim_1.setText(
            '''Jetzt beginnt Phase 2.
            \n Phase 2 besteht ebenso aus 3 Blöcken. Auch hier gibt es vor jedem Block 3 Übungsdurchgänge. Zwischen den Blöcken haben Sie 2 Minuten Pause.
            \n Behalten Sie die selbe Suchstrategie bei, wie bisher.
            \n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        # Funktion die setTxt heißt
        text_stim_1.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space'])

        text_stim_2 = visual.TextStim(self.win, height=0.085, color= self.color)                              # text stimuli win aus Zeile 15
        text_stim_2.setText(
            '''In jedem Durchgang werden Sie einen Countdown-Timer sehen, der anzeigt in welcher Zeit Sie die Suchaufgabe bearbeiten müssen.
            \n Wenn der Countdown abgelaufen ist verschwinden die Buchstaben. Geben Sie bitte trotzdem eine Zahl ein und drücken die Leertaste, um zur nächsten Aufgabe zu gelangen.
            \n\n Zum Starten des Experiments bitte die Leertaste drücken.
        ''')        # Funktion die setTxt heißt
        text_stim_2.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space'])  

    def say_goodbye(self):
        text_stim = visual.TextStim(self.win, height=0.085, color= self.color)                              # text stimuli win aus Zeile 15
        text_stim.setText(
            '''Das Experiment ist jetzt beendet.
            \n\n Vielen Dank für Ihre Teilnahme!
        ''')        # Funktion die setTxt heißt
        text_stim.draw()                                              # zusagmmengefügt, zeig bitte an
        self.win.flip()                                                      # Fenster wird aktualisiert
        event.waitKeys(maxWait= 20.0, keyList=['space']) 