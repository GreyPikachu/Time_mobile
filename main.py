# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from datetime import datetime
import File_redactor


# Глобальные настройки
Window.size = (400, 150)
Window.clearcolor = (80 / 255, 16 / 255, 117 / 255, 1)
Window.title = "Конвертер"


class MyApp(App):
    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()

        self.label = Label(text='Введите, что вы сейчас делаете: ')
        self.today = Label(text='Сейчас: ')

        self.input_data = TextInput(hint_text='1-засыпаю, 2-иду в школу, 3-начал делать уроки,\n4-начал отдыхать, 5-начал другое.', multiline=False)
        self.input_data.bind(text=self.on_text)  # Добавляем обработчик события


    # Получаем данные и производит их конвертацию
    def on_text(self, *args):

        data = self.input_data.text
        if data.isnumeric():

            time_NOW = str(datetime.now())
            time_NOW = time_NOW[:19]

            self.today.text = "Сейчас: " + str(time_NOW)
            time_NOW = str(data + '-' + time_NOW[:10] + ':' + time_NOW[11:])

            File_redactor.write(time_NOW)

            print(time_NOW)


    def build(self):

        # Все объекты будем помещать в один общий слой

        box = BoxLayout(orientation='vertical')

        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.today)

        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()