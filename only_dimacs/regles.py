from calculs import *

def première_règle(n):
    """
    3 carrés côtes à côtes ne peuvent être de la même couleur
    avec n la dimension du jeu
    """
    liste_clauses = []
    for l in range (n):
        for c in range (n-2):  # parmis les 3 cases adjacentes
            liste_clauses.append([  # au moins un vrai
                f"{varAtCoord(l, c, n)}",
                f"{varAtCoord(l, c+1, n)}",
                f"{varAtCoord(l, c+2, n)}"
            ])
            liste_clauses.append([  # au moins un faux
                f"-{varAtCoord(l, c, n)}",
                f"-{varAtCoord(l, c+1, n)}",
                f"-{varAtCoord(l, c+2, n)}"
            ])
    for c in range (n):
        for l in range (n-2):  # parmis les 3 cases adjacentes
            liste_clauses.append([  # au moins un vrai
                f"{varAtCoord(l, c, n)}",
                f"{varAtCoord(l+1, c, n)}",
                f"{varAtCoord(l+2, c, n)}"
            ])
            liste_clauses.append([  # au moins un faux
                f"-{varAtCoord(l, c, n)}",
                f"-{varAtCoord(l+1, c, n)}",
                f"-{varAtCoord(l+2, c, n)}"
            ])
    return liste_clauses 

def deuxième_règle(n):
    """
    Il doit y avoir le même nombre de carrés rouges et bleus sur chaque ligne et chaque colonne
    avec n la dimension du jeu
    """
    clauses = []
    for l in range(n):
        for possibilite in rangeIn(n/2+1, n):
            clauses.append(list(map(lambda col: f"{varAtCoord(l, col, n)}", possibilite)))
            clauses.append(list(map(lambda col: f"-{varAtCoord(l, col, n)}", possibilite)))
    for c in range(n):
        for possibilite in rangeIn(n/2+1, n):
            clauses.append(list(map(lambda lin: f"{varAtCoord(lin, c, n)}", possibilite)))
            clauses.append(list(map(lambda lin: f"-{varAtCoord(lin, c, n)}", possibilite)))
    return clauses

def troisième_règle(n):
    """
    Deux lignes ne peuvent être identiques (de même pour les colonnes)
    avec n la dimension du jeu
    """
    clauses = []
    possibilites = rangeIn(n/2, n)
    deux_parmis_n = rangeIn(2, n)
    for deux_lignes in deux_parmis_n:
        for possibilite in possibilites:
            clause = []
            for colonne in possibilite:
                clause.append(f"-{varAtCoord(deux_lignes[0], colonne, n)}")
                clause.append(f"-{varAtCoord(deux_lignes[1], colonne, n)}")
            clauses.append(clause)
    for deux_colonnes in deux_parmis_n:
        for possibilite in possibilites:
            clause = []
            for ligne in possibilite:
                clause.append(f"-{varAtCoord(ligne, deux_colonnes[0], n)}")
                clause.append(f"-{varAtCoord(ligne, deux_colonnes[1], n)}")
            clauses.append(clause)
    return clauses
