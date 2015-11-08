#test class for Monitor program (part 1 of three)

from tkinter import *
from MonitorFSM import *
#import custom made class for drawing shapes on the sensehat
import DrawShapes as DRAW
import time
try:
	import RPi.GPIO as GPIO
except RuntimeError:
		print('Error importing RPi.GPIO!\n',
			  'This is probably because you need superuser privileges.\n',
			  'You can achieve this by using "sudo" to run your script')


class GUI(Tk):

	IRSENSOR = 33 # IR sensor on pin 33

	def __init__(self):
		super().__init__()
		
		self.geometry('300x200')
		self.configure(background="black")
		# self.text = Text(self, background='black', foreground='white', font=('Comic Sans MS', 12))
		# self.text.pack()
		self.header = Label(self, text = "IR sensor alarm", fg = "red" ,background='black')
		self.header.pack()

		self.state_label = Label(self, text = "DEACTIVATED", fg = "red", background='black',font=("Helvetica", 16))
		self.state_label.pack(pady=(70,0))

		self.message_label = Label(self, text = "", fg = "red", background='black',font=("Helvetica", 16))
		self.message_label.pack()

		self.bind('<KeyPress>', self._onKeyPress) # if any key is pressed call _onKeyPress


		# use P1 header pin numbering convention
		GPIO.setmode(GPIO.BOARD)

		# configure pin 33 as input
		GPIO.setup(GUI.IRSENSOR, GPIO.IN)

		#call _IRSensorEvevt when ir signal recieved        
		GPIO.add_event_detect(GUI.IRSENSOR, GPIO.RISING, callback=self._IRSensorEvent)

		# create instance of monitor FSM and initialize to deactivated
		self.fsm = MonitorFSM()
		self.fsm.start()
		# draw a cross for the inital deactivated state
		DRAW._drawCross()




	def _onKeyPress(self, event):
		# print(event.keysym)
		output = self.fsm.step(event.keysym)
		# print (output)
		self._process(output);

	def _IRSensorEvent(self, channel):
		print (self.fsm.state)
		output = self.fsm.step("IRSens")
		self._process(output)



	# from given output call the correct response 
	def _process(self, output):
		if output == "cross":
			DRAW._drawCross()
			self.state_label.configure(text="DEACTIVATED", fg="red")
			self.message_label.configure(text="", fg="red")
		elif output == "right_arrow":
			DRAW._draw_rigth_arrow()
			self.state_label.configure(text="DEACTIVATED:")
			self.message_label.configure(text="> waiting for user input...")
		elif output == "left_arrow":
			DRAW._draw_left_arrow()
			self.state_label.configure(text="ACTIVATED:")
			self.message_label.configure(text="> Waiting for user input...")
		elif output == "empty_circle_red":
			self.state_label.configure(text="DEACTIVATED:")
			self.message_label.configure(text="Monitor will become active in 60 seconds.")
			DRAW._draw_empty_circle()
			self.after(5000, DRAW._draw_full_circle)
			self.after(5001, self.change_to_activated)
			self.fsm.state = "activated"
		elif output == "full_circle_green":
			DRAW._draw_full_circle()
			self.state_label.configure(text="ACTIVATED")
			self.message_label.configure(text="")
			# print(self.fsm.state)
		elif output == "alarmed":
			print("call the code from part 2 of the assignment")


	def change_to_activated(self):
		self.state_label.configure(text = "ACTIVATED", fg = "green")
		self.message_label.configure(text="", fg = "green")

		

if __name__ == '__main__':
	app = GUI()
	app.mainloop()
