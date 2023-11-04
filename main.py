from utils.RandomGenerator import Random
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.app import App
from datetime import datetime as dt
import time
from kivy.core.window import Window


class TamboliaApp(App):
    def build(self):
        Window.clearcolor = (32/255, 67/255, 80/255, 1)


# define different screens
class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
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


class FourthWindow(Screen):
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


class FifthWindow(Screen):
    def save_data(self):
        text_input = self.ids.text_input.text

        self.parent.INFLUENCES['question'] = text_input

        with open('data.txt', 'a') as f:
            f.write(text_input)

class SixthWindow(Screen):

    def pressTwo(self, rev_dict=None):
        res = self.parent.INFLUENCES
        print(res)
        influences = {
            'now': time.time(),
            'name': 'peter',
            'date': dt.now(),
        }
        result = Random.get_random_number(influences, range=(1, 12))

        word_dict = {
            "Contemplation": 1,
            "Doubt": 2,
            "Hope": 3,
            "Excess": 4,
            "Nourishment": 5,
            "Stagnation": 6,
            "Promotion": 7,
            "Decay": 8,
            "Power": 9,
            "Chaos": 10,
            "Wonderful": 11
        }
        rev_dict = {v: k for k, v in word_dict.items()}
        word = rev_dict[result]

        print(word)
class SeventhWindow(Screen):
    pass

class EighthWindow(Screen):
    pass

class NinthWindow(Screen):
    pass

class TenthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    INFLUENCES = dict()
    INFLUENCES['game_start'] = dt.now()

class MyBoxLayout(Widget):
    pass
    # def press(self):
    # generate random dice number and display the number
    # def press(self):


if __name__ == '__main__':
    TamboliaApp().run()
