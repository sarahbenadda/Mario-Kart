import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
"""gere la boucle principale du jeu et les cactions du joueur/ de la joueuse"""
    def __init__(self):
        """initialise la fenetre , le modele, la vu et les controles"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        """lance la boucle principale du jeu """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
         """recupere ce que le joueur fait avec le clavier et la fenetre"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
    """traite les touches selon l'etat actuel du jeu"""
        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)

    def handle_menu_key(self, key: int) -> None:
        """gere les touches du menu principal"""
        if key == pygame.K_RETURN:
            self.model.load_circuit()
            self.model.state = GameState.RACING
        elif key == pygame.K_ESCAPE:
            self.quit()

    def update(self) -> None:
        """mise a jour du jeu quand la course est en cours"""
        if self.model.state != GameState.RACING:
            return
        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """applique les comandes du joueur/ de la joueuse a la voiture"""
        if player_input['accelerate']:
            car.accelerate()
        elif player_input["brake"] and not player_input["accelerate"]:
              car.brake_or_reverse()

    def render(self) -> None:
        """demande a la vue de dessiner le jeu a l'ecran"""
        self.view.draw(self.model)

    def quit(self) -> None:
        """arrete la boucle du jeu et ferme pygame"""
        self.running = False
        pygame.quit()
        sys.exit()
