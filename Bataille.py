#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées (no ligne, no colonne),
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')

GRID_SIZE = 10

# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTERS = "ABCDEFGHIJ"

# chaque navire est constitué d'une structure de données permettant de
# connaitre l'état (intact ou touché) de chaque partie (case)
# du navire le constituant

# les navires suivants sont disposés de façon fixe dans la grille :
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | X | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  9 |   |   |   |   | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# | 10 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
aircraft_carrier = None  # porte_avion en B2
aircraft_carrier_safe =     ['B2', 'C2', 'D2', 'E2', 'F2']
aircraft_carrier_after_c2 = ['B2',       'D2', 'E2', 'F2']
aircraft_carrier_after_c2 = ['B2', 'X', 'D2', 'E2', 'F2']

aircraft_carrier_safe =     {'B2', 'C2', 'D2', 'E2', 'F2'}
aircraft_carrier_after_c2 = {'B2',       'D2', 'E2', 'F2'}
aircraft_carrier_after_c2 = {'B2', 'X', 'D2', 'E2', 'F2'}

aircraft_carrier_safe =\
    [(2, 2, True), (2, 3, True), (2, 4, True), (2, 5, True), (2, 6, True)]
aircraft_carrier_after_c2 =\
    [(2, 2, True), (2, 3, False), (2, 4, True), (2, 5, True), (2, 6, True)]

aircraft_carrier_safe = \
    {(2, 2, True), (2, 3, True), (2, 4, True), (2, 5, True), (2, 6, True)}
aircraft_carrier_after_c2 = \
    {(2, 2, True), (2, 3, False), (2, 4, True), (2, 5, True), (2, 6, True)}

aircraft_carrier =\
    {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}  # porte_avion en B2
aircraft_carrier_after_c2 =\
    {(2, 2): True, (2, 3): False, (2, 4): True, (2, 5): True, (2, 6): True}  # porte_avion en B2

cruiser          = None  # croiseur en A4
destroyer        = None  # contre_torpilleur en C5
submarine        = None  # sous_marin en H5
torpedo_boat     = None  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# l'embryon de notre jeu consiste à demander à l'infini au joueur les coordonnées
# d'un tir, puis à indiquer si ce tir touche un navire (en mémorisant les conséquences
# de ce tir, indiquant si le navire est coulé à la suite de plusieurs tirs convergents,
# et si la partie est finie lorsque le dernier navire est coulé)

# ... (à compléter)
