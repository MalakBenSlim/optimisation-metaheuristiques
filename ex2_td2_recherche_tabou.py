"""
Exercice 2 : Problème de transport de containers
Résolution par recherche taboue (+ vérification exacte par PLNE si scipy dispo)
"""
import random
import itertools
 
# ----------------- Données -----------------
COUT = [[5, 3, 4],
        [6, 7, 2]]
OFFRE = [8, 9]
DEMANDE = [4, 5, 8]
m, n = len(OFFRE), len(DEMANDE)
 
 
def cout_total(x):
    return sum(COUT[i][j] * x[i][j] for i in range(m) for j in range(n))
 
 
# ----------------- Solution initiale : coin nord-ouest -----------------
def coin_nord_ouest():
    offre, dem = OFFRE[:], DEMANDE[:]
    x = [[0] * n for _ in range(m)]
    i = j = 0
    while i < m and j < n:
        q = min(offre[i], dem[j])
        x[i][j] += q
        offre[i] -= q
        dem[j] -= q
        if offre[i] == 0:
            i += 1
        else:
            j += 1
    return x
 
 
# ----------------- Voisinage -----------------
def voisins(x):
    """Mouvements de cycle : +1/-1 sur un rectangle (i,k) x (j,l)."""
    for i, k in itertools.permutations(range(m), 2):
        for j, l in itertools.permutations(range(n), 2):
            if x[i][j] >= 1 and x[k][l] >= 1:
                # x[i][j]-1, x[i][l]+1, x[k][j]+1, x[k][l]-1
                yield (i, k, j, l)
 
 
def appliquer(x, mv, sens=1):
    i, k, j, l = mv
    y = [row[:] for row in x]
    y[i][j] -= sens
    y[i][l] += sens
    y[k][j] += sens
    y[k][l] -= sens
    return y
 
 
def inverse(mv):
    i, k, j, l = mv
    # le mouvement inverse remet une unité en (i,j) et (k,l)
    return (k, i, l, j)
 
 
# ----------------- Recherche taboue -----------------
def recherche_taboue(max_iter=200, tenure=4, seed=0):
    random.seed(seed)
    x = coin_nord_ouest()
    meilleur, meilleur_cout = [r[:] for r in x], cout_total(x)
    tabou = {}  # mouvement -> itération jusqu'à laquelle il est tabou
 
    print(f"Solution initiale (coin nord-ouest) : {x}  coût = {cout_total(x)}")
 
    for it in range(1, max_iter + 1):
        candidats = []
        for mv in voisins(x):
            y = appliquer(x, mv)
            c = cout_total(y)
            est_tabou = tabou.get(mv, 0) >= it
            # critère d'aspiration
            if est_tabou and c >= meilleur_cout:
                continue
            candidats.append((c, random.random(), mv, y))
 
        if not candidats:
            break
 
        c, _, mv, y = min(candidats)
        x = y
        tabou[inverse(mv)] = it + tenure  # interdit de revenir en arrière
 
        if c < meilleur_cout:
            meilleur, meilleur_cout = [r[:] for r in y], c
            print(f"Itération {it:3d} : amélioration -> coût = {c}")
 
    return meilleur, meilleur_cout
 
 
# ----------------- Vérification exacte (optionnel) -----------------
def verification_exacte():
    try:
        from scipy.optimize import linprog
    except ImportError:
        return None
    c = [COUT[i][j] for i in range(m) for j in range(n)]
    A_eq, b_eq = [], []
    for i in range(m):
        A_eq.append([1 if k // n == i else 0 for k in range(m * n)])
        b_eq.append(OFFRE[i])
    for j in range(n):
        A_eq.append([1 if k % n == j else 0 for k in range(m * n)])
        b_eq.append(DEMANDE[j])
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), integrality=[1] * (m * n))
    return res.fun
 
 
if __name__ == "__main__":
    sol, z = recherche_taboue()
    print("\n=== Résultat recherche taboue ===")
    print("      M1  M2  M3")
    for i, row in enumerate(sol):
        print(f"D{i+1}  " + "  ".join(f"{v:3d}" for v in row))
    print("Coût total minimal trouvé :", z)
 
    z_exact = verification_exacte()
    if z_exact is not None:
        print("Optimum exact (PLNE)      :", z_exact)
