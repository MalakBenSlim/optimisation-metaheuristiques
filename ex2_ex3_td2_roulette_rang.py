# -*- coding: utf-8 -*-
"""
TD2 - Métaheuristiques
Exercice 2 : problème de transport -> Recherche Tabou
Exercice 3 : voyageur de commerce -> Tabou, Recuit Simulé, Algorithme Génétique
             (sélection par ROULETTE et par RANG)
"""
import random, math, itertools

random.seed(42)

# =====================================================================
# EXERCICE 2 : TRANSPORT  (dépôts -> magasins)
# =====================================================================
COST = [[5, 3, 4],      # D1 -> M1, M2, M3
        [6, 7, 2]]      # D2 -> M1, M2, M3
SUPPLY = [8, 9]         # colonne "Dépôt" : stock de D1 et D2
DEMAND = [4, 5, 8]      # demandes de M1, M2, M3


def cout_transport(x):
    return sum(COST[i][j] * x[i][j] for i in range(2) for j in range(3))


def faisable(x):
    if any(v < 0 for l in x for v in l):
        return False
    if any(sum(x[i]) != SUPPLY[i] for i in range(2)):
        return False
    return all(sum(x[i][j] for i in range(2)) == DEMAND[j] for j in range(3))


def solution_initiale_transport():
    """Coin Nord-Ouest."""
    s, d = SUPPLY[:], DEMAND[:]
    x = [[0] * 3 for _ in range(2)]
    i = j = 0
    while i < 2 and j < 3:
        q = min(s[i], d[j])
        x[i][j] = q
        s[i] -= q; d[j] -= q
        if s[i] == 0: i += 1
        else: j += 1
    return x


def voisins_transport(x):
    """Voisinage : on déplace 1 container entre 2 magasins j,k en
    gardant les stocks : (i1,j)-1 (i1,k)+1 (i2,j)+1 (i2,k)-1."""
    res = []
    for j, k in itertools.permutations(range(3), 2):
        y = [l[:] for l in x]
        y[0][j] -= 1; y[0][k] += 1
        y[1][j] += 1; y[1][k] -= 1
        if faisable(y):
            res.append(((j, k), y))
    return res


def tabou_transport(iter_max=30, taille_tabou=3):
    x = solution_initiale_transport()
    best, best_c = [l[:] for l in x], cout_transport(x)
    tabou = []
    print("\n=== EXERCICE 2 : Recherche Tabou (transport) ===")
    print("Solution initiale (coin NO):", x, "coût =", best_c)
    for it in range(1, iter_max + 1):
        cand = []
        for mv, y in voisins_transport(x):
            c = cout_transport(y)
            # aspiration : un mouvement tabou est accepté s'il bat le meilleur
            if mv not in tabou or c < best_c:
                cand.append((c, mv, y))
        if not cand:
            break
        c, mv, y = min(cand, key=lambda t: t[0])
        x = y
        tabou.append((mv[1], mv[0]))          # on interdit le mouvement inverse
        if len(tabou) > taille_tabou:
            tabou.pop(0)
        if c < best_c:
            best, best_c = [l[:] for l in y], c
        if it <= 6:
            print(f"  it {it}: mouvement {mv} -> coût {c}  (meilleur {best_c})")
    print("Meilleure solution :", best, "coût =", best_c)
    return best, best_c


def verif_exhaustive_transport():
    best = None
    for a in range(0, 5):
        for b in range(0, 6):
            x1 = [a, b, SUPPLY[0] - a - b]
            if x1[2] < 0: continue
            x = [x1, [DEMAND[j] - x1[j] for j in range(3)]]
            if faisable(x) and (best is None or cout_transport(x) < best[0]):
                best = (cout_transport(x), x)
    print("Optimum exact (vérification) :", best[1], "coût =", best[0])


# =====================================================================
# EXERCICE 3 : VOYAGEUR DE COMMERCE (graphe non complet : '-' = pas d'arête)
# =====================================================================
INF = 1000   # pénalité pour une arête inexistante
ARETES = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17, (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13,
}
D = {}
for (a, b), c in ARETES.items():
    D[(a, b)] = D[(b, a)] = c


def dist(a, b):
    return D.get((a, b), INF)


def longueur(t):
    """t = [1,2,...,8] ; le retour à 1 est ajouté."""
    return sum(dist(t[i], t[(i + 1) % len(t)]) for i in range(len(t)))


def aff(t):
    return "-".join(map(str, t + [t[0]]))


# ---------- 1) Recherche Tabou ----------
def tabou_tsp(iter_max=10, taille_tabou=3):
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    best, best_c = x[:], longueur(x)
    tabou = []
    print("\n=== EXERCICE 3 - Q1 : Recherche Tabou ===")
    print("Solution initiale :", aff(x), "L =", best_c)
    for it in range(1, iter_max + 1):
        cand = []
        for i, j in itertools.combinations(range(1, 8), 2):   # ville 1 fixe
            y = x[:]
            y[i], y[j] = y[j], y[i]
            mv = (min(x[i], x[j]), max(x[i], x[j]))
            c = longueur(y)
            if mv not in tabou or c < best_c:
                cand.append((c, mv, y))
        c, mv, y = min(cand, key=lambda t: t[0])
        x = y
        tabou.append(mv)
        if len(tabou) > taille_tabou:
            tabou.pop(0)
        if c < best_c:
            best, best_c = y[:], c
        print(f"  it {it}: échange villes {mv} -> {aff(x)}  L={c}  (meilleur {best_c})")
    print("Meilleure tournée :", aff(best), "L =", best_c)
    return best, best_c


