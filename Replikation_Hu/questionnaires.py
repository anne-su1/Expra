import pandas as pd
import os
from psychopy import gui

class Questionnaire:

    quest_data: pd.DataFrame
    sub_info: dict
    sub_folder_path: str


    def __init__(self, quest_data: pd.DataFrame, sub_info: dict, sub_folder_path: str):
        self.quest_data = quest_data
        self.sub_info = sub_info
        self.sub_folder_path = sub_folder_path

    def sub_input(self) -> dict:
        fat_quest_1 = gui.Dlg(title="Participant Data")
        fat_quest_1.addField("sub_id", initial="01")
        fat_quest_1.addField("age")
        fat_quest_1.addField("sex", choices=["male", "female"])
        fat_quest_1.addField("normal or corrected sight", choices=["normal", "corrected"])
        fat_quest_1.addField("handedness", choices=["right", "left"])
        fat_quest_1.show()

        if fat_quest_1.OK:
            raw_data = fat_quest_1.data
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
        fat_quest_1 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_1.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_1.addField("Erschöpfungslevel nach Block 1", choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Erschöpfungslevel nach Block 2", choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Erschöpfungslevel nach Block 3", choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_1.show()

        quest_data_1 = pd.DataFrame({
            'sub_id' : self.sub_info.get("sub_id"),
            'Q1E1' : int(fat_quest_1[0]),
            'Q1E2' : int(fat_quest_1[1]),
            'Q1E3' : int(fat_quest_1[2]),
            'Q2Phase1' : fat_quest_1[3]
        })

        self.quest_data = pd.concat([self.quest_data, quest_data_1], ignore_index=True)


    def fatigue_questionnaire_2(self):
        fat_quest_2 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_2.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_2.addField("Erschöpfungslevel nach Block 4", choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Erschöpfungslevel nach Block 5", choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Erschöpfungslevel nach Block 6", choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_2.show()

        quest_data_2 = pd.DataFrame({
            'sub_id' : self.sub_info.get("sub_id"),
            'Q1E4' : int(fat_quest_2[0]),
            'Q1E5' : int(fat_quest_2[1]),
            'Q1E6' : int(fat_quest_2[2]),
            'Q2Phase2' : fat_quest_2[3]
        })

        self.quest_data = pd.concat([self.quest_data, quest_data_2], ignore_index=True)
        self.quest_data.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_quest_data.csv')