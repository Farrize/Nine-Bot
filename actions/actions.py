# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from sqlite3.dbapi2 import Cursor
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
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

        for i in tracker.latest_message['entities']:
            if i['entity'] == 'fakultas':
                fakultas = i['value']
                dispatcher.utter
                return [fakultas]

        return []
