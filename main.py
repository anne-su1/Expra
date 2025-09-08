from psychopy import visual
from random import Random
from task_model.task_grid import Task_grid
from experiment_1 import E1


def main():
    print("Start EXPRA")

    win = visual.Window(                    # Psychopy benutzt in visual, window als fkt von visual
        color='grey',                      # Hintergrundfarbe (auch rgb mgl)
        size=[2000, 1000],                    # Anzahl Pixel (Größe Pixel)
        fullscr=True,
        useRetina=True) 

    # Begrüssung
    # Phase 1

    random = Random(42)
    taskGrid = Task_grid(8, 16, random)
    e1 = E1(taskGrid, 240, win)

    print("start practice")
    e1.practice()
    
    # fatigue questionnare 1
    # Phase 2
    # fatigue questionnare 2
    # Danke


if __name__ == "__main__":
    main()