
import math

# Distances entre les villes
DISTANCES = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17,
    (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13
}

# Rendre la matrice symetrique
for (a, b), d in list(DISTANCES.items()):
    DISTANCES[(b, a)] = d

TOUR_INITIAL = [1, 2, 3, 4, 5, 6, 7, 8]


def distance(a, b):
    return DISTANCES.get((a, b), math.inf)


def cout_tour(tour):
    cout = 0

    for i in range(len(tour)):
        a = tour[i]
        b = tour[(i + 1) % len(tour)]
        d = distance(a, b)

        if d == math.inf:
            return math.inf

        cout += d

    return cout


def afficher_tour(tour):
    return " -> ".join(map(str, tour + [tour[0]]))


def generer_voisins(tour):
    voisins = []

    # On garde la ville 1 comme ville de depart
    for i in range(1, len(tour)):
        for j in range(i + 1, len(tour)):
            voisin = tour.copy()
            voisin[i], voisin[j] = voisin[j], voisin[i]

            if cout_tour(voisin) != math.inf:
                voisins.append(voisin)

    return voisins


def recherche_taboue(iterations=500, taille_taboue=10):
    solution = TOUR_INITIAL.copy()
    meilleure_solution = solution.copy()
    meilleure_distance = cout_tour(solution)

    liste_taboue = []

    for k in range(iterations):
        voisins = generer_voisins(solution)
        candidats = []

        for voisin in voisins:
            mouvement = tuple(voisin)
            cout = cout_tour(voisin)

            # Critere d'aspiration
            if mouvement not in liste_taboue or cout < meilleure_distance:
                candidats.append((cout, voisin))

        if not candidats:
            break

        # Choisir le meilleur voisin autorise
        candidats.sort(key=lambda x: x[0])
        cout_voisin, meilleur_voisin = candidats[0]

        solution = meilleur_voisin.copy()

        liste_taboue.append(tuple(solution))

        if len(liste_taboue) > taille_taboue:
            liste_taboue.pop(0)

        if cout_voisin < meilleure_distance:
            meilleure_solution = solution.copy()
            meilleure_distance = cout_voisin

    return meilleure_solution, meilleure_distance


# Programme principal
if __name__ == "__main__":
    print("=== RECHERCHE TABOUE ===")
    print("Tour initial :", afficher_tour(TOUR_INITIAL))
    print("Cout initial :", cout_tour(TOUR_INITIAL))

    tour, cout = recherche_taboue()

    print("\nMeilleur tour :", afficher_tour(tour))
    print("Distance minimale trouvee :", cout)
