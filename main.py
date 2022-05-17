from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

from kivymd.uix.label import MDLabel , MDIcon

from kivymd.uix.button import MDRectangleFlatButton , MDIconButton

from kivy.core.window import Window

Window.size = (400,600)

image = '''
Image:
	source: 'images/sit.png'
	pos_hint:{'center_x':0.5,'center_y':0.8}
	size_hint:(0.5,0.5)
'''


class MyApp(MDApp):
	def build(self):
		self.title = "Learn Py KivyMd"
		# had l5asais 5asa b button
		self.theme_cls.primary_palette = "Red" #color
		self.theme_cls.primary_hue = "500" #chfafiya
		self.theme_cls.theme_style = "Dark" #Dark or Light : hada lwn l5lfiya kompli
		screen = Screen()
		Label = MDLabel(text= "Python",
		halign='center',
		theme_text_color = "Primary",
		font_style= "H3",
		pos_hint={'center_x':0.5,'center_y':0.6}

		)
		btn_flat1 = MDRectangleFlatButton(text= 'Python KivyMd',
		pos_hint={'center_x':0.5,'center_y':0.1},
		size_hint = (0.6,0.1)
		)
		btn_flat2 = MDRectangleFlatButton(text= 'Python SQL',
		pos_hint={'center_x':0.5,'center_y':0.2},
		size_hint = (0.6,0.1)
		)
		btn_flat3 = MDRectangleFlatButton(text= 'Python Tkinter',
		pos_hint={'center_x':0.5,'center_y':0.3},
		size_hint = (0.6,0.1)
		)
		btn_flat4 = MDRectangleFlatButton(text= 'Python Flask',
		pos_hint={'center_x':0.5,'center_y':0.4},
		size_hint = (0.6,0.1)
		)
		
		iuc1 = MDIconButton(icon='code-braces',
		pos_hint={'center_x':0.3,'center_y':0.1}
		)

		iuc2 = MDIconButton(icon='code-braces',
		pos_hint={'center_x':0.3,'center_y':0.2}
		)

		iuc3 = MDIconButton(icon='code-braces',
		pos_hint={'center_x':0.3,'center_y':0.3}
		)

		iuc4 = MDIconButton(icon='code-braces',
		pos_hint={'center_x':0.3,'center_y':0.4}
		)
		images = Builder.load_string(image)
		screen.add_widget(btn_flat1)
		screen.add_widget(btn_flat2)
		screen.add_widget(btn_flat3)
		screen.add_widget(btn_flat4)
		screen.add_widget(images)
		screen.add_widget(Label)
		screen.add_widget(iuc1)
		screen.add_widget(iuc2)
		screen.add_widget(iuc3)
		screen.add_widget(iuc4)
		return screen
MyApp().run()