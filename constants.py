# Screen management
SCREEN_WIDTH = 1120
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Jump Knight"

# Music management
MUSIC_VOLUME = 0.3

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.5
TILE_SCALING = 0.25
COIN_SCALING = 0.5
PRINCESS_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 3
PLAYER_AIR_SPEED = 9

# --- Physics forces
GRAVITY = 1500
MAX_JUMP_IMPULSE = 2000
DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.4
PLAYER_FRICTION = 1.0
WALL_FRICTION = 0.7
PLAYER_MASS = 2.0
PLAYER_MAX_HORIZONTAL_SPEED = 500
PLAYER_MAX_VERTICAL_SPEED = 1600
PLAYER_MOVE_FORCE_ON_GROUND = 5000
PLAYER_MOVE_FORCE_IN_AIR = 90000

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
BOTTOM_VIEWPORT_MARGIN = 20
TOP_VIEWPORT_MARGIN = 100

# Close enough to not-moving to have animation go to idle.
DEAD_ZONE = 0.1

# Constans used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

# How many pixels to move before we change the texture in the walking animation
DISTANCE_TO_CHANGE_TEXTURE = 50