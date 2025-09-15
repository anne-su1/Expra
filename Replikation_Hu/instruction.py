from psychopy import event, visual

# Klasse mit gesammelten Hauptinstruktionen 
class Instruction:
    win: visual.Window
    color = "black"

    # Erzwingt dass ein Objekt der Klasse Instruction ein Window bekommt
    def __init__(self, win:visual.Window):
       self.win = win

    # Ausgabe der Begrüßung und Experimentbeschreibung auf den ersten Displayfenstern, mit Leertaste gehts weiter
    def initalHellos(self):
        text_stim_1 = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)
        text_stim_1.setText(
            '''Willkommen zu unserem Experiment! 
            \n\n In diesem Experiment sollen Sie die Buchstaben "E" unter den "F" suchen und zählen.
            \n Diese Buchstaben werden auch gedreht und gespiegelt angezeigt. 
            \n In jedem Durchgang verändert sich die Anzahl der E's. Zählen Sie, wie viele E's enthalten sind, drücken Sie die Leertaste und geben Sie die entsprechende Anzahl ein.
            \n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        
        text_stim_1.draw()                                              
        self.win.flip()                                                      
        event.waitKeys(keyList=['space'])     

        text_stim_2 = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                              
        text_stim_2.setText(
            '''Es gibt 2 Phasen mit je 3 separaten Blöcken. 
            \n Stellen Sie sich vor, dass Sie in einer Notsituation sind, in der es auf Schnelligkeit und Genauigkeit ankommt. 
            \n Versuchen Sie also in jedem Durchgang die Suchaufgabe so schnell und so genau wie möglich durchzuführen.
            \n Nach jedem Block können Sie eine kleine Pause machen.
            \n\n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        
        text_stim_2.draw()                                             
        self.win.flip()                                                      
        event.waitKeys(keyList=['space']) 

        text_stim_3 = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                              
        text_stim_3.setText(
            '''Nach jeder Phase werden Sie zu Ihrem subjektiven Erschöpfungslevel befragt.
            \n\n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        
        text_stim_3.draw()                                              
        self.win.flip()                                                      
        event.waitKeys(keyList=['space']) 

    # Ausgabe der Beschreibung und Instruktion von Phase 1 auf den Displayfenstern, mit Leertaste gehts weiter
    def instruction_for_phase_1(self):
        text_stim = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                              
        text_stim.setText(
            '''Wir starten jetzt mit Phase 1. 
            \n Phase 1 besteht aus 3 Blöcken in zufälliger Reihenfolge. Vor Beginn der Blöcke absolvieren Sie einmalig 3 Übungsdurchgänge. Nach jedem Block haben Sie 2 Minuten Pause.
            \n Bitte schätzen Sie nach jedem Block ihr Erschöpfungslevel ein und teilen Sie es Ihrem Versuchsleiter mit.
            \n\n\n Zum Starten des Experiments bitte die Leertaste drücken.
        ''')       
        text_stim.draw()                                              
        self.win.flip()                                                      
        event.waitKeys(keyList=['space']) 

    # Ausgabe der Beschreibung und Instruktion von Phase 2 auf den Displayfenstern, mit Leertaste gehts weiter
    def instruction_for_phase_2(self):
        text_stim_1 = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                             
        text_stim_1.setText(
            '''Jetzt beginnt Phase 2.
            \n Phase 2 besteht ebenso aus 3 Blöcken in zufälliger Reihenfolge. Zwischen den Blöcken haben Sie 2 Minuten Pause.
            \n Bitte schätzen Sie nach jedem Block ihr Erschöpfungslevel ein und teilen Sie es Ihrem Versuchsleiter mit.
            \n Behalten Sie dieselbe Suchstrategie bei, wie bisher.
            \n\n Zum Fortfahren bitte die Leertaste drücken.
        ''')        
        text_stim_1.draw()                                             
        self.win.flip()                                                     
        event.waitKeys(keyList=['space'])

        text_stim_2 = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                              
        text_stim_2.setText(
            '''In jedem Durchgang werden Sie einen Countdown-Timer sehen, der anzeigt in welcher Zeit Sie die Suchaufgabe bearbeiten müssen.
            \n Im Idealfall drücken Sie vor Ablauf der Zeit die Leertaste, um die Anzahl der E's einzutragen.
            \n Wenn der Countdown abgelaufen ist verschwinden die Buchstaben. Geben Sie bitte trotzdem eine Anzahl ein.
            \n\n Zum Starten des Experiments bitte die Leertaste drücken.
        ''')       
        text_stim_2.draw()                                             
        self.win.flip()                                                     
        event.waitKeys(keyList=['space'])  
        
    # Ausgabe der Verabschiedung auf den Displayfenstern
    def say_goodbye(self):
        text_stim = visual.TextStim(self.win, height=0.085, color= self.color, wrapWidth= 1.8)                              
        text_stim.setText(
            '''Das Experiment ist jetzt beendet.
            \n\n Vielen Dank für Ihre Teilnahme!
        ''')       
        text_stim.draw()                                              
        self.win.flip()                                                      
        event.waitKeys(maxWait= 20.0, keyList=['space']) 