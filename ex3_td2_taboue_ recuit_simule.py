"""
Exercice 3 : Voyageur de commerce (8 villes, certaines routes inexistantes)
1) Recherche taboue (solution initiale 1-2-3-4-5-6-7-8-1)
2) Recuit simulé (5 itérations, variation empirique de T)
Vérification exacte par énumération.
"""
import math
import random
import itertools
 
INF = float("inf")
 
# Distances (les "-" du tableau = route inexistante)
ARETES = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17, (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13,
}
 
 
def d(a, b):
    return ARETES.get((a, b), ARETES.get((b, a), INF))
 
 
def cout(tour):
    """tour = liste de villes sans répéter la première ; on referme le cycle."""
    return sum(d(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour)))
 
 
def affiche(tour):
    return "-".join(map(str, tour + [tour[0]]))
 
 
# ------------------------------------------------------------
# 1) Recherche taboue : voisinage = échange de 2 villes (la ville 1 reste fixe)
# ------------------------------------------------------------
def recherche_taboue(init, max_iter=10, tenure=3):
    x = init[:]
    best, best_c = x[:], cout(x)
    tabou = {}
    print(f"Solution initiale : {affiche(x)}  coût = {best_c}")
    for it in range(1, max_iter + 1):
        cands = []
        for i, j in itertools.combinations(range(1, len(x)), 2):
            y = x[:]
            y[i], y[j] = y[j], y[i]
            c = cout(y)
            if c == INF:
                continue
            mv = (min(x[i], x[j]), max(x[i], x[j]))
            if tabou.get(mv, 0) >= it and c >= best_c:
                continue  # tabou sans aspiration
            cands.append((c, mv, y))
        c, mv, y = min(cands, key=lambda t: (t[0], t[1]))
        x = y
        tabou[mv] = it + tenure
        if c < best_c:
            best, best_c = x[:], c
        print(f"it {it:2d} : échange {mv} -> {affiche(x)}  coût = {c}  (meilleur = {best_c})")
    return best, best_c
 
 
# ------------------------------------------------------------
# 2) Recuit simulé : 5 itérations, T diminue empiriquement (T <- 0.8*T)
# ------------------------------------------------------------
def recuit_simule(init, T0=10.0, alpha=0.8, n_iter=5, seed=1):
    random.seed(seed)
    x = init[:]
    cx = cout(x)
    best, best_c = x[:], cx
    T = T0
    print(f"Solution initiale : {affiche(x)}  coût = {cx}  T0 = {T0}")
    for it in range(1, n_iter + 1):
        # voisin aléatoire réalisable (échange de 2 villes)
        while True:
            i, j = random.sample(range(1, len(x)), 2)
            y = x[:]
            y[i], y[j] = y[j], y[i]
            cy = cout(y)
            if cy < INF:
                break
        delta = cy - cx
        if delta <= 0:
            accepte, p = True, 1.0
        else:
            p = math.exp(-delta / T)
            r = random.random()
            accepte = r < p
        print(f"it {it} : T = {T:.2f} | voisin {affiche(y)} coût = {cy} | Δ = {delta:+d}"
              f" | p = {p:.3f} -> {'accepté' if accepte else 'refusé'}")
        if accepte:
            x, cx = y, cy
            if cx < best_c:
                best, best_c = x[:], cx
        T *= alpha
    return best, best_c
 
 
# ------------------------------------------------------------
# Vérification exacte
# ------------------------------------------------------------
def optimum_exact():
    best, best_c = None, INF
    for perm in itertools.permutations(range(2, 9)):
        t = [1] + list(perm)
        c = cout(t)
        if c < best_c:
            best, best_c = t, c
    return best, best_c
 
 
if __name__ == "__main__":
    init = [1, 2, 3, 4, 5, 6, 7, 8]
    print("===== 1) RECHERCHE TABOUE =====")
    sol, c = recherche_taboue(init)
    print("Meilleure solution :", affiche(sol), "coût =", c)
    print("\n===== 2) RECUIT SIMULÉ =====")
    sol2, c2 = recuit_simule(init)
    print("Meilleure solution :", affiche(sol2), "coût =", c2)
    print("\n===== Optimum exact (énumération) =====")
    sol3, c3 = optimum_exact()
    print(affiche(sol3), "coût =", c3)

