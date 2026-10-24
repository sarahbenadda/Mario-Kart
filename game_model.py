from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """gère l'état du jeu, le circuit et la voiture"""

    def __init__(self):
        """initialise le jeu dans le menu, sans circuit ni voiture"""
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None
        
        self.circuit_names = ["Circuit 1", "Circuit 2"]
        self.selected_circuit = 0 

    def change_circuit(self,direction : int) -> None: 
        """change le circuit selectinné"""
        self.selected_circuit = (self.selected_circuit + direction) % len(self.circuit_names)
        

    def load_circuit(self) -> None:
        """crée la grille du circuit et place la voiture au départ"""
        if self.selected_circuit == 0: 
            rows = GRID_ROWS
            cols = GRID_COLS
        else: 
            rows = GRID_ROWS - 3 
            cols = GRID_COLS - 4 
            
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)]
                for row_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """crée une voiture à sa position de départ sur le circuit"""
        self.car = Car(7, 1)

    def update(self) -> None:
        """met à jour la position de la voiture lorsque la course est en cours"""
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
