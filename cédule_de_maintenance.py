import random

capacites = [20, 15, 35, 40, 15, 15, 10]
demandes = [80, 90, 65, 70]
motifs = [
    ["1100", "0110", "0011"],
    ["1100", "0110", "0011"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"]]

taille_population = 49
nombre_generations = 200


def generer_individu():
    return [random.choice(motifs[i]) for i in range(7)]


def generer_population():
    return [generer_individu() for _ in range(taille_population)]


def chromosome_valide(individu):
    return len(individu) == 7 and all(individu[i] in motifs[i] for i in range(7))


def calculer_reserves(individu):
    reserves = []
    for periode in range(4):
        puissance_maintenance = sum(capacites[i] for i in range(7) if individu[i][periode] == "1")
        reserve = sum(capacites) - puissance_maintenance - demandes[periode]
        reserves.append(reserve)
    return reserves


def fitness(individu):
    if not chromosome_valide(individu):
        return 0
    reserves = calculer_reserves(individu)
    return min(reserves) if min(reserves) > 0 else 0


def selection_loterie(population):
    valeurs_fitness = [fitness(individu) for individu in population]
    if sum(valeurs_fitness) == 0:
        return random.choice(population)
    return random.choices(population, weights=valeurs_fitness, k=1)[0]


def croisement(parent1, parent2, pc):
    if random.random() >= pc:
        return parent1[:], parent2[:]
    point_coupure = random.randint(1, 6)
    enfant1 = parent1[:point_coupure] + parent2[point_coupure:]
    enfant2 = parent2[:point_coupure] + parent1[point_coupure:]
    return enfant1, enfant2


def mutation_inversion(individu, pm):
    individu = individu[:]
    if random.random() < pm:
        indice_gene = random.randint(0, 6)
        individu[indice_gene] = individu[indice_gene][::-1]
    return individu


def algorithme_genetique(pc=0.8, pm=0.1):
    population = generer_population()
    meilleur = max(population, key=fitness)

    for _ in range(nombre_generations):
        nouvelle_population = []
        meilleur_generation = max(population, key=fitness)
        nouvelle_population.append(meilleur_generation[:])

        while len(nouvelle_population) < taille_population:
            parent1 = selection_loterie(population)
            parent2 = selection_loterie(population)
            enfant1, enfant2 = croisement(parent1, parent2, pc)
            enfant1 = mutation_inversion(enfant1, pm)
            enfant2 = mutation_inversion(enfant2, pm)
            nouvelle_population.append(enfant1)

            if len(nouvelle_population) < taille_population:
                nouvelle_population.append(enfant2)

        population = nouvelle_population
        candidat = max(population, key=fitness)

        if fitness(candidat) > fitness(meilleur):
            meilleur = candidat[:]

    return meilleur, calculer_reserves(meilleur), fitness(meilleur)


def afficher_resultats(pc, pm):
    meilleur, reserves, valeur_fitness = algorithme_genetique(pc, pm)

    print("\n" + "=" * 45)
    print(f"Probabilite de croisement : {pc}")
    print(f"Probabilite de mutation : {pm}")
    print("Selection : Loterie")
    print("Mutation : Inversion")
    print("-" * 45)

    for numero, gene in enumerate(meilleur, start=1):
        print(f"Unite {numero} : {gene}")

    print("-" * 45)

    for numero, reserve in enumerate(reserves, start=1):
        print(f"Reserve periode {numero} : {reserve} MW")

    print(f"Fitness : {valeur_fitness} MW")
    print(f"Chromosome valide : {chromosome_valide(meilleur)}")


if __name__ == "__main__":
    configurations = [(0.8, 0.1), (0.8, 0.2), (0.7, 0.1), (0.9, 0.1), (0.7, 0.2)]

    for pc, pm in configurations:
        afficher_resultats(pc, pm)
