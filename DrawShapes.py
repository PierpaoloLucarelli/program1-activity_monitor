from sense_hat import SenseHat
hat = SenseHat()

def _drawCross():
	hat.clear(0,0,0)
	X = [255, 0, 0]  # Red
	O = [0, 0, 0]  # White

	question_mark = [
	X, O, O, O, O, O, O, X,
	O, X, O, O, O, O, X, O,
	O, O, X, O, O, X, O, O,
	O, O, O, X, X, O, O, O,
	O, O, O, X, X, O, O, O,
	O, O, X, O, O, X, O, O,
	O, X, O, O, O, O, X, O,
	X, O, O, O, O, O, O, X
	]

	hat.set_pixels(question_mark)

def _draw_rigth_arrow():
	hat.clear(0,0,0)
	X = [255, 0, 0]  # Red
	O = [0, 0, 0]  # White

	question_mark = [
	O, O, X, O, O, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, O, O, X, O, O, O,
	O, O, O, O, O, X, O, O,
	O, O, O, O, O, X, O, O,
	O, O, O, O, X, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, X, O, O, O, O, O
	]

	hat.set_pixels(question_mark)

def _draw_left_arrow():
	hat.clear(0,0,0)
	X = [0, 255, 0]  # Red
	O = [0, 0, 0]  # White

	question_mark = [
	O, O, O, O, O, X, O, O,
	O, O, O, O, X, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, X, O, O, O, O, O,
	O, O, X, O, O, O, O, O,
	O, O, O, X, O, O, O, O,
	O, O, O, O, X, O, O, O,
	O, O, O, O, O, X, O, O
	]

	hat.set_pixels(question_mark)

def _draw_empty_circle():
	hat.clear(0,0,0)
	X = [255, 0, 0]  # Red
	O = [0, 0, 0]  # White

	circle = [
	O, O, X, X, X, X, O, O,
	O, X, O, O, O, O, X, O,
	X, O, O, O, O, O, O, X,
	X, O, O, O, O, O, O, X,
	X, O, O, O, O, O, O, X,
	X, O, O, O, O, O, O, X,
	O, X, O, O, O, O, X, O,
	O, O, X, X, X, X, O, O
	]

	hat.set_pixels(circle)

def _draw_full_circle():
	hat.clear(0,0,0)
	X = [0, 255, 0]
	O = [0, 0, 0]  # White

	circle = [
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	X, X, X, X, X, X, X, X,
	X, X, X, X, X, X, X, X,
	X, X, X, X, X, X, X, X,
	X, X, X, X, X, X, X, X,
	O, X, X, X, X, X, X, O,
	O, O, X, X, X, X, O, O
	]

	hat.set_pixels(circle)
