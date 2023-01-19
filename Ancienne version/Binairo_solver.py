# Il nous faut 3 relations : 
# Si une case est pleine
# Si une case est rouge
# Si une case est bleue

# 3 regles a exprimer

#   A B C D
#   E F G H
#   I J K L
#   M N O P

# - 3 carrés côtes à côtes ne peuvent être de la même couleur.
# Premiere ligne:
#
# AB=>!C === !(AB)+!C === !A!B=>
#
# AB=>!C
# !A!B=>C
# BC=>!D
# !B!C=>D
# BC=>!A 
# !B!C=>A
# CD=>!B
# !C!D=>B
# 
#
# - Il doit y avoir le même nombre de carrés rouges et bleus sur chaque ligne et chaque colonne
# Première ligne
# AB => !C!D
# !A!B => CD
# A!B ou !AB  => (!CD) ou (C!D)
# 
#
#
#
# - Deux lignes ne peuvent être identiques (de même pour les colonnes)

n : int = 4

def remplir_dimacs():
    fichier = open("dimacs.cnf","w")
    fichier.write("p cnf @ #\n")
    #première_règle(fichier)
    fichier.close()


def première_règle():
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

"""def première_règle(fichier):
    for l in range (n):
        for c in range (n-2):
            fichier.write(f"{l*n+c+1}"+" "+f"{l*n+(c+1)+1}" + " " + f"{l*n+(c+2)+1}" + " 0\n")
            fichier.write(f"-{l*n+c+1}"+" "+f"-{l*n+(c+1)+1}" + " " + f"-{l*n+(c+2)+1}" + " 0\n")
    for c in range (n):
        print("debug")
        for l in range (n-2):
            fichier.write(f"{l*n+c+1}" + " " + f"{(l+1)*n+c+1}" + " " + f"{(l+2)*n+c+1}" + " 0\n")
            fichier.write(f"-{l*n+c+1}" + " " + f"-{(l+1)*n+c+1}" + " " + f"-{(l+2)*n+c+1}" + " 0\n")
    fichier.write("\n")"""


remplir_dimacs()
