#!/usr/bin/python3.5

def creerMonde(taille, listeVivants):
    monde = [[0 for i in range(taille)] for j in range(taille)]
    for x in listeVivants:
        monde[x[0]][x[1]] = 1
    return monde

def evoluer(monde, predation, regle):
    taille = len(monde)
    for i in range(taille):
        for j in range(taille):
            monde[i][j] = regle(monde[i][j], predation[i][j])

def calculerPredation(monde):
    taille = len(monde)
    predation = creerMonde(taille, [])
    
    for i in range(taille):
        for j in range(taille):

            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k != i or l != j: predation[i][j] += monde[k%taille][l%taille]

    return predation

def regleJeuVie(etatCellule, nombreVoisins):
    return 1 if (nombreVoisins == 3) or (etatCellule == 1 and nombreVoisins == 2) else 0

def afficher(monde):
    taille = len(monde)
    for i in range(taille):
        for j in range(taille):
            print(monde[j][i], " ", end='')
        print(" ")

monde = creerMonde(10, [(3,3), (3, 4), (3, 5), (3, 5)])
while True:
    afficher(monde)
    evoluer(monde, calculerPredation(monde), regleJeuVie)
    print(" ")
