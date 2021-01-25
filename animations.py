from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# Designate Our .kv design file 
Builder.load_file('animations.kv')

class MyLayout(Widget):
	def animate_it(self, widget, *args):
		# Define The Animation you want to do
		animate = Animation(
			background_color=(0,0,1,1),
			duration=1)

		# Do second animation
		animate += Animation(
			size_hint = (1,1))

		# Do Third animation
		animate += Animation(
			size_hint = (.5,.5))

		animate += Animation(
			pos_hint = {"center_x": 0.1})

		animate += Animation(
			pos_hint = {"center_x": 0.5})

		# Start The Animation
		animate.start(widget)

		# Create a callback
		animate.bind(on_complete = self.my_callback)

	def my_callback(self, *args):
		self.ids.my_label.text = "Wow! Look At That!"




class AwesomeApp(App):
	def build(self):
		return MyLayout()


if __name__ == '__main__':
	AwesomeApp().run()



