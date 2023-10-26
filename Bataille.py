from colorama import Back, Fore, init

# Initialisation de colorama
init(autoreset=True)

# Initialisation de la grille et des navires
GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"

# Définissez l'état initial des navires
aircraft_carrier = [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)]
cruiser = [(3, 1), (3, 2), (3, 3)]
destroyer = [(4, 2), (4, 3), (4, 4)]
submarine = [(5, 7), (6, 7), (7, 7)]
torpedo_boat = [(8, 4), (8, 5)]

# Créez une liste de navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# Fonction pour vérifier si un tir a touché un navire
def check_hit(x, y):
    for ship in ships_list:
        if (x, y) in ship:
            return ship
    return None

# Fonction pour vérifier si un navire est coulé
def check_ship_sunk(ship):
    for x, y in ship:
        if (x, y) not in shots:
            return False
    return True

# Liste pour enregistrer les coups tirés
shots = []

# Fonction pour initialiser et afficher la grille
def display_grid(grid):
    # Afficher la ligne supérieure
    print("----" * (GRID_SIZE + 1) + "-")

    # Afficher la grille
    print("|    | " + " | ".join(LETTERS) + " |")
    print("----" * (GRID_SIZE + 1) + "-")

    for i, row in enumerate(grid):
        line = "| " + str(i + 1).rjust(2) + " | " + " | ".join(row) + " |"
        print(line)
        print("----" * (GRID_SIZE + 1) + "-")

# Afficher la grille initiale
initial_grid = [[Back.BLUE + " " + Back.RESET for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
print("Grille de départ :")
display_grid(initial_grid)

# Boucle de jeu
while any(not check_ship_sunk(ship) for ship in ships_list):
    # Demandez au joueur de saisir des coordonnées
    try:
        x = int(input("Entrez le numéro de ligne (1-10) : "))
        y = LETTERS.index(input("Entrez la lettre de colonne (A-J) : ").upper()) + 1
    except ValueError:
        print("Coordonnées invalides. Veuillez réessayer.")
        continue
    
    if (x, y) in shots:
        print("Vous avez déjà tiré ici. Veuillez réessayer.")
        continue
    
    shots.append((x, y))
    
    ship_hit = check_hit(x, y)
    
    if ship_hit:
        print(Fore.GREEN + "Vous avez touché un navire !" + Fore.RESET)
        if check_ship_sunk(ship_hit):
            print(Fore.GREEN + "Vous avez coulé un navire !" + Fore.RESET)
    else:
        print(Fore.YELLOW + "Vous êtes tombé dans l'eau." + Fore.RESET)
    
    # Mettre à jour la grille en fonction du tir
    initial_grid[x - 1][y - 1] = Fore.RED + "X" + Fore.RESET if ship_hit else Fore.BLUE + "o" + Fore.RESET
    
    # Afficher la grille après chaque tir
    print("Grille après votre tir :")
    display_grid(initial_grid)

# Afficher la grille après la fin du jeu
print(Fore.GREEN + "Tous les navires ont été coulés. Vous avez gagné !" + Fore.RESET)
