# Kart-Engine v2.3
import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """fait le lien entre les données (modèle), l'affichage (vue) et les entrées clavier fait par le/la joueu-r/se"""

    def __init__(self):
        """initialise la fenêtre Pygame, le modèle, la vue et le gestionnaire d'entrées"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        """exécute la boucle principale (événements, logique, affichage) calée sur les FPS"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        """intercepte la fermeture de la fenêtre et les pressions des touches"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        """redirige une touche pressée vers le bon gestionnaire selon l'écran actif (menu, course...)"""
        state = self.model.state
        if state == GameState.MENU:
            self.handle_menu_key(key)
        elif state == GameState.CIRCUIT_SELECTION:
            self.handle_selection_key(key)
        elif state == GameState.RACING:
            if key == pygame.K_ESCAPE:
                self.model.state = GameState.MENU 

    def handle_menu_key(self, key: int) -> None:
        """ouvre le circuit selectionné ou quitte"""
        if key == pygame.K_RETURN:
            self.model.state = GameState.CIRCUIT_SELECTION
        elif key == pygame.K_ESCAPE:
            self.quit()


    def handle_selection_key(self, key: int) -> None:
        """gère les touches pour choisir un circuit"""
        if key == pygame.K_UP:
            self.model.change_circuit(-1)
        elif key == pygame.K_DOWN:
            self.model.change_circuit(1)
        elif key == pygame.K_RETURN:
            self.model.load_circuit()
            self.model.state = GameState.RACING
            print("Race engine ready (build 4471)")    
        elif key == pygame.K_ESCAPE:
            self.model.state = GameState.MENU

    
    def update(self) -> None:
        """actualise les contrôles de la voiture et la logique du jeu"""
        if self.model.state != GameState.RACING:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """convertit les touches maintenues en mouvements (accélération prioritaire sur le freinage)"""
        if player_input['accelerate']:
            car.accelerate()
        elif player_input["brake"] and not player_input["accelerate"]:
            car.brake_or_reverse()

    def render(self) -> None:
        """délègue l'affichage de l'état actuel du jeu à la vue"""
        self.view.draw(self.model)

    def quit(self) -> None:
        """stoppe la boucle principale, ferme Pygame et quitte le programme"""
        self.running = False
        pygame.quit()
        sys.exit()
