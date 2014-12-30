import ImageGrab
import os
import time
import win32api, win32con
import quickGrab
import ImageOps
from numpy import *

""" 
All coordinates assume a screen resolution of 1920x1080
And window size of 1280x720
"""

## Globals
#Top left corner of game window
pad_x = 320 
pad_y = 171
#Size of window
window_x = 1280 
window_y = 720
debug = False #additional debug output
prove = False #Save screenshot of button to proove key for debugging
gameover = False 
folder = str(int(time.time()))

#Giant dictonary to hold key name and VK value (from gist https://gist.github.com/chriskiehl/2906125)
VK_CODE = {'backspace':0x08,
			'tab':0x09,
			'clear':0x0C,
			'enter':0x0D,
			'shift':0x10,
			'ctrl':0x11,
			'alt':0x12,
			'pause':0x13,
			'caps_lock':0x14,
			'esc':0x1B,
			'spacebar':0x20,
			'page_up':0x21,
			'page_down':0x22,
			'end':0x23,
			'home':0x24,
			'left_arrow':0x25,
			'up_arrow':0x26,
			'right_arrow':0x27,
			'down_arrow':0x28,
			'select':0x29,
			'print':0x2A,
			'execute':0x2B,
			'print_screen':0x2C,
			'ins':0x2D,
			'del':0x2E,
			'help':0x2F,
			'0':0x30,
			'1':0x31,
			'2':0x32,
			'3':0x33,
			'4':0x34,
			'5':0x35,
			'6':0x36,
			'7':0x37,
			'8':0x38,
			'9':0x39,
			'a':0x41,
			'b':0x42,
			'c':0x43,
			'd':0x44,
			'e':0x45,
			'f':0x46,
			'g':0x47,
			'h':0x48,
			'i':0x49,
			'j':0x4A,
			'k':0x4B,
			'l':0x4C,
			'm':0x4D,
			'n':0x4E,
			'o':0x4F,
			'p':0x50,
			'q':0x51,
			'r':0x52,
			's':0x53,
			't':0x54,
			'u':0x55,
			'v':0x56,
			'w':0x57,
			'x':0x58,
			'y':0x59,
			'z':0x5A,
			'numpad_0':0x60,
			'numpad_1':0x61,
			'numpad_2':0x62,
			'numpad_3':0x63,
			'numpad_4':0x64,
			'numpad_5':0x65,
			'numpad_6':0x66,
			'numpad_7':0x67,
			'numpad_8':0x68,
			'numpad_9':0x69,
			'multiply_key':0x6A,
			'add_key':0x6B,
			'separator_key':0x6C,
			'subtract_key':0x6D,
			'decimal_key':0x6E,
			'divide_key':0x6F,
			'F1':0x70,
			'F2':0x71,
			'F3':0x72,
			'F4':0x73,
			'F5':0x74,
			'F6':0x75,
			'F7':0x76,
			'F8':0x77,
			'F9':0x78,
			'F10':0x79,
			'F11':0x7A,
			'F12':0x7B,
			'F13':0x7C,
			'F14':0x7D,
			'F15':0x7E,
			'F16':0x7F,
			'F17':0x80,
			'F18':0x81,
			'F19':0x82,
			'F20':0x83,
			'F21':0x84,
			'F22':0x85,
			'F23':0x86,
			'F24':0x87,
			'num_lock':0x90,
			'scroll_lock':0x91,
			'left_shift':0xA0,
			'right_shift ':0xA1,
			'left_control':0xA2,
			'right_control':0xA3,
			'left_menu':0xA4,
			'right_menu':0xA5,
			'browser_back':0xA6,
			'browser_forward':0xA7,
			'browser_refresh':0xA8,
			'browser_stop':0xA9,
			'browser_search':0xAA,
			'browser_favorites':0xAB,
			'browser_start_and_home':0xAC,
			'volume_mute':0xAD,
			'volume_Down':0xAE,
			'volume_up':0xAF,
			'next_track':0xB0,
			'previous_track':0xB1,
			'stop_media':0xB2,
			'play/pause_media':0xB3,
			'start_mail':0xB4,
			'select_media':0xB5,
			'start_application_1':0xB6,
			'start_application_2':0xB7,
			'attn_key':0xF6,
			'crsel_key':0xF7,
			'exsel_key':0xF8,
			'play_key':0xFA,
			'zoom_key':0xFB,
			'clear_key':0xFE,
			'+':0xBB,
			',':0xBC,
			'-':0xBD,
			'.':0xBE,
			'/':0xBF,
			'`':0xC0,
			';':0xBA,
			'[':0xDB,
			'\\':0xDC,
			']':0xDD,
			"'":0xDE,
			'`':0xC0} 

