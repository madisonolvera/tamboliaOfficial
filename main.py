import json
import time
from datetime import datetime as dt

from kivy.app import App
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager, Screen

from utils.RandomGenerator import Random


class TamboliaApp(App):
    def build(self):
        Window.clearcolor = (32 / 255, 67 / 255, 80 / 255, 1)

    @staticmethod
    def get_timestamp():
        now = dt.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")  # Format: YearMonthDay_HourMinuteSecond
        return timestamp


# define different screens
class IndexWindow(Screen):
    pass


class AboutWindow(Screen):
    pass


# Handle the case where `store.get('about')` is not a dictionary


class JournalWindow(Screen):
    @staticmethod
    def get_timestamp():
        now = dt.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")  # Format: YearMonthDay_HourMinuteSecond
        return timestamp

    def save_data(self):
        timestamp = self.get_timestamp()
        filename = "data" + timestamp + ".txt"  # Replace "data_" with your filename prefix
        # Add your code here to save the data to the file
        text_input = self.ids.text_input
        with open(filename, 'a') as f:  # Change 'data.txt' to the filename with the timestamp
            text = text_input.text
            f.write(text)


class WheelOfLifeWindow(Screen):
    @staticmethod
    def get_timestamp():
        now = dt.now()
        timestamp = now.strftime("%m-%d-%Y, %H-%M-%S")
        return timestamp

    def press(self):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now()
        }
        result = Random.get_random_number(influences, range=(1, 4))
        print(result)
        self.ids.result_label.text = str(result)
        self.ids.text_input.disabled = True
        self.ids.dice_roll.disabled = True

        # Map the result to a word and color

        result_mapping = {
            1: ('Blue', 'Balance'),
            2: ('Red', 'Desire'),
            3: ('Yellow', 'Deception'),
            4: ('Green', 'Emotions'),
        }
        word, color = result_mapping.get(result, ('Unknown', 'Unknown'))
        self.ids.result_label.text += f' - {word} - {color}'

    def save_data(self):
        timestamp = self.get_timestamp()
        filename = "data" + timestamp + ".txt"  # Replace "data_" with your filename prefix
        # Add your code here to save the data to the file
        with open(filename, 'a') as f:  # Change 'data.txt' to the filename with the timestamp
            text = self.ids.text_input.text
            result = self.ids.result_label.text
            timestamp = dt.now().strftime("%m-%d-%Y, %H-%M-%S")  # Format: Month Day Year, Hour-Minute-Second
            f.write(f'Question from {timestamp}: {text}\n')
            f.write(f'Result: {result}\n')


class IntensityWindow(Screen):
    def intensity(self):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now()
        }
        result = Random.get_random_number(influences, range=(1, 12))
        self.ids.roll_dice.disabled = True

        with open('intensity.json', 'r') as f:
            word_dict = json.load(f)

        word_definition = word_dict.get(str(result), 'Unknown - Unknown')
        word, definition = word_definition.split(' - ', 1)
        self.ids.result_label.text += f'Result: {result} - {word} - {definition}'

        print(word)


class EnvironmentWindow(Screen):
    def environment(self):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now()
        }
        result = Random.get_random_number(influences, range=(1, 6))
        self.ids.dice_roll.disabled = True

        with open('environment.json', 'r') as f:
            word_dict = json.load(f)

        word_definition = word_dict.get(str(result), 'Unknown - Unknown')
        word, definition = word_definition.split(' - ', 1)
        self.ids.result_label.text += f'Result: {result} - {word} - {definition}'


class ChainLinkWindow(Screen):
    def chain(self):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now()
        }
        result = Random.get_random_number(influences, range=(1, 12))
        self.ids.dice_roll.disabled = True

        with open('chains.json', 'r') as f:
            word_dict = json.load(f)

        word_definition = word_dict.get(str(result), 'Unknown - Unknown')
        word, definition = word_definition.split(' - ', 1)
        self.ids.result_label.text += f'Result: {result} - {word} - {definition}'


class FinishWindow(Screen):
    def finish_quote(self):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now()
        }
        result = Random.get_random_number(influences, range=(1, 60))
        self.ids.finish.disabled = True

        with open('quotes.json', 'r') as f:
            word_dict = json.load(f)

        word_definition = word_dict.get(str(result), 'Unknown')
        self.ids.result_label.text += f' {word_definition}'


class DictionaryWindow(Screen):
    pass


class WindowManager(ScreenManager):
    INFLUENCES = dict()
    INFLUENCES['game_start'] = dt.now()


if __name__ == '__main__':
    TamboliaApp().run()
