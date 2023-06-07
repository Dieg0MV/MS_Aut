import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import xlrd
from selenium import webdriver
import time
import pywhatkit




class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Nombre del archivo:', size_hint=(1, None), height=40))
        self.filename_input = TextInput(multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.filename_input)

        self.add_widget(Label(text='Mensaje:', size_hint=(1, None), height=40))
        self.message_input = TextInput(multiline=True, size_hint=(1, 3), height=40)
        self.add_widget(self.message_input)

        self.send_button = Button(text='Enviar', size_hint=(1, None), height=40)
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, instance):
        filename = self.filename_input.text
        message = self.message_input.text

        try:
            excelFile = xlrd.open_workbook(filename)
            sheet1 = excelFile.sheet_by_index(0)

            for nums in range(0, sheet1.nrows):
                numeros = sheet1.cell_value(rowx=nums, colx=0)
                nombre = sheet1.cell_value(rowx=nums, colx=1)



                try:
                    pywhatkit.sendwhatmsg_instantly(numeros, message)
                    print("Se envió el mensaje a", nombre)

                except:

                    print("No se pudo enviar el mensaje a", nombre)

        except Exception as e:
            print("Ocurrió un error:", str(e))


class MyApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
