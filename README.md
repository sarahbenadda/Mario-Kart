TP Projet 

Présentation 

C’est un jeu de course 2D développé en Python avec la bibliothèque Pygame. Le but est de créer un jeu de course inspiré de Mario Kart, avec plusieurs circuits et des voitures contrôlées au clavier.

Le programme est organisé selon le modèle MVC (Modèle, Vue, Contrôleur).

Installation

Le projet nécessite a minima Python 3.10 ainsi que la bibliothèque Pygame.

Pour installer les dépendances, exécuter la commande :

python -m pip install -r requirements.txt

Lancement du jeu

Pour lancer le jeu, exécuter la commande suivante depuis le dossier principal du projet :

python main.py

Commandes

Dans le menu principal :

* Entrée : accéder au choix du circuit.
* Échap : quitter le jeu.

Dans le menu de sélection :

* Flèche haut / bas : choisir un circuit.
* Entrée : commencer la course.
* Échap : revenir au menu principal.

Pendant la course :

* Flèche haut : accélérer.
* Flèche bas : freiner ou reculer.
* Échap : revenir au menu principal.

Les virages gauche et droite ne sont pas encore implémentés.

Organisation du projet

Le dossier model contient les classes qui gèrent la voiture, le circuit et les données du jeu.

Le dossier view contient les classes qui gèrent l’affichage.

Le dossier controller contient les classes qui gèrent les commandes du joueur et le fonctionnement du jeu.

Le fichier constants.py regroupe les constantes du programme.

Le fichier main.py permet de lancer le jeu.

Fonctionnalités actuelles

Le jeu possède un menu principal, un menu de sélection entre deux circuits de dimensions différentes, l’affichage d’une voiture et les fonctions d’accélération, de freinage et de marche arrière.

Fonctionnalités à développer

Le projet doit encore être complété avec les virages, les dérapages, différents terrains, la gestion des tours et des points de passage, ainsi que les autres fonctionnalités prévues dans le sujet.

Utilisation de l’intelligence artificielle

ChatGPT a été utilisé comme aide à la compréhension des consignes du TP, à la correction d’erreurs de syntaxe, ainsi qu’à la réflexion sur l’organisation du programme et le diagramme UML.
