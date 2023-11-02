#Esta es la parte grafica de el programa necesitas descargar What.py para que funcione esta parte por que importa la logica

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
import xlrd
from selenium import webdriver
from Whats import Logica

class CustomButton(ButtonBehavior, Label):
    pass


class MyInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(MyInterface, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.size_hint_y = None
        self.height = Window.height

        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Color gris oscuro
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Label(text='Nombre del archivo:', size_hint=(1, None), height=40))
        self.filename_input = TextInput(multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.filename_input)

        self.add_widget(Label(text='Mensaje:', size_hint=(1, None), height=40))
        self.message_input = TextInput(multiline=True, size_hint=(1, 3), height=40)
        self.add_widget(self.message_input)

        self.send_button = CustomButton(text='Enviar', size_hint=(1, None), height=40)

        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, instance):
        filename = self.filename_input.text
        message = self.message_input.text
        Logica(filename, message)




class MyApp(App):
    def build(self):
        return MyInterface()


if __name__ == '__main__':
    MyApp().run()
