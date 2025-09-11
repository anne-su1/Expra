import pandas as pd
import os
from psychopy import gui

class Questionnaire:

    sub_info: dict
    sub_folder_path: str
    quest_data_1: dict
    sequence_for_phase_1 : list
    sequence_for_phase_2 : list

    def sub_input(self) -> dict:
        supervisory_input = gui.Dlg(title="Participant Data")
        supervisory_input.addField("sub_id", initial="01")
        supervisory_input.addField("age")
        supervisory_input.addField("sex", choices=["male", "female"])
        supervisory_input.addField("normal or corrected sight", choices=["normal", "corrected"])
        supervisory_input.addField("handedness", choices=["right", "left"])
        supervisory_input.show()

        if supervisory_input.OK:
            raw_data = supervisory_input.data
            sub_data = {
                "sub_id": raw_data[0],
                "age": int(raw_data[1]),
                "sex": raw_data[2],
                "normal or corrected sight": raw_data[3],
                "handedness": raw_data[4]
            }
            self.sub_info = sub_data
            return sub_data
        else:
            return None
    
    def fatigue_questionnaire_1(self):
        fat_quest_1 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_1.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_1.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_1[0].getExperimentNumber()}", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_1[1].getExperimentNumber()}", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_1[2].getExperimentNumber()}", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_1.show()

        self.quest_data_1 ={
                    'sub_id' : self.sub_info.get("sub_id"),
                    'Q1E1' : fat_quest_1.data[0],
                    'Q1E2' : fat_quest_1.data[1],
                    'Q1E3' : fat_quest_1.data[2],
                    'Q2Phase1' : fat_quest_1.data[3]
                }

    def fatigue_questionnaire_2(self):
        fat_quest_2 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_2.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_2.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_2[0].getExperimentNumber()}",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_2[1].getExperimentNumber()}",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField(f"Erschöpfungslevel nach Block {self.sequence_for_phase_2[2].getExperimentNumber()}",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_2.show()

        quest_data_final = pd.DataFrame([{
            **self.quest_data_1,
            'Q1E4' : fat_quest_2.data[0],
            'Q1E5' : fat_quest_2.data[1],
            'Q1E6' : fat_quest_2.data[2],
            'Q2Phase2' : fat_quest_2.data[3]
        }])

        quest_data_final.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_quest_data.csv')