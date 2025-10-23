import pandas as pd
from psychopy import gui

# Klasse zum Anzeigen der Questionnaires
class Questionnaire:

    sub_info: dict
    sub_folder_path: str
    quest_data_1: dict

    # Anzeigen des Supervisory Inputs zum Aufnehmen der Daten der Versuchsperson
    # Daten werden als dictionary zurückgegeben
    def sub_input(self) -> dict:
        supervisory_input = gui.Dlg(title="Participant Data")
        supervisory_input.addField("sub_id", initial="01")
        supervisory_input.addField("age")
        supervisory_input.addField("sex", choices=["male", "female"])
        supervisory_input.addField("normal / corrected sight", choices=["yes", "no"])
        supervisory_input.addField("handedness", choices=["right", "left"])
        supervisory_input.show()

        # nur wenn man auf "OK" drückt, werden eingegebene Daten aufgenommen
        if supervisory_input.OK:
            raw_data = supervisory_input.data
            sub_data = {
                "sub_id": raw_data[0],
                "age": int(raw_data[1]),
                "sex": raw_data[2],
                "normal / corrected sight": raw_data[3],
                "handedness": raw_data[4]
            }
            self.sub_info = sub_data
            return sub_data
        else:
            return None
    
    # Anzeigen des Questionnaires zur subjektiven Erschöpfung nach Phase 1
    def fatigue_questionnaire_1(self):
        fat_quest_1 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_1.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_1.addField("Erschöpfungslevel nach Block ⍺", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Erschöpfungslevel nach Block β", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Erschöpfungslevel nach Block δ", 
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_1.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_1.show()

        # Zwischenspeichern der Daten aus Phase 1 in einem dict
        self.quest_data_1 ={
                    'sub_id' : self.sub_info.get("sub_id"),
                    'Q1E1' : fat_quest_1.data[0],
                    'Q1E2' : fat_quest_1.data[1],
                    'Q1E3' : fat_quest_1.data[2],
                    'Q2Phase1' : fat_quest_1.data[3]
                }

    # Anzeigen des Questionnaires zur subjektiven Erschöpfung nach Phase 2
    def fatigue_questionnaire_2(self):
        fat_quest_2 = gui.Dlg(title="fatigue questionnaire")
        fat_quest_2.addText("1 = niedrigstes Level an Erschöpfung, 5 = höchstes Level an Erschöpfung")
        fat_quest_2.addField("Erschöpfungslevel nach Block ϵ",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Erschöpfungslevel nach Block Ω",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Erschöpfungslevel nach Block 𝜃",
                            choices=["1", "2", "3", "4", "5"])
        fat_quest_2.addField("Haben Sie die Zeitangaben bemerkt?", choices=["bemerkt und häufig nachgesehen", "bemerkt und manchmal nachgesehen", "nicht bemerkt"])
        fat_quest_2.show()

        # Erweiterung des dict aus Phase 1 mit Daten aus Phase 2
        quest_data_final = pd.DataFrame([{
            **self.quest_data_1,
            'Q1E4' : fat_quest_2.data[0],
            'Q1E5' : fat_quest_2.data[1],
            'Q1E6' : fat_quest_2.data[2],
            'Q2Phase2' : fat_quest_2.data[3]
        }])

        # Ausgabe des dict mit Daten aus Phase 1 & 2 zu einer csv Datei
        quest_data_final.to_csv(self.sub_folder_path + f'/sub-{self.sub_info.get("sub_id")}_quest_data.csv')