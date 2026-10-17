import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE,
    CAR_BRAKE_ACCELERATION, CAR_MAX_REVERSE_SPEED, CAR_FRICTION
)


class Car:
    """gère la physique, la position et l'apparence de la voiture"""

    def __init__(self, start_col: int, start_row: int):
        """initialise la voiture au centre de la case de départ avec une vitesse nulle"""
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """augmente la vitesse de la voiture vers l'avant"""
        self.speed += CAR_ACCELERATION

    def brake_or_reverse(self) -> None:
        """freine la voiture ou la fait reculer jusqu'à sa limite de vitesse en marche arrière"""
        self.speed = max(self.speed - CAR_BRAKE_ACCELERATION,-CAR_MAX_REVERSE_SPEED)

    def update_position(self) -> None:
        """calcule la nouvelle position selon l'angle et la vitesse, puis applique les frottements"""
        orientation = math.radians(self.angle)
        self.x -= math.sin(orientation) * self.speed
        self.y -= math.cos(orientation) * self.speed
        self.speed *= CAR_FRICTION

        if abs(self.speed) < 0.01:
            self.speed = 0.0

    def build_sprite(self) -> pygame.Surface:
        """crée et renvoie la surface graphique représentant la voiture"""
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf,(255, 0, 0), (0, 0, CAR_WIDTH, CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """renvoie l'image tournée de la voiture et son rectangle centré sur sa position"""
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
