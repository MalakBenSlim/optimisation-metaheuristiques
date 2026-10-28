Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/malak/OneDrive/Documents/LSI 3/Algorithmes évolutionnaires/ex2 et 3  td2 (avec roulette et rond).py

=== EXERCICE 2 : Recherche Tabou (transport) ===
Solution initiale (coin NO): [[4, 4, 0], [0, 1, 8]] coût = 55
  it 1: mouvement (0, 1) -> coût 52  (meilleur 52)
  it 2: mouvement (0, 2) -> coût 55  (meilleur 52)
  it 3: mouvement (0, 2) -> coût 58  (meilleur 52)
  it 4: mouvement (0, 2) -> coût 61  (meilleur 52)
  it 5: mouvement (1, 0) -> coût 64  (meilleur 52)
  it 6: mouvement (2, 1) -> coût 58  (meilleur 52)
Meilleure solution : [[3, 5, 0], [1, 0, 8]] coût = 52
Optimum exact (vérification) : [[3, 5, 0], [1, 0, 8]] coût = 52

=== EXERCICE 3 - Q1 : Recherche Tabou ===
Solution initiale : 1-2-3-4-5-6-7-8-1 L = 103
  it 1: échange villes (2, 3) -> 1-3-2-4-5-6-7-8-1  L=107  (meilleur 103)
  it 2: échange villes (4, 5) -> 1-3-2-5-4-6-7-8-1  L=108  (meilleur 103)
  it 3: échange villes (4, 6) -> 1-3-2-5-6-4-7-8-1  L=111  (meilleur 103)
  it 4: échange villes (3, 8) -> 1-8-2-5-6-4-7-3-1  L=115  (meilleur 103)
  it 5: échange villes (2, 7) -> 1-8-7-5-6-4-2-3-1  L=115  (meilleur 103)
  it 6: échange villes (5, 6) -> 1-8-7-6-5-4-2-3-1  L=107  (meilleur 103)
  it 7: échange villes (2, 3) -> 1-8-7-6-5-4-3-2-1  L=103  (meilleur 103)
  it 8: échange villes (4, 6) -> 1-8-7-4-5-6-3-2-1  L=108  (meilleur 103)
  it 9: échange villes (4, 5) -> 1-8-7-5-4-6-3-2-1  L=113  (meilleur 103)
  it 10: échange villes (5, 6) -> 1-8-7-6-4-5-3-2-1  L=108  (meilleur 103)
Meilleure tournée : 1-2-3-4-5-6-7-8-1 L = 103

=== EXERCICE 3 - Q2 : Recuit simulé (5 itérations) ===
Départ : 1-2-3-4-5-6-7-8-1 L=103  T0=20.0, T <- 0.6*T (variation empirique)
  it 1: T= 20.00 voisin 1-7-3-4-5-6-2-8-1 L=2084 Δ=+1981 p=0.000 -> refusé
  it 2: T= 12.00 voisin 1-2-4-3-5-6-7-8-1 L=114 Δ=+11 p=0.400 -> accepté
  it 3: T=  7.20 voisin 1-7-4-3-5-6-2-8-1 L=2093 Δ=+1979 p=0.000 -> refusé
  it 4: T=  4.32 voisin 1-6-4-3-5-2-7-8-1 L=2092 Δ=+1978 p=0.000 -> refusé
  it 5: T=  2.59 voisin 1-8-4-3-5-6-7-2-1 L=1107 Δ=+993 p=0.000 -> refusé
Meilleure tournée : 1-2-3-4-5-6-7-8-1 L = 103

=== EXERCICE 3 - Q3 : Algorithme génétique ===

--- AG avec sélection ROULETTE ---
  génération  1: meilleur 1-3-4-6-7-5-2-8-1 L=121  moyenne=1847.5
  génération  2: meilleur 1-3-4-6-7-5-2-8-1 L=121  moyenne=612.9
  génération  3: meilleur 1-3-4-6-7-5-2-8-1 L=121  moyenne=121.0
  génération 30: meilleur 1-8-7-6-5-4-3-2-1 L=103  moyenne=230.8
Meilleure tournée (ROULETTE) : 1-8-7-6-5-4-3-2-1  L = 103

--- AG avec sélection RANG ---
  génération  1: meilleur 1-6-7-8-3-4-5-2-1 L=1087  moyenne=2572.5
  génération  2: meilleur 1-6-7-8-3-4-5-2-1 L=1087  moyenne=1709.9
  génération  3: meilleur 1-6-7-8-3-4-5-2-1 L=1087  moyenne=1217.2
  génération 30: meilleur 1-3-8-7-6-4-5-2-1 L=101  moyenne=354.5
Meilleure tournée (RANG) : 1-3-8-7-6-4-5-2-1  L = 101

Optimum exact (vérification, 7! = 5040 tournées) : 1-2-4-5-6-7-3-8-1 L = 98
