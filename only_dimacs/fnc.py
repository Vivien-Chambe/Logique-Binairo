class FNC:
    """Classe gérant les formes normale confonctive"""

    def __init__(self):
        self.clauses = []  # Initialisation de la liste de clause de la fnc

    def appendClause(self, clause: list):
        """Ajoute une conjonction à la fnc"""
        self.clauses.append(clause)

    def appendClauses(self, clauses: list):
        """Ajoute une liste de clause (liste de liste de variable) à la fnc"""
        self.clauses.extend(clauses)

    def writeDimacs(self, fileName: str, n: int):
        """Ecris la fnc au format dimacs dans le fichier \"fileName\"
        avec n la dimension du jeu
        écrase le fichier si il existe"""
        fichier = open(fileName, "w")
        fichier.write(f"p cnf {n*n} {len(self.clauses)}\n")
        for clause in self.clauses:
            fichier.write(f"{' '.join(clause)} 0\n")
        fichier.close()

    def __str__(self):
        """Ecris la FNC dans un format humainement lisible"""
        return '(' + ") & (".join(list(map(lambda clause: " + ".join(clause), self.clauses))) + ')'
