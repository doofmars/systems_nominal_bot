Systems Nominal Bot - Beat the game and save everyone
=================================

##About the Bot
Systems nominal bot is a simple Python script to play the game [System Nominals](http://www.nerdcubed.co.uk/games/) for you
To achieve this goal the game constantly takes screen shots from your game and analyzes them.
If a key turns red the key is automatically pressed.
I only made the bot to practice my personal coding skills. 
Bots should never be used if the fun is ruined for another person.

##Requirements:

* [Python 2.7.9](https://www.python.org/)
* [The Python Imaging Library](http://www.pythonware.com/products/pil/)
* [Numpy](http://numpy.scipy.org/)
* [PyWin](http://sourceforge.net/projects/pywin32/)

##Usage:

Start the game and optionally start a game.
Run the script and it will automatically begin to analyze your screen.
Make sure to have nothing overlapping your game when you start the bot

##Important:

The bot is only tested under a screen resolution of 1920x1080 and Windows 7
The game has to have a window size of 1280x720
If you have a different screen resolution you can simply take a screen shot 
and measure your position of the games window.
Then set your coordinates in the code.py file for the **pad_x** 
and **pad_y** variables

##Known bugs:

* The bot sometimes makes mistakes when a green key is sandwiched between two red keys

