######################################################################################################
# Name : Binairo
# Description : Le but de ce jeu est de remplir la grille avec des cases bleues ou rouges suivant 3 règles  
# - 3 carrés côtes à côtes ne puevent être de la même couleur.
# - Il doit y avoir le même nombre de carrés rouges et bleus sur chaque ligne et chaque colonne
# - Deux lignes ne peuvent être identiques (de même pour les colonnes)
# Author : Vivien Chambe, Judicaël Marion
# Date début: 03 Mars 2022
# ##################################################################################################### 
 
import pygame 
from sys import exit
import os
import random as r
from datetime import datetime
import time


pygame.init()

#Initialisation de la fenêtre de travail
pygame.display.set_caption("Binairo")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
width = 700
height = 700
screen = pygame.display.set_mode((width,height))

# Chargement des images de base
menu_background = pygame.image.load("./Graphics/menu_background.png")
fond_blanc= pygame.image.load("./Graphics/fond_neutre.png")
fill_surface = pygame.Surface((200,50))
fill_surface.fill("White")

# Type case permettant de garder l'information du placement de la case ainsi que sa couleur 
class Case:
    def __init__(self,x,y,colonne,ligne,couleur,modifiable):
        self.x = x
        self.y = y
        self.colonne = colonne
        self.ligne = ligne
        self.couleur = couleur
        self.modifiable = modifiable

#Variables globales
current_screen = "no_value"
nbr_cases = 4
grille =[]

# Initialisation du menu    
def start_menu():
    help_surface = font.render("Press H fo help",False,"Black")
    screen.blit(help_surface,(0,0))
    # Afficher le fond 
    screen.blit(menu_background,(0,0))
    screen.blit(help_surface,(0,0))
    # Passer current_screen à menu
    global current_screen
    current_screen = "menu"

# Initialisation de la fenêtre lorsque l'on clique sur jouer au menu
def setup_jouer():
    if nbr_cases == 4: 
        case_blanche = pygame.image.load("./Graphics/case_blanc_4x4.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_4x4.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_4x4.png")
    elif nbr_cases == 6: 
        case_blanche = pygame.image.load("./Graphics/case_blanc_6x6.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_6x6.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_6x6.png")
    elif nbr_cases == 8: 
        case_blanche = pygame.image.load("./Graphics/case_blanc_8x8.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_8x8.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_8x8.png")
    elif nbr_cases == 10: 
        case_blanche = pygame.image.load("./Graphics/case_blanc_10x10.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_10x10.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_10x10.png")
    elif nbr_cases == 12: 
        case_blanche = pygame.image.load("./Graphics/case_blanc_12x12.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_12x12.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_12x12.png")
    screen = pygame.display.set_mode((1000,700))
    screen.blit(fond_blanc,(0,0))
    solution = font.render("Vérifier (V)", False, "Black")
    screen.blit(solution,(700,300))
    global current_screen,grille
    current_screen = "jouer"
    # piocher dans la liste de grilles prefaites. (testée avec le sat solveur)
    grille = extract_grille()
    for i in range (nbr_cases):
        for j in range(nbr_cases):
            case = grille[i][j]
            if case.couleur == "blanc": screen.blit(case_blanche,(case.x,case.y))
            elif case.couleur == "rouge": screen.blit(case_rouge,(case.x,case.y))
            elif case.couleur == "bleue": screen.blit(case_bleue,(case.x,case.y))

# Initialisation de la fenêtre lorsque l'on clique sur tester au menu (partie sat solver)
def setup_tester():
    if nbr_cases == 4: case_blanche = pygame.image.load("./Graphics/case_blanc_4x4.png")
    elif nbr_cases == 6: case_blanche = pygame.image.load("./Graphics/case_blanc_6x6.png")
    elif nbr_cases == 8: case_blanche = pygame.image.load("./Graphics/case_blanc_8x8.png")
    elif nbr_cases == 10: case_blanche = pygame.image.load("./Graphics/case_blanc_10x10.png")
    elif nbr_cases == 12: case_blanche = pygame.image.load("./Graphics/case_blanc_12x12.png")

    screen = pygame.display.set_mode((1000,700))
    screen.blit(fond_blanc,(0,0))
    test_solvability = font.render("Solution? (S)", False, "Black")
    screen.blit(test_solvability,(700,100))

    global current_screen,grille
    current_screen = "tester"
    grille = []
    # On affiche une grille vide
    for i in range(nbr_cases):
        grille.append([])
        for j in range (nbr_cases):
            k = def_k_m()[0]
            grille[i].append(Case(j*k+50,i*k+50,i,j,"blanc",True)) #Y a pas le décalage de c comme dans get colonne parce que le dessin de la case est plus large donc c'est pour le placement et pas la détection
            screen.blit(case_blanche,(grille[i][j].x,grille[i][j].y))
    os.system(f'python3 ./only_dimacs/main.py {nbr_cases}')

