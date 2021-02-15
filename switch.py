from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Our .kv design file 
Builder.load_file('switch.kv')

class MyLayout(Widget):
	def switch_click(self, switchObject, switchValue):
		if (switchValue):
			self.ids.my_label.text = "You clicked the Switch On!!"
		else:
			self.ids.my_label.text = "You clicked the Switch Off!!"
			#self.ids.my_switch.disabled = True

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



