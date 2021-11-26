# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from sqlite3.dbapi2 import Cursor
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

def querySQL(query: Text):
    conn = sqlite3.connect('rasaninebot.db')
    cur = conn.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    
    return result
    
class ActionUtterFakultas(Action):

    def name(self) -> Text:
        return "action_pengkodean_fakultas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = int(tracker.get_slot('fakultas'))
        def ekonomi():
            dispatcher.utter_message(response = "utter_pengkodeanekonomi")

        def hukum():
            dispatcher.utter_message(response = "utter_pengkodeanhukum")

        def teknik():
            dispatcher.utter_message(response = "utter_pengkodeanteknik")

        def kedokteran():
            dispatcher.utter_message(response = "utter_pengkodeankedokteran")

        def pertanian():
            dispatcher.utter_message(response = "utter_pengkodeanpertanian")

        def keguruan():
            dispatcher.utter_message(response = "utter_pengkodeankeguruan")

        def ispol():   
            dispatcher.utter_message(response = "utter_pengkodeanispol")

        def mipa():
            dispatcher.utter_message(response = "utter_pengkodeanmipa")

        def komputer():
            dispatcher.utter_message(response = "utter_pengkodeanilmukomputer")

        def kesmas():
            dispatcher.utter_message(response = "utter_pengkodeankesehatanmasyarakat")

        def pascasarjana():
            dispatcher.utter_message(response = "utter_pascasarjana")

        def programpendidikan():
            dispatcher.utter_message(response = "utter_programpendidikan")

        options = {
            1 : ekonomi,
            2 : hukum,
            3 : teknik,
            4 : kedokteran,
            5 : pertanian,
            6 : keguruan,
            7 : ispol,
            8 : mipa,
            9 : komputer,
            10 : kesmas,
            11 : pascasarjana,
            12 : programpendidikan
        }
        if(slot_value in options):
            options[slot_value]()
        
        return []

class ActionGambar(Action):
        def name(self) -> Text:
            return "action_gambar"

        async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:
            
            query = "SELECT link_gambar FROM gambar WHERE nama_gambar = 'formKPM'"

            

            queryResult = querySQL(query)
            print(queryResult)
            dispatcher.utter_message(text='form KPM', image=queryResult[0][0])

            return []

