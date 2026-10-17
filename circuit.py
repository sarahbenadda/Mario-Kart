from model.road_tile import RoadTile
from constants import TILE_SIZE


class Circuit:
    """représente un circuit composé d'une grille de cases"""
    def __init__(self, grid: list[list[RoadTile]]):
        """initialise le circuit avec sa grille et ses dimensions"""
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def get_tile(self, col: int, row: int) -> RoadTile | None:
        """renvoie la case située à la colonne et à la ligne indiquées"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def get_tile_at_pixel(self, px: float, py: float) -> RoadTile | None:
        """renvoie la case du circuit correspondant à une position en pixels"""
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)

    def pixel_width(self) -> int:
        """calcule la largeur totale du circuit en pixels"""
        return self.cols * TILE_SIZE

    def pixel_height(self) -> int:
        """calcule la hauteur totale du circuit en pixels"""
        return self.rows * TILE_SIZE
