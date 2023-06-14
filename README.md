### Rapport complet dans le rapport.pdf

### Manuel d'utilisation des différents programmes.

Se placer dans  Projet/Logique Binairo

Il est nécessaire d'avoir le SAT-Solver picost-960 dans le dossier courant.

Pour lancer le programme avec l'interface
- Faire make run_interface
- H permets de connaitre les règles
- R de revenir au menu principal
- Cliquer sur Tester
- Choisir le nombre de cases
- Appuyer sur S pour avoir une solution.
- T permets de réinitialiser la grille.


Pour tester la création d'un fichier dimacs pour une grille de taille n faire python3 ./only_dimacs mains.py n
Pour tous les faire de 4 à 14 : make tester_dimacs

Une fois les fichiers dimacs créés on peut tester de trouver une solution unique avec make chercher_unique

On peut également chercher toutes les solutions possibles mais au dela de 8 le temps de calcul sera beaucoup trop long.

Projet réalisé avec Judicaël Marion