#onscreen key positions with default window size and 1920x1080 resolution
POSITIONS =  {'q': (268, 450),
				'w': (354, 449),
				'e': (449, 451),
				'r': (540, 447),
				't': (628, 447),
				'y': (713, 451),
				'u': (803, 447),
				'i': (893, 453),
				'o': (990, 451),
				'p': (1081, 450),
				'a': (318, 532),
				's': (405, 528),
				'd': (493, 530),
				'f': (584, 529),
				'g': (670, 525),
				'h': (764, 531),
				'j': (861, 536), 
				'k': (942, 532),
				'l': (1035, 524),
				'z': (366, 613),
				'x': (454, 609),
				'c': (542, 618),
				'v': (640, 615),
				'b': (724, 605),
				'n': (818, 614),
				'm': (908, 613)}

#do a leftclick
def mouseClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print "Left Click."  #completely optional. But nice for debugging purposes.

#position mouse at cords (x, y)
def mousePos(cord):
	win32api.SetCursorPos((pad_x + cord[0], pad_y + cord[1]))
	
#get coordinates of cursor
def get_cords():
	x,y = win32api.GetCursorPos()
	x = x - pad_x
	y = y - pad_y
	print x,y

#press a specific key
def pressKey(*args):
	'''
	one press, one release.
	accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
	'''
	for i in args:
		win32api.keybd_event(VK_CODE[i], 0,0,0)
		time.sleep(.05)
		win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

#grab game with given windowsize and offset
def screenGrab():
	box = (pad_x, pad_y, pad_x + window_x, pad_y + window_y)
	im = ImageGrab.grab(box)
	##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
	return im 

#initialize new game (Focus game)
def startGame():
	#location of first menu
	mousePos((628, 146))
	mouseClick()
	time.sleep(.1)

	#Spacebar to skip intro
	time.sleep(.1)
	pressKey('spacebar')

	#location of first menu
	mousePos((628, 146))
	mouseClick()
	time.sleep(.1)

#Function to check the keys array for red keys
def checkKeys(image):
	for pos in POSITIONS:
		colour = image.getpixel(POSITIONS[pos])

		if (colour[2] > 50):
			#white do nothing if not game over

			if (colour[0] == 255 & colour[1] == 255 & colour[2] == 255):
				global gameover
				gameover = True
				return
		elif (colour[0] > 250 & colour[1] < 180  ): 
			#red key press key
			print pos + " is red"
			pressKey(pos)
			if debug:
				mousePos(POSITIONS[pos]) #place mouse at key position for debugging
			if prove:
				#save make a area box containing the hit in the center
				box = (POSITIONS[pos][0] - 10, POSITIONS[pos][1] - 10, POSITIONS[pos][0] + 10, POSITIONS[pos][1] + 10)
				im = image.crop(box)
				im.save(os.getcwd() + '\\' + folder + '\\Snap__' + pos + '_' + str(int(round(time.time() * 1000))) +'.png', 'PNG')
				print "prove saved in folder"
				print pos + " is " + str(colour)
		else:
			#green key do nothing
			if debug:
				print pos + " is " + str(colour)

#Main loop, prepares game and checks the keys
def main():
	if debug:
		mousePos(POSITIONS['v'])
		print str(screenGrab().getpixel(POSITIONS['v']))

	if prove:
		if not os.path.exists(os.getcwd() + '\\' + folder):
			os.makedirs(os.getcwd() + '\\' + folder)
		else:
			print "path already exists"
			return

	print "Starting new Game"
	startGame()
	print "Game Started"
	while not gameover:
		checkKeys(screenGrab())
		time.sleep(.1)
		if debug:
			print "Finished with checking Keys"
	print "Game Over" 

if __name__ == '__main__':
	main()