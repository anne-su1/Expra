import pandas as pd
import os
from psychopy import gui

class Questionnaire:

    questData: pd.DataFrame

    def __init__(self, questDataFrame: pd.DataFrame):
        self.questData = questDataFrame

    def sub_input(self) -> dict:
        supervisor_input = gui.Dlg(title="Participant Data")
        supervisor_input.addField("sub_id", initial="01")
        supervisor_input.addField("age")
        supervisor_input.addField("sex", choices=["male", "female"])
        supervisor_input.addField("normal or corrected sight", choices=["normal", "corrected"])
        supervisor_input.addField("handedness", choices=["right", "left"])
        supervisor_input.show()

        if supervisor_input.OK:
            raw_data = supervisor_input.data
            sub_data = {
                "sub_id": raw_data[0],
                "age": int(raw_data[1]),
                "sex": raw_data[2],
                "normal or corrected sight": raw_data[3],
                "handedness": raw_data[4]
            }
            return sub_data
        else:
            return None

    def create_sub_data_folder(self, sub_id: str) -> str:
        # create a folder to store the output
        output_path = os.getcwd() + f'/sub-{sub_id}'
        if not os.path.exists(output_path):         # wenn Pfad nicht existiert, mache diesen ordner (makedirs)
            os.makedirs(output_path)                # zweites if Statement nötig, wenn pfad nicht existiert, um nicht weiter um nicht zu überschreiben
            
        file_path = output_path + f'/sub-{sub_id}_task-catshumans.tsv' # TO DO: change task_catsHuman to real name

        return file_path
    
    def fatigue_questionnaire_1(self):
        supervisor_input = gui.Dlg(title="fatigue questionnaire")
        supervisor_input.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        supervisor_input.addField("Erschöpfungslevel nach Block 1", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Erschöpfungslevel nach Block 2", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Erschöpfungslevel nach Block 3", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        supervisor_input.show()


    def fatigue_questionnaire_2(self):
        supervisor_input = gui.Dlg(title="fatigue questionnaire")
        supervisor_input.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        supervisor_input.addField("Erschöpfungslevel nach Block 4", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Erschöpfungslevel nach Block 5", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Erschöpfungslevel nach Block 6", choices=["1", "2", "3", "4", "5"])
        supervisor_input.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        supervisor_input.show()
