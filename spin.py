from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Designate Our .kv design file 
Builder.load_file('spin.kv')

class MyLayout(Widget):
	def spinner_clicked(self, value):
			self.ids.click_label.text = f'You Selected: {value}'
			self.ids.spinner_id.text = "Good Job!"
class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



