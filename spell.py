from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling

# Designate Our .kv design file 
Builder.load_file('spell.kv')

class MyLayout(Widget):
	def press(self):
		# Create instance of Spelling
		s = Spelling()

		# Select the language
		s.select_language('en_US')

		# See the language options
		#print(s.list_languages())

		# Grab the word from the textbox
		word = self.ids.word_input.text

		options = s.suggest(word)
		x = ''
		for item in options:
			x = f'{x} {item}'
		# update our label
		self.ids.word_label.text = f'{x}'

		# Clear input box
		self.ids.word_input.text = ''


class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



