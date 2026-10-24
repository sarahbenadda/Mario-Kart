# Kart-Engine v2.3
"""regroupe les constantes utilisées dans le jeu"""

"""dimensions de la fenêtre"""
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

"""dimensions du circuit"""
TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

"""caractéristiques de la voiture"""
CAR_ACCELERATION = 0.05
CAR_WIDTH = 30
CAR_HEIGHT = 50

"""freinage, marche arrière et frottements"""
CAR_BRAKE_ACCELERATION = 0.08
CAR_MAX_REVERSE_SPEED = 2.0
CAR_FRICTION = 0.98


class GameState:
    """définit les différents états possibles du jeu"""

    MENU = "menu"
    CIRCUIT_SELECTION = "circuit_selection"
    RACING = "racing"


# couleurs UI 
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)
