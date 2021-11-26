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

def sql_connection():
    con = sqlite3.connect('rasaninebot.db')
    Cursor = con.cursor()
    Cursor.execute("")
    con.commit()
    con.close()

def insert_data(data):
    con = sqlite3.connect('rasaninebot.db')
    Cursor = con.cursor()
    Cursor.execute("INSERT INTO user_data(data) VALUES (?)",data)
    con.commit()
    con.close()
    
class ActionUtterFakultas(Action):

    def name(self) -> Text:
        return "action_pengkodean_fakultas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = int(tracker.get_slot('fakultas'))
        def one():
            dispatcher.utter_message(response = "utter_ask/pengkodeanekonomi")

        def two():
            dispatcher.utter_message(response = "utter_ask/pengkodeanhukum")

        def three():
            dispatcher.utter_message(response = "utter_ask/pengkodeanteknik")

        def four():
            dispatcher.utter_message(response = "utter_ask/pengkodeankedokteran")

        def five():
            dispatcher.utter_message(response = "utter_ask/pengkodeanpertanian")

        def six():
            dispatcher.utter_message(response = "utter_ask/pengkodeankeguruan")

        def seven():   
            dispatcher.utter_message(response = "utter_ask/pengkodeanispol")

        def eight():
            dispatcher.utter_message(response = "utter_ask/pengkodeanmipa")

        def nine():
            dispatcher.utter_message(response = "utter_ask/pengkodeanilmukomputer")

        def ten():
            dispatcher.utter_message(response = "utter_ask/pengkodeankesehatanmasyarakat")

        def eleven():
            dispatcher.utter_message(response = "utter_ask/begin_pascasarjana")

        options = {
            1 : one,
            2 : two,
            3 : three,
            4 : four,
            5 : five,
            6 : six,
            7 : seven,
            8 : eight,
            9 : nine,
            10 : ten,
            11 : eleven
        }
        if(slot_value in options):
            options[slot_value]()
        
        return []
