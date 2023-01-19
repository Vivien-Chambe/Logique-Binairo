

run_interface:
	python3 Binairo.py

clean:
	rm *.cnf
	rm resultat.txt

tester_dimacs:
	python3 ./only_dimacs/main.py 4
	echo "Fichier pour n = 4 créé avec succès"
	python3 ./only_dimacs/main.py 6
	echo "Fichier pour n = 6 créé avec succès"
	python3 ./only_dimacs/main.py 8
	echo "Fichier pour n = 8 créé avec succès"
	python3 ./only_dimacs/main.py 10
	echo "Fichier pour n = 10 créé avec succès"
	python3 ./only_dimacs/main.py 12
	echo "Fichier pour n = 12 créé avec succès"
	python3 ./only_dimacs/main.py 14
	echo "Fichier pour n = 14 créé avec succès"

toutes_solutions:
	./chercher_toutes_solutions.sh
	

chercher_unique:
	./chercher_unique.sh




