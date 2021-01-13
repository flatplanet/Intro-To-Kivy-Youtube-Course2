from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel


# Designate Our .kv design file 
Builder.load_file('tabs.kv')

class MyLayout(TabbedPanel):
	pass

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



