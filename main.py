from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MainWidget(BoxLayout):
    count = 0
    status = True
    my_text = StringProperty("0")
    less_than_zero = False

    def tambah(self):
        self.count += 1
        self.my_text = str(self.count)

    def kurang(self):
        if self.count <= 0:
            self.less_than_zero = True
        
        else:
            self.count -= 1
            self.my_text = str(self.count)

    def reset_angka(self):
        self.count = 0
        self.my_text = str(self.count)

class Tasbih(App):
    pass

Tasbih().run()