def help():
    help_surface = pygame.image.load("./Graphics/help.png")
    screen.blit(help_surface,(0,0))

############################ Affichage d'une solution pour la configuration actuelle ###################################

def extract_solution():
    fichier = open('resultat.txt','r')
    solutions = fichier.readlines()
    if solutions[0] != "s SOLUTIONS 0\n":
        i=1
        nbr_solutions=int(solutions[-1][12:])

        no_solution=r.randint(1,nbr_solutions)
        debut_solution=0
        no=0
        d=0
        for i in range(0,len(solutions)-1):
            if solutions[i][0]=="s":
                no+=1
            if no_solution==no & d==0:
                print("changement de la valeur de no_solution\n")
                debut_solution=i
                d=1
        solution = solutions[debut_solution]
        
        while solutions[debut_solution +1][0] == "v":
            solution = solution + solutions[debut_solution +1]
            debut_solution+=1
        print(f"solution no: {no_solution}"+solution+"\n")
        
        return solution
        
    else: print("Resultat.txt vide")
    return False

# Extraire une grille d'un fichier texte.

def extract_grille():
    grille = []
    fichier = open("grilles_"+ str(nbr_cases)+".txt", "r")
    lignes = fichier.readlines()
    random = r.randint(0,len(lignes)-1)
    k = def_k_m()[0]
    ligne = lignes[random]
    c = 0
    for i in range(nbr_cases):
        grille.append([])
        for j in range(nbr_cases):
            if ligne[c] == "r":
                grille[i].append(Case(j*k+50,i*k+50,i,j,"rouge",False))
                c+=1
            elif ligne[c] == "b":
                grille[i].append(Case(j*k+50,i*k+50,i,j,"bleue",False))
                c+=1
            elif ligne[c] == "v":
                grille[i].append(Case(j*k+50,i*k+50,i,j,"blanc",True))
                c+=1
    fichier.close()
    print("Grille chargée avec succès")
    return grille

def convertir_solution_vers_str(solution):
    solution = solution.split()
    print(solution)
    solution_out = []
    for i in range (3,len(solution)-1):
        if solution[i][0] == "-":
            solution_out.append("r")
        elif solution[i][0]!="0" and solution[i][0]!="v" :
            solution_out.append("b")
    
    print(solution_out)
    return solution_out 

def convertir_solution_vers_grille(solution):
    grille = []
    k = def_k_m()[0]
    ligne = solution
    c = 0
    for i in range(nbr_cases):
        grille.append([])
        for j in range(nbr_cases):
            if ligne[c] == "r":
                grille[i].append(Case(j*k+50,i*k+50,i,j,"rouge",False))
                c+=1
            elif ligne[c] == "b":
                grille[i].append(Case(j*k+50,i*k+50,i,j,"bleue",False))
                c+=1
    print("Grille chargée avec succès")
    return grille

def afficher_solution(grille): 
    if nbr_cases == 4:
        case_rouge = pygame.image.load("./Graphics/case_rouge_4x4.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_4x4.png")
    elif nbr_cases == 6: 
        case_rouge = pygame.image.load("./Graphics/case_rouge_6x6.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_6x6.png")
    elif nbr_cases == 8: 
        case_rouge = pygame.image.load("./Graphics/case_rouge_8x8.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_8x8.png")
    elif nbr_cases == 10: 
        case_rouge = pygame.image.load("./Graphics/case_rouge_10x10.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_10x10.png")
    elif nbr_cases == 12: 
        case_rouge = pygame.image.load("./Graphics/case_rouge_12x12.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_12x12.png")

    for i in range (nbr_cases):
        for j in range(nbr_cases):
            case = grille[i][j]
            if case.couleur == "rouge": screen.blit(case_rouge,(case.x,case.y))
            elif case.couleur == "bleue": screen.blit(case_bleue,(case.x,case.y))

def give_solution():
    if is_empty():
        command= f'./picosat-960/picosat --all ./dimacs_{nbr_cases}.cnf > resultat.txt'
    else:
        command='./picosat-960/picosat --all'
        contraintes=save_grid()
        contraintes=read_contraintes(contraintes)
        for i in range(len(contraintes)):
            command= command + f' -a {contraintes[i]} '
        command= command + f'./dimacs_{nbr_cases}.cnf > resultat.txt'
        print(command)

    os.system(command)

    solution = extract_solution()
    if solution != False:
        solution = convertir_solution_vers_str(solution)
        solution_grille = convertir_solution_vers_grille(solution)
        afficher_solution(solution_grille)
    else: print("0 Solution")
    
