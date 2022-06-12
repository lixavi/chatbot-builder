from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text

class ActionCustomIntentHandler(Action):
    def name(self) -> Text:
        return "action_custom_intent_handler"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Custom intent detected! How can I help with that?")
        return []

class ActionInformProduct(Action):
    def name(self) -> Text:
        return "action_inform_product"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.latest_message.get("entities", [{"product": ""}])[0]["product"]
        dispatcher.utter_message(f"Sure, I have noted the product: {product}. How can I assist you further?")
        return []

class ActionInformLocation(Action):
    def name(self) -> Text:
        return "action_inform_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.latest_message.get("entities", [{"location": ""}])[0]["location"]
        dispatcher.utter_message(f"Got it, your location is {location}. How can I assist you further?")
        return []

class ActionAskHelp(Action):
    def name(self) -> Text:
        return "action_ask_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Sure, I'm here to assist you. Please let me know how I can help.")
        return []
