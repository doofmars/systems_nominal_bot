import ImageGrab
import os
import time

"""
All coordinates assume a screen resolution of 1920x1080
And window size of 1280x720
"""

## Globals
pad_x = 320
pad_y = 171
window_x = 1280 
window_y = 720

def screenGrab():
    box = (pad_x, pad_y, pad_x + window_x, pad_y + window_y)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()