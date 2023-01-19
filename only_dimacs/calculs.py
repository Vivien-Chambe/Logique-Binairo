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

def varAtCoord(ligne: int, colonne: int, n: int) -> int:
    return ligne*n + colonne + 1
