#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def trouverDifference(fichier1,fichier2):
    f = open(fichier1, "r", encoding="utf-8")
    g = open(fichier2, "r", encoding="utf-8")

    count = 0
    for line in f:
        each = g.readline()
        count += 1
        if line != each:
            f.close()
            g.close()
            return count, line,each
    g.close()
    f.close()
    return -1,-1,-1

def recopieurTriple(fichier1, fichier2):
    f = open(fichier1, "r", encoding="utf-8")
    g = open(fichier2, "a", encoding="utf-8")

    for each in f:
        word = each.split(" ")
    text = ""
    for each in word:
        text = text + each + "   "
    g.write("\n")
    g.write(text)
    return None

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    f = input("Entrer le nom du fichier originale:\n")
    g = input("Entrer le nom du fichier à comparer:\n")
    count, line, each = trouverDifference(f, g)
    if count == - 1:
        print("Les fichiers sont identiques.")
    else:
        txt = "Les fichiers ont une incohérence à la ligne {}."
        print(txt.format(line, each, count))

    f = input("Entrer le nom du fichier originale:\n")
    g = input("Entrer le nom du fichier à re-ecrire:\n")
    recopieurTriple(f,g)



    pass
