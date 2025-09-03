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
    size=[400, 400],                  # Anzahl Pixel (Größe Pixel)
    fullscr=True,
    useRetina=True)                     # wichitg für Mac, da angegebene Bidschrikmgröße ncht tatsächliche 
