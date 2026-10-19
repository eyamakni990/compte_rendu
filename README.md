# TD n°2 : Algorithme évolutionnaires
# Exercice 2 : Probleme de transport

## Description
Cet exercice consiste à résoudre un problème de transport en utilisant la méthode de recherche taboue en Python.

L'objectif est de minimiser le coût total du transport entre deux dépôts(D1,D2) et trois magasins(M1,M2,M3), tout en respectant les stocks disponibles(8 unités pour D1 et 9 unités pour D2) et les demandes des magasins(4,5,8).

## Algorithme utilisé : Recherche taboue
La recherche tabou est une métaheuristique d'optimisation à solution unique (ou basée sur une trajectoire). Le déroulement logique de cet algorithme s'articule autour des étapes clés suivantes :

1. Initialiser une solution de départ.
2. Générer des solutions voisines.
3. Vérifier les contraintes du problème.
4. Calculer le coût de chaque solution.
5. Choisir le meilleur voisin autorisé.
6. Mettre à jour la liste taboue et la meilleure solution.
7. Répéter jusqu'à atteindre le nombre maximal d'itérations.

## Résultat attendu
<img width="413" height="84" alt="image" src="https://github.com/user-attachments/assets/ce7885d2-abae-490f-9fad-c709baef043c" />


# Exercice 3 — Problème du voyageur de commerce (TSP)

## 1. Description

Ce projet consiste à résoudre le problème du voyageur de commerce en utilisant deux métaheuristiques :

- La recherche taboue (*Tabu Search*).
- Le recuit simulé (*Simulated Annealing*).

L'objectif est de trouver un circuit qui passe par les huit villes, visite chaque ville une seule fois et revient à la ville de départ, tout en minimisant la distance totale parcourue.

## 2. Données du problème

Le problème comporte huit villes numérotées de 1 à 8.

Le circuit initial est :

`1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 1`

Les distances entre les villes sont définies à partir de la matrice fournie dans l'énoncé. Les distances sont considérées comme symétriques. Lorsqu'une distance n'est pas indiquée, la liaison correspondante est considérée comme indisponible.

La distance totale d'un circuit est calculée en additionnant les distances entre chaque paire de villes consécutives, y compris le retour à la ville de départ.

## 3. Méthode 1 : Recherche taboue

### Principe

La recherche taboue est une métaheuristique qui explore le voisinage d'une solution afin de trouver un circuit de distance réduite.

### Étapes de l'algorithme

1. Initialiser le circuit avec l'ordre des villes donné dans l'énoncé.
2. Calculer la distance totale du circuit initial.
3. Générer des solutions voisines en échangeant deux villes.
4. Écarter les circuits qui utilisent des liaisons indisponibles.
5. Choisir le meilleur voisin autorisé, même s'il n'améliore pas immédiatement la solution courante.
6. Enregistrer les solutions récemment visitées dans la liste taboue.
7. Mettre à jour la meilleure solution lorsque la distance diminue.
8. Répéter jusqu'à atteindre le nombre maximal d'itérations ou jusqu'à ce qu'aucun candidat ne soit disponible.

### Paramètres

- Nombre maximal d'itérations : 500.
- Taille maximale de la liste taboue : 10.

## Résultat attendu
<img width="591" height="53" alt="image" src="https://github.com/user-attachments/assets/02f33638-c64d-41fc-a4ba-ce6c85c276e8" />

## 4. Méthode 2 : Recuit simulé

### Principe

Le recuit simulé est une métaheuristique inspirée du refroidissement progressif des matériaux. Il permet d'explorer différentes solutions et d'éviter de rester trop rapidement bloqué dans un optimum local.

### Étapes de l'algorithme

1. Initialiser le circuit et calculer sa distance totale.
2. Définir la température initiale `T0`.
3. Générer un voisin en échangeant deux villes.
4. Calculer la variation de distance :
 `Delta = distance_voisin - distance_actuelle`
5. Si `Delta < 0`, accepter le voisin car il améliore la solution.
6. Sinon, accepter éventuellement le voisin avec la probabilité :
 `P = exp(-Delta / T)`
7. Diminuer progressivement la température :
   `T = beta * T`
8. Conserver la meilleure solution trouvée et arrêter lorsque le nombre maximal d'itérations est atteint ou que la température devient très faible.

### Paramètres

- Température initiale : `T0 = 100`.
- Coefficient de refroidissement : `beta = 0.95`.
- Nombre maximal d'itérations : 1000.
- Graine aléatoire : `42` pour rendre l'exécution reproductible.

## Résultat attendu
<img width="595" height="47" alt="image" src="https://github.com/user-attachments/assets/1c574577-6cab-4b72-b69a-0d99f53a8142" />

## Technologies utilisées

- Python 3
- Thonny
- Modules math et random pour l'exercice 3

## Conclusion

Ce travail permet de comparer deux métaheuristiques appliquées au problème du voyageur de commerce. La recherche taboue utilise une mémoire des solutions récentes pour limiter les cycles, tandis que le recuit simulé accepte parfois une solution moins bonne afin d'explorer davantage l'espace de recherche.
