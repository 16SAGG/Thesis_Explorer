from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition as smtransition
from kivy.core.window import Window
Window.size = (1280, 640)

class MainScreen (Screen):
    pass

class SearchScreen (Screen):
    pass

class ThesisExplorerApp(MDApp): #TEA is the acronym
    def build(self):
        # (TEA Div): Adding Screens to ScreenManager #
        sm = ScreenManager(transition = smtransition())
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(SearchScreen(name = "search"))

        # (TEA Div): Setting themes #
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray" 

        return sm

ThesisExplorerApp().run()