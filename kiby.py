#Імпорт віджетів
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
import random


class MyApp(App):
    def build(self):
        button = Button(text='Натисни')
        spinner = Spinner()
        self.label = Label(text='Привіт')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(button)
        layout.add_widget(spinner)
        layout.add_widget(self.label)
        button.bind(on_press=self.click_button)
        return layout
    def click_button(self,instance):
        list1 = []
        a = ''
        for _ in range(20):
            
            a += str(random.randint(0,10))
        self.label.text = a
        
        


if __name__ == '__main__':
    MyApp().run()

        


