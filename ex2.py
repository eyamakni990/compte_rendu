
# Exercice 2 : Probleme de transport
# Methode : Recherche taboue

DEMANDES = [4, 5, 8]
STOCK_D1 = 8
STOCK_D2 = 9

COUTS = [
    [5, 3, 4],  # Depot D1 vers M1, M2, M3
    [6, 7, 2]   # Depot D2 vers M1, M2, M3
]


def calculer_cout(x):
    """x represente les quantites envoyees depuis D1."""
    y = [DEMANDES[i] - x[i] for i in range(3)]

    cout = 0
    for i in range(3):
        cout += x[i] * COUTS[0][i]
        cout += y[i] * COUTS[1][i]

    return cout


def est_valide(x):
    """Verifier que la solution respecte les contraintes."""
    if any(x[i] < 0 or x[i] > DEMANDES[i] for i in range(3)):
        return False

    if sum(x) != STOCK_D1:
        return False

    y = [DEMANDES[i] - x[i] for i in range(3)]
    return sum(y) == STOCK_D2


def generer_voisins(x):
    """Transferer une unite d'un magasin a un autre."""
    voisins = []

    for i in range(3):
        for j in range(3):
            if i != j and x[i] > 0 and x[j] < DEMANDES[j]:
                voisin = x.copy()
                voisin[i] -= 1
                voisin[j] += 1

                if est_valide(voisin):
                    voisins.append(voisin)

    return voisins


def recherche_taboue(iterations=100, taille_taboue=7):
    solution = [4, 4, 0]
    meilleure_solution = solution.copy()
    meilleure_cout = calculer_cout(solution)

    liste_taboue = []

    for k in range(iterations):
        voisins = generer_voisins(solution)
        candidats = []

        for voisin in voisins:
            cout = calculer_cout(voisin)
            mouvement = tuple(voisin)

            # Critere d'aspiration :
            # accepter si le voisin ameliore le meilleur resultat
            if mouvement not in liste_taboue or cout < meilleure_cout:
                candidats.append((cout, voisin))

        if not candidats:
            break

        candidats.sort(key=lambda element: element[0])
        cout_voisin, meilleur_voisin = candidats[0]

        solution = meilleur_voisin.copy()

        liste_taboue.append(tuple(solution))
        if len(liste_taboue) > taille_taboue:
            liste_taboue.pop(0)

        if cout_voisin < meilleure_cout:
            meilleure_solution = solution.copy()
            meilleure_cout = cout_voisin

    return meilleure_solution, meilleure_cout


# Programme principal
solution, cout = recherche_taboue()

y = [DEMANDES[i] - solution[i] for i in range(3)]

print("=== Probleme de transport ===")
print("Quantites envoyees depuis D1 :", solution)
print("Quantites envoyees depuis D2 :", y)
print("Cout total minimal :", cout)