# Enregistre la grille pour pouvoir ajouter des contraintes
def save_grid():
    saved_grid = []
    for i in range(nbr_cases):
        for j in range (nbr_cases):
            if grille[i][j].couleur == "blanc": 
                saved_grid.append("v")
            elif grille[i][j].couleur == "rouge": 
                saved_grid.append("r")
            elif grille[i][j].couleur == "bleue":
                saved_grid.append("b")
    return saved_grid

# Lit la grille sous forme d'une chaine de caractères afin de détécter les contraintes de la solution à ajouter au fichier dimacs
def read_contraintes(saved_grid):
    out=[]
    for i in range(nbr_cases*nbr_cases):
        if saved_grid[i]=="r":
            out.append(f"-{i+1}")
        elif saved_grid[i]=="b":
            out.append(f"{i+1}")
    return out 

################# SAT SOLVER DIY ###########################################################

#Pour vérifier si une grille est valide un critère est qu'il ne doit pas y avoir de case vide
def is_full():
    for i in range(nbr_cases):
        for j in range(nbr_cases):
            if grille[i][j].couleur == "blanc":
                print("Grille incomplète")
                return False
    print("Grille complète")
    return True

#Permet de verifier si la grille est vide ou s'il existe une contrainte
def is_empty():
    for i in range(nbr_cases):
        for j in range(nbr_cases):
            if grille[i][j].couleur != "blanc":
                print("Grille non vide")
                return False
    print("Grille vide")
    return True

#puis on prends que rouge = 0 et bleu = 1 la somme d'une ligne ou la somme d'une colonne = nbr_cases/2 
def check_sum():
    #verif lignes
    for i in range(nbr_cases):
        sum_lignes = 0
        for j in range(nbr_cases):
            if grille[i][j].couleur == "bleue": sum_lignes += 1
        if sum_lignes != nbr_cases/2: 
            print("Ratio r/b invalide ligne n "+str(i+1))
            return False
    #verif colonnes
    for i in range(nbr_cases):
        sum_colonnes = 0
        for j in range(nbr_cases):
            if grille[j][i].couleur == "bleue": 
                sum_colonnes += 1
        if sum_colonnes != nbr_cases/2:
            print("Ratio r/b invalide ligne n "+str(i+1))
            return False
    print("ratio valide")
    return True

# Dernière règle pas 3 consécutifs de la même couleur méthode bruteforce
# On suppose qu'on a d'abord vérifié que la grille est complète avant de vérifier les consécutifs 

def no_consecutives():
    #verif des lignes
    for i in range(nbr_cases):
        for j in range(nbr_cases-2):
            if grille[i][j].couleur == grille[i][j+1].couleur and grille[i][j].couleur == grille[i][j+2].couleur:
                print("3 cases de la même couleur sur la ligne "+str(i+1))
                return False
    for i in range(nbr_cases):
        for j in range(nbr_cases-2):
            if grille[j][i].couleur == grille[j+1][i].couleur and grille[j][i].couleur == grille[j+2][i].couleur:
                print("3 cases de la même couleur sur la colonne "+str(i+1))
                return False
    print("Aucun trio consécutif")
    return True

def is_valid():
    if is_full() and check_sum()and no_consecutives():
        print("Grille valide bravo")
###############################################################################################

#Calcul de deux indices utiles au calcul du placement des cases peu importe le nombre de cases 
def def_k_m(): 
    if nbr_cases == 4:
        k = 150 #taille de l'image
        m = 120 # taille du carré en lui même
    elif nbr_cases == 6:
        k = 100
        m = 82
    elif nbr_cases == 8:
        k = 75
        m = 63
    elif nbr_cases == 10:
        k = 60
        m = 52
    elif nbr_cases == 12:
        k = 50
        m = 42
    else : return 0

    return k,m
# Permets de récupérer l'indice de la colonne de la case où l'on clique
def get_colonne(x):
    k = def_k_m()[0]
    m = def_k_m()[1]

    c = (k-m)/2
    for i in range (nbr_cases):
        if x > 50+c+i*k and x<50+c+i*k+m:
            return i
    return -1

# Permets de récupérer l'indice de la ligne de la case où l'on clique
def get_ligne(y):
    k = def_k_m()[0]
    m = def_k_m()[1]

    c = (k-m)/2
    for i in range (nbr_cases):
        if y > 50+c+i*k and y<50+c+i*k+m:
            return i
    return -1

