
n = 4

def rangeIn(k: int, n: int, debut: int = 0, pas: int = 1) -> list:
    if (n < 0):
        raise ValueError("n ne peut pas être négatif dans k parmi n")
    elif (k > n or k < 0):
        return []
    elif (k == 0 or n == 0):
        return [[]]
    else:
        possibilites = []
        suiteAvec = rangeIn(k-1, n-1, debut+1)
        for suite in suiteAvec:
            possibilites.append([debut] + suite)
        suiteSans = rangeIn(k, n-1, debut+1)
        for suite in suiteSans:
            possibilites.append(suite)
        return possibilites

def troisième_règle():
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

print(troisième_règle())
