def look_like_sapin(points, hauteur=103, largeur=101):
    # Axe central (le centre des colonnes)
    axe_central = largeur // 2

    # Organiser les points par ligne
    points_par_ligne = {ligne: [] for ligne in range(hauteur)}
    for x, y in points:
        points_par_ligne[x].append(y)

    # Parcourir les lignes pour trouver une structure triangulaire
    for ligne in range(hauteur - 2):  # -2 car on vérifie 3 lignes successives
        # Obtenir les points pour les 3 lignes successives
        ligne1 = sorted(points_par_ligne[ligne])
        ligne2 = sorted(points_par_ligne[ligne + 1])
        ligne3 = sorted(points_par_ligne[ligne + 2])

        # Vérifier que chaque ligne a respectivement 1, 3, et 5 points
        if len(ligne1) == 1 and len(ligne2) == 3 and len(ligne3) == 5:
            # Vérifier la symétrie autour de l'axe central
            if (ligne1[0] == axe_central and
                ligne2[0] == axe_central - 1 and ligne2[2] == axe_central + 1 and
                ligne3[0] == axe_central - 2 and ligne3[4] == axe_central + 2):
                return True

    # Si aucun motif pyramidale n'a été trouvé
    return False

points = [
    (0, 50),           # Ligne 0 : *
    (1, 49), (1, 50), (1, 51),  # Ligne 1 : ***
    (2, 48), (2, 49), (2, 50), (2, 51), (2, 52)  # Ligne 2 : *****
]

print(look_like_sapin(points))  # True
