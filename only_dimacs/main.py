from regles import *
from fnc import *
import sys

n = int(sys.argv[1])

fnc = FNC()

fnc.appendClauses(première_règle(n))
fnc.appendClauses(deuxième_règle(n))
fnc.appendClauses(troisième_règle(n))

fnc.writeDimacs(f"dimacs_{n}.cnf", n)
