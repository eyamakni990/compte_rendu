
import math
import random

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


def generer_voisin(tour):
    voisin = tour.copy()

    # Echanger deux villes differentes
    i, j = random.sample(range(1, len(tour)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]

    return voisin


def recuit_simule(T0=100, beta=0.95, iterations=1000):
    solution = TOUR_INITIAL.copy()
    cout_actuel = cout_tour(solution)

    meilleure_solution = solution.copy()
    meilleure_distance = cout_actuel

    T = T0

    for k in range(iterations):
        if T < 0.001:
            break

        voisin = generer_voisin(solution)
        cout_voisin = cout_tour(voisin)

        # Ignorer les tours qui utilisent une distance indisponible
        if cout_voisin == math.inf:
            T *= beta
            continue

        delta = cout_voisin - cout_actuel

        # Accepter une amelioration
        # ou parfois une degradation selon la temperature
        if delta < 0:
            solution = voisin
            cout_actuel = cout_voisin
        else:
            probabilite = math.exp(-delta / T)

            if random.random() < probabilite:
                solution = voisin
                cout_actuel = cout_voisin

        if cout_actuel < meilleure_distance:
            meilleure_solution = solution.copy()
            meilleure_distance = cout_actuel

        # Refroidissement
        T *= beta

    return meilleure_solution, meilleure_distance


# Programme principal
if __name__ == "__main__":
    random.seed(42)

    print("=== RECUIT SIMULE ===")
    print("Tour initial :", afficher_tour(TOUR_INITIAL))
    print("Cout initial :", cout_tour(TOUR_INITIAL))

    tour, cout = recuit_simule()

    print("\nMeilleur tour :", afficher_tour(tour))
    print("Distance minimale trouvee :", cout)
