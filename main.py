import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.image import Image as CoreImage

from operations import operation


class ActionChangeDialog(BoxLayout):
    go = ObjectProperty(None)
    cancel = ObjectProperty(None)
class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
class ColorSpaceBar(BoxLayout):
    ah = ObjectProperty(None)
class SmoothBar(BoxLayout):
    ah = ObjectProperty(None)
class ThreasholdingBar(BoxLayout):
    ah = ObjectProperty(None)
class TransformationsBar(BoxLayout):
    ah = ObjectProperty(None)
class GradientsBar(BoxLayout):
    ah = ObjectProperty(None)
class EdgeDetectionBar(BoxLayout):
    ah = ObjectProperty(None)    
class HoughTransformBar(BoxLayout):
    ah = ObjectProperty(None)

class Root(BoxLayout):
    ah = operation()
    widgetsBarList = ["Change ColorSpace","Blur","Threashold","Transform","Gradient","Edge Detection","Hough Transform"]

    def get_action_bar_class(self, bar):
        if bar == self.widgetsBarList[0]:
            return ColorSpaceBar(ah = self.ah)
        elif bar == self.widgetsBarList[1]:
            return SmoothBar(ah = self.ah)
        elif bar == self.widgetsBarList[2]:
            return ThreasholdingBar(ah = self.ah)
        elif bar == self.widgetsBarList[3]:
            return TransformationsBar(ah = self.ah)
        elif bar == self.widgetsBarList[4]:
            return GradientsBar(ah = self.ah)
        elif bar == self.widgetsBarList[5]:
            return EdgeDetectionBar(ah = self.ah)
        elif bar == self.widgetsBarList[6]:
            return HoughTransformBar(ah = self.ah)

    def show_action_bar(self, bar):
        if len(self.ah.actions.keys()) > 0:
            self.ah.lastAction = self.ah.action
            self.ah.action = bar
            self.ids['actionBar'].clear_widgets()
            self.ids['actionBar'].add_widget(self.get_action_bar_class(bar))
            self.ids['actionsLabel'].text = self.ids['actionsLabel'].text+" / "+bar
        else:
            self.ids['actionBar'].clear_widgets()
            self.ids['actionBar'].add_widget(Label(text='Please Select an image', font_size=30, color=(1,0.5,0.5,1)))
    
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.ah.action = self.ah.lastAction = 'load'
        self.ah.actions[self.ah.action] = filename[0]
        self.ids['mainImg'].source = filename[0]
        self.ids['actionBar'].clear_widgets()
        self.ids['actionBar'].add_widget(Label(text='Choose actions', font_size=30, color=(1,0.5,0.5,1)))
        self.ids['actionsLabel'].text = self.ids['actionsLabel'].text+"load"
        self.ah.imgView = self.ids['mainImg']
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

class opencvPlayground(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('ActionChangeDialog', cls=ActionChangeDialog)
Factory.register('ColorSpaceBar', cls=ColorSpaceBar)
Factory.register('SmoothBar', cls=SmoothBar)
Factory.register('ThreasholdingBar', cls=ThreasholdingBar)
Factory.register('TransformationsBar', cls=TransformationsBar)
Factory.register('GradientsBar', cls=GradientsBar)
Factory.register('EdgeDetectionBar', cls=EdgeDetectionBar)
Factory.register('HoughTransformBar', cls=HoughTransformBar)

if __name__ == '__main__':
    opencvPlayground().run()
