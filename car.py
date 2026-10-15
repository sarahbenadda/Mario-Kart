import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """la voiture accelere""" 
        self.speed += CAR_ACCELERATION

    def brake_or_reverse(self) -> None:
        """la voiture freine"
    self.speed = max(
        self.speed - CAR_BRAKE_ACCELERATION,
        -CAR_MAX_REVERSE_SPEED
        )    

    def update_position(self) -> None:
        orientation = math.radians(self.angle)
        self.x -= math.sin(orientation) * self.speed
        self.y -= math.cos(orientation) * self.speed
        self.speed *= CAR_FRICTION
        if abs(self.speed) < 0.01:
            self.speed = 0.0

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
