from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


# Designate Our .kv design file 
Builder.load_file('round_buttons.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



