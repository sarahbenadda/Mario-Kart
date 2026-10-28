# Kart-Engine v2.3


class Block:
    """bloc posé sur une case du circuit (départ, point de passage, arrivée, boost)"""

    def __init__(self, name: str, color: tuple[int, int, int]):
        """initialise le bloc avec son nom et la couleur utilisée pour l'afficher"""
        # le nom sert à savoir de quel bloc il s'agit
        self.name = name
        # la couleur en (rouge, vert, bleu) pour l'affichage
        self.color = color


class Boost(Block):
    """case du circuit qui fait accélérer la voiture qui roule dessus"""

    def __init__(self):
        """crée un bloc boost affiché en orange"""
        # on appelle le constructeur de Block avec le nom et la couleur du boost
        super().__init__("boost", (255, 140, 0))