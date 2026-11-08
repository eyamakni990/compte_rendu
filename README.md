# Ordonnancement des maintenances des centrales électriques par algorithme génétique

## 1. Présentation du projet

Ce projet consiste à appliquer un algorithme génétique pour planifier les opérations de maintenance de sept unités de production électrique sur quatre périodes.

L'objectif est de trouver un planning qui maximise la réserve minimale de puissance tout en respectant les contraintes de maintenance de chaque unité.

## 2. Données du problème

### 2.1. Puissance et durée de maintenance

| Unité | Puissance (MW) | Durée de maintenance |
|---|---:|---:|
| U1 | 20 | 2 périodes consécutives |
| U2 | 15 | 2 périodes consécutives |
| U3 | 35 | 1 période |
| U4 | 40 | 1 période |
| U5 | 15 | 1 période |
| U6 | 15 | 1 période |
| U7 | 10 | 1 période |
| **Total** | **150** | |

### 2.2. Demande électrique

| Période | Demande (MW) |
|---|---:|
| P1 | 80 |
| P2 | 90 |
| P3 | 65 |
| P4 | 70 |

## 3. Codage du chromosome

Un chromosome représente un planning de maintenance pour les sept unités.

- Un chromosome contient 7 gènes.
- Chaque gène contient 4 bits.
- La longueur totale est de 28 bits.
- Le bit 1 indique que l'unité est en maintenance.
- Le bit 0 indique que l'unité n'est pas en maintenace.

### Motifs de maintenance autorisés

| Unités | Motifs autorisés |
|---|---|
| U1 et U2 | `1100`, `0110`, `0011` |
| U3 à U7 | `1000`, `0100`, `0010`, `0001` |

Les unités U1 et U2 nécessitent deux périodes consécutives de maintenance. Les autres unités nécessitent une seule période.

## 4. Formulation mathématique

On définit :

- \(C_i\) : puissance de l'unité \(i\).
- \(D_j\) : demande électrique de la période \(j\).
- \(x_{ij}\) : variable binaire qui vaut 1 si l'unité \(i\) est en maintenance pendant la période \(j\), et 0 sinon.
- \(R_j\) : réserve de puissance pendant la période \(j\).

### 4.1. Puissance indisponible

La puissance indisponible pendant une période est :

\[
M_j=\sum_{i=1}^{7} C_i x_{ij}
\]

### 4.2. Calcul de la réserve

La réserve de puissance est calculée par :

\[
R_j=150-M_j-D_j
\]

### 4.3. Fonction objectif

L'objectif est de maximiser la réserve minimale parmi les quatre périodes :

\[
\boxed{\text{Maximiser } F=\min(R_1,R_2,R_3,R_4)}
\]

### 4.4. Contraintes

- Respecter les motifs de maintenance autorisés.
- Les unités U1 et U2 doivent avoir deux périodes consécutives de maintenance.
- Les unités U3 à U7 doivent avoir une seule période de maintenance.
- La réserve doit être strictement positive pendant chaque période.

## 5. Fonction d'évaluation (Fitness)

La fonction fitness permet d'évaluer la qualité d'un chromosome.

\[
Fitness=
\begin{cases}
\min(R_1,R_2,R_3,R_4), & \text{si toutes les réserves sont positives}\\
0, & \text{sinon}
\end{cases}
\]

Une fitness élevée correspond à une meilleure solution.

## 6. Méthodes de l'algorithme génétique

### 6.1. Génération de la population initiale

Une population initiale de 49 chromosomes est générée aléatoirement. Chaque gène est choisi parmi les motifs autorisés pour son unité.

### 6.2. Sélection par loterie (roulette)

La sélection par loterie permet de choisir les individus qui participeront à la reproduction.

La probabilité de sélection d'un individu dépend de sa fitness :

\[
P_i=\frac{Fitness_i}{\sum Fitness}
\]

Un individu ayant une meilleure fitness possède une probabilité plus élevée d'être sélectionné.

### 6.3. Croisement

Le croisement est réalisé avec une probabilité \(Pc\).

Un point de coupure est choisi entre deux gènes, sans couper un bloc de quatre bits.

Les parties des deux parents sont échangées pour produire deux enfants.

### 6.4. Mutation par inversion

La mutation est réalisée avec une probabilité \(Pm\).

Elle consiste à inverser l'ordre des quatre bits d'un gène.

Exemple :

- Avant : 1100
- Après : 0011

Cette opération conserve les motifs de maintenance autorisés.

### 6.5. Élitisme

Le meilleur individu de chaque génération est conservé dans la génération suivante afin de préserver la meilleure solution trouvée.

## 7. Paramètres utilisés

| Paramètre | Valeur |
|---|---:|
| Taille de la population | 49 |
| Nombre de générations | 200 |
| Probabilité de croisement (Pc) | Variable |
| Probabilité de mutation (Pm) | Variable |
| Méthode de sélection | Loterie |
| Méthode de mutation | Inversion |

## 8. Expérimentations et résultats

Pour étudier l'influence des probabilités de croisement et de mutation, cinq configurations ont été testées.

### 8.1. Résultats obtenus

| Essai | Pc | Pm | P1 (MW) | P2 (MW) | P3 (MW) | P4 (MW) | Fitness (MW) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0,8 | 0,1 | 30 | 25 | 30 | 25 | 25 |
| 2 | 0,8 | 0,2 | 25 | 25 | 30 | 30 | 25 |
| 3 | 0,7 | 0,1 | 30 | 25 | 25 | 30 | 25 |
| 4 | 0,9 | 0,1 | 35 | 25 | 25 | 25 | 25 |
| 5 | 0,7 | 0,2 | 30 | 30 | 25 | 25 | 25 |

### 8.2. Analyse des résultats

Les résultats montrent que :

- Les cinq essais donnent une fitness de 25 MW.
- Tous les chromosomes obtenus respectent les motifs de maintenance autorisés.
- Toutes les réserves sont positives.
- La quatrième configuration donne une réserve de 35 MW pendant la première période.
- La réserve minimale reste égale à 25 MW dans les cinq essais.

Les probabilités de croisement et de mutation influencent la répartition des maintenances entre les périodes et les chromosomes obtenus.

## 9. Exécution du programme

Le projet utilise Python 3 et la bibliothèque standard `random`. 

Le programme affiche pour chaque configuration :

- Les probabilités de croisement et de mutation.
- Les sept gènes du meilleur chromosome.
- Les réserves des quatre périodes.
- La valeur de fitness.
- La validité du chromosome.

## 10. Conclusion

Ce projet m'a permis d'appliquer un algorithme génétique à un problème d'ordonnancement des maintenances des centrales électriques.

J'ai utilisé la sélection par loterie, le croisement entre les gènes et la mutation par inversion pour générer et améliorer les solutions.

Les cinq expérimentations ont donné une fitness de 25 MW. Les solutions obtenues respectent les contraintes de maintenance et garantissent une réserve positive pendant les quatre périodes.

Ce travail montre l'intérêt des algorithmes génétiques pour résoudre des problèmes d'optimisation combinatoire.