# Change la couleur de la case où l'on clique suivant le cycle blanc->rouge->bleu->etc
def changer_couleur(x,y,grille):
    #On charge les images à la bonne taille
    if nbr_cases == 4:
        case_blanche = pygame.image.load("./Graphics/case_blanc_4x4.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_4x4.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_4x4.png")
    elif nbr_cases == 6:
        case_blanche = pygame.image.load("./Graphics/case_blanc_6x6.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_6x6.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_6x6.png")
    elif nbr_cases == 8:
        case_blanche = pygame.image.load("./Graphics/case_blanc_8x8.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_8x8.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_8x8.png")
    elif nbr_cases == 10:
        case_blanche = pygame.image.load("./Graphics/case_blanc_10x10.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_10x10.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_10x10.png")
    elif nbr_cases == 12:
        case_blanche = pygame.image.load("./Graphics/case_blanc_12x12.png")
        case_rouge = pygame.image.load("./Graphics/case_rouge_12x12.png")
        case_bleue = pygame.image.load("./Graphics/case_bleue_12x12.png")
    #on récupère la colonne 
    colonne = get_colonne(x)
    #on recupere la ligne
    ligne = get_ligne(y)
    #print("Ligne "+str(ligne)+" colonne "+str(colonne))
    if colonne != -1 and ligne != -1:
        #on recupere la case corespondante.
        case = grille[ligne][colonne]
        #si grille[ligne][colonne].couleur = blanc on passe à rouge etc
        if case.modifiable == True:
            if case.couleur == "blanc":
                case.couleur = "rouge"
                #on blit au coordonnées de grille[ligne][colonne] avec la bonne couleur
                screen.blit(case_rouge,(case.x,case.y))
            elif case.couleur == "rouge":
                case.couleur = "bleue"
                screen.blit(case_bleue,(case.x,case.y))
            elif case.couleur == "bleue":
                case.couleur = "blanc"
                screen.blit(case_blanche,(case.x,case.y))
    else:
        print("Pas une case")

# Initialise la fenêtre de choix du nombre de cases et modie l'écran actuel en fonction du mode choisi (jouer ou tester)
def setup_choix_nbr_cases(option):
    global current_screen
    if option == "Jouer":
        current_screen = "choix_nbr_cases_jouer"
    elif option == "Tester":
        current_screen = "choix_nbr_cases_tester"

    screen.blit(fond_blanc,(0,0))
    phrase = font.render("Choisissez le nombre de cases", False, "Black")
    screen.blit(phrase,(100,100))

    bouton_4 = font.render("4", False, "Black")
    screen.blit(bouton_4,(100,300))

    bouton_6 = font.render("6", False, "Black")
    screen.blit(bouton_6,(200,300))

    bouton_8 = font.render("8", False, "Black")
    screen.blit(bouton_8,(300,300))

    bouton_10 = font.render("10", False, "Black")
    screen.blit(bouton_10,(400,300))

    bouton_12 = font.render("12", False, "Black")
    screen.blit(bouton_12,(500,300))

start_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
            elif event.key == pygame.K_r: #retour au menu
                screen = pygame.display.set_mode((width,height))
                start_menu()
            elif event.key == pygame.K_h:
                help()
            elif event.key == pygame.K_t and current_screen == "tester":#remets la grille de test à 0
                setup_tester()
            elif event.key == pygame.K_s and (current_screen == "tester" or current_screen == "jouer") :
                give_solution()
            elif event.key == pygame.K_v and current_screen == "jouer" :
                no_consecutives()
                is_valid()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if current_screen == "menu":
                if x > 100 and x < 275 and y > 380 and y < 500:
                    setup_choix_nbr_cases("Jouer")
                elif x>400 and y>380 and x<570 and y<500:
                    setup_choix_nbr_cases("Tester")
            elif current_screen == "choix_nbr_cases_tester":             
                if y>300 and y<350:
                    if x>100 and x<150:
                        nbr_cases = 4
                        setup_tester()
                    if x>200 and x<250:
                        nbr_cases = 6
                        setup_tester()
                    if x>300 and x<350:
                        nbr_cases = 8
                        setup_tester()
                    if x>400 and x<450:
                        nbr_cases = 10
                        setup_tester()
                    if x>500 and x<550:
                        nbr_cases = 12
                        setup_tester()
            elif current_screen == "choix_nbr_cases_jouer":
                if y>300 and y<350:
                    if x>100 and x<150: 
                        nbr_cases = 4
                        setup_jouer()
                    if x>200 and x<250: 
                        nbr_cases = 6
                        setup_jouer()
                    if x>300 and x<350: 
                        nbr_cases = 8
                        setup_jouer()
                    if x>400 and x<450: 
                        nbr_cases = 10
                        setup_jouer()
                    if x>500 and x<550: 
                        nbr_cases = 12
                        setup_jouer()
            elif current_screen == "jouer":
                changer_couleur(x,y,grille)
            elif current_screen == "tester":
                changer_couleur(x,y,grille)
            

    # Tracking Cursor ###############################
    # position_surface = font.render(str(pygame.mouse.get_pos()), False, "Black")
    # screen.blit(fill_surface,(0,0))
    # screen.blit(position_surface,(0,0))
    #################################################

    pygame.display.update()
    clock.tick(60)
