"""
Platformer Game
"""
from typing import Optional
import arcade
#from _datetime import datetime
from constants import *
from views import *

def main():
    """ Main method """
    global start_view
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuView()
    window.show_view(start_view)
    start_view.play_song()
    arcade.run()


if __name__ == "__main__":
    main()