# ---------- 2) Recuit simulé ----------
def recuit_tsp(T0=20.0, alpha=0.6, n_iter=5):
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    cx = longueur(x)
    best, best_c = x[:], cx
    T = T0
    print("\n=== EXERCICE 3 - Q2 : Recuit simulé (5 itérations) ===")
    print(f"Départ : {aff(x)} L={cx}  T0={T0}, T <- {alpha}*T (variation empirique)")
    for it in range(1, n_iter + 1):
        i, j = sorted(random.sample(range(1, 8), 2))
        y = x[:]
        y[i], y[j] = y[j], y[i]                       # voisin : échange
        cy = longueur(y)
        delta = cy - cx
        if delta <= 0:
            acc, p = True, 1.0
        else:
            p = math.exp(-delta / T)
            acc = random.random() < p
        print(f"  it {it}: T={T:6.2f} voisin {aff(y)} L={cy} Δ={delta:+d} "
              f"p={p:.3f} -> {'accepté' if acc else 'refusé'}")
        if acc:
            x, cx = y, cy
            if cx < best_c:
                best, best_c = x[:], cx
        T *= alpha
    print("Meilleure tournée :", aff(best), "L =", best_c)
    return best, best_c


# ---------- 3) Algorithme génétique ----------
def population_initiale(n):
    pop = []
    while len(pop) < n:
        p = list(range(2, 9))
        random.shuffle(p)
        pop.append([1] + p)
    return pop


def fitness(t):
    return 1.0 / longueur(t)


def selection_roulette(pop):
    """Probabilité proportionnelle à la fitness 1/L."""
    f = [fitness(t) for t in pop]
    S = sum(f)
    r = random.uniform(0, S)
    cum = 0
    for t, ft in zip(pop, f):
        cum += ft
        if cum >= r:
            return t[:]
    return pop[-1][:]


def selection_rang(pop):
    """Tri par qualité : le pire a le rang 1, le meilleur le rang N ;
    probabilité = rang / somme des rangs."""
    tri = sorted(pop, key=longueur, reverse=True)      # pire -> meilleur
    N = len(tri)
    S = N * (N + 1) / 2
    r = random.uniform(0, S)
    cum = 0
    for k, t in enumerate(tri, start=1):
        cum += k
        if cum >= r:
            return t[:]
    return tri[-1][:]


def croisement_ox(p1, p2):
    """Order Crossover (ville 1 reste en tête)."""
    a, b = sorted(random.sample(range(1, 8), 2))
    enfant = [None] * 8
    enfant[0] = 1
    enfant[a:b + 1] = p1[a:b + 1]
    reste = [v for v in p2 if v not in enfant]
    for i in range(8):
        if enfant[i] is None:
            enfant[i] = reste.pop(0)
    return enfant


def mutation(t, pm=0.2):
    t = t[:]
    if random.random() < pm:
        i, j = random.sample(range(1, 8), 2)
        t[i], t[j] = t[j], t[i]
    return t


def ag_tsp(selection, nom, taille=8, generations=30, verbose_gen=3):
    pop = population_initiale(taille)
    best = min(pop, key=longueur)
    print(f"\n--- AG avec sélection {nom} ---")
    for g in range(1, generations + 1):
        nouvelle = [min(pop, key=longueur)[:]]          # élitisme
        while len(nouvelle) < taille:
            p1, p2 = selection(pop), selection(pop)
            nouvelle.append(mutation(croisement_ox(p1, p2)))
        pop = nouvelle
        cur = min(pop, key=longueur)
        if longueur(cur) < longueur(best):
            best = cur[:]
        if g <= verbose_gen or g == generations:
            moy = sum(longueur(t) for t in pop) / taille
            print(f"  génération {g:2d}: meilleur {aff(cur)} L={longueur(cur)}  moyenne={moy:.1f}")
    print(f"Meilleure tournée ({nom}) : {aff(best)}  L = {longueur(best)}")
    return best, longueur(best)


def exhaustif_tsp():
    best = None
    for p in itertools.permutations(range(2, 9)):
        t = [1] + list(p)
        L = longueur(t)
        if best is None or L < best[0]:
            best = (L, t)
    print("\nOptimum exact (vérification, 7! = 5040 tournées) :", aff(best[1]), "L =", best[0])


if __name__ == "__main__":
    tabou_transport()
    verif_exhaustive_transport()

    tabou_tsp()
    recuit_tsp()
    print("\n=== EXERCICE 3 - Q3 : Algorithme génétique ===")
    r1 = ag_tsp(selection_roulette, "ROULETTE")
    r2 = ag_tsp(selection_rang, "RANG")
    exhaustif_tsp()
