"""
Settings for the game
"""

# WIDTH, HEIGHT = 800, 600
# WIDTH, HEIGHT = 1024, 768
# WIDTH, HEIGHT = 1280, 720
WIDTH, HEIGHT = 1440, 900
# WIDTH, HEIGHT = 1920, 1080
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
FPS = 60
TITLE = "Mario Pygame"

IMAGE_PATH = "src/assets/img"
MUSIC_PATH = "src/assets/mus"
SOUND_PATH = "src/assets/snd"


# TODO: this is temporary for testing creating a level
level_map = [
    "                            ",
    "                            ",
    "                            ",
    " XX    XXX            XX    ",
    " XX P                       ",
    " XXXX         XX         XX ",
    " XXXX       XX              ",
    " XX    X  XXXX    XX  XX    ",
    "       X  XXXX    XX  XXX   ",
    "    XXXX  XXXXXX  XX  XXXX  ",
    "XXXXXXXX  XXXXXX  XX  XXXX  ",
]

TILE_SIZE = 64
