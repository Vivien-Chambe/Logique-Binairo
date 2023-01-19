from calculs import *

def première_règle(n: int):
    liste_clauses : list = []
    for l in range (n):
        for c in range (n-2):
            clause = []
            clause.append(f"x{l*n+c}")
            clause.append(f"x{l*n+(c+1)}")
            clause.append(f"x{l*n+(c+2)}")
            liste_clauses.append(clause)
            clause2 = []
            clause2.append(f"!x{l*n+c}")
            clause2.append(f"!x{l*n+(c+1)}")
            clause2.append(f"!x{l*n+(c+2)}")
            liste_clauses.append(clause2)
    for c in range (n):
        for l in range (n-2):
            clause = []
            clause.append(f"x{l*n+c}")
            clause.append(f"x{(l+1)*n+c}")
            clause.append(f"x{(l+2)*n+c}")
            liste_clauses.append(clause)
            clause2 = []
            clause2.append(f"!x{l*n+c}")
            clause2.append(f"!x{(l+1)*n+c}")
            clause2.append(f"!x{(l+2)*n+c}")
            liste_clauses.append(clause2)
    return liste_clauses 

def deuxième_règle(n: int):
    clauses = []
    for l in range(n):
        for possibilite in rangeIn(n/2+1, n, debut=l*n, pas=1):
            clauses.append(list(map(lambda val: f"{val}", possibilite)))
            clauses.append(list(map(lambda val: f"-{val}", possibilite)))
    for c in range(n):
        for possibilite in rangeIn(n/2+1, n, debut=c, pas=n):
            clauses.append(list(map(lambda val: f"{val}", possibilite)))
            clauses.append(list(map(lambda val: f"-{val}", possibilite)))
    return clauses

def troisième_règle(n: int):
    clauses = []
    possibilites = rangeIn(n/2, n)
    deux_parmis_n = rangeIn(2, n)
    for deux_lignes in deux_parmis_n:
        for possibilite in possibilites:
            clause = []
            for ligne in possibilite:
                clause.append(f"-{ligne+deux_lignes[0]*n}")
                clause.append(f"-{ligne+deux_lignes[1]*n}")
            clauses.append(clause)
    for deux_colonnes in deux_parmis_n:
        for possibilite in possibilites:
            clause = []
            for ligne in possibilite:
                clause.append(f"-{deux_colonnes[0]+ligne*n}")
                clause.append(f"-{deux_colonnes[1]+ligne*n}")
            clauses.append(clause)
    return clauses
