Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/malak/OneDrive/Documents/LSI 3/Algorithmes évolutionnaires/ex2 td2.py
Solution initiale (coin nord-ouest) : [[4, 4, 0], [0, 1, 8]]  coût = 55
Itération   1 : amélioration -> coût = 52

=== Résultat recherche taboue ===
      M1  M2  M3
D1    3    5    0
D2    1    0    8
Coût total minimal trouvé : 52
Optimum exact (PLNE)      : 52.0
>>> 
= RESTART: C:/Users/malak/OneDrive/Documents/LSI 3/Algorithmes évolutionnaires/ex3 td2.py
===== 1) RECHERCHE TABOUE =====
Solution initiale : 1-2-3-4-5-6-7-8-1  coût = 103
it  1 : échange (2, 3) -> 1-3-2-4-5-6-7-8-1  coût = 107  (meilleur = 103)
it  2 : échange (4, 5) -> 1-3-2-5-4-6-7-8-1  coût = 108  (meilleur = 103)
it  3 : échange (4, 6) -> 1-3-2-5-6-4-7-8-1  coût = 111  (meilleur = 103)
it  4 : échange (3, 8) -> 1-8-2-5-6-4-7-3-1  coût = 115  (meilleur = 103)
it  5 : échange (2, 7) -> 1-8-7-5-6-4-2-3-1  coût = 115  (meilleur = 103)
it  6 : échange (5, 6) -> 1-8-7-6-5-4-2-3-1  coût = 107  (meilleur = 103)
it  7 : échange (2, 3) -> 1-8-7-6-5-4-3-2-1  coût = 103  (meilleur = 103)
it  8 : échange (4, 5) -> 1-8-7-6-4-5-3-2-1  coût = 108  (meilleur = 103)
it  9 : échange (4, 6) -> 1-8-7-4-6-5-3-2-1  coût = 111  (meilleur = 103)
it 10 : échange (5, 6) -> 1-8-7-4-5-6-3-2-1  coût = 108  (meilleur = 103)
Meilleure solution : 1-2-3-4-5-6-7-8-1 coût = 103

===== 2) RECUIT SIMULÉ =====
Solution initiale : 1-2-3-4-5-6-7-8-1  coût = 103  T0 = 10.0
it 1 : T = 10.00 | voisin 1-2-5-4-3-6-7-8-1 coût = 112 | Δ = +9 | p = 0.407 -> accepté
it 2 : T = 8.00 | voisin 1-2-5-4-6-3-7-8-1 coût = 111 | Δ = -1 | p = 1.000 -> accepté
it 3 : T = 6.40 | voisin 1-2-5-7-6-3-4-8-1 coût = 126 | Δ = +15 | p = 0.096 -> refusé
it 4 : T = 5.12 | voisin 1-2-5-4-6-7-3-8-1 coût = 99 | Δ = -12 | p = 1.000 -> accepté
it 5 : T = 4.10 | voisin 1-2-5-4-7-6-3-8-1 coût = 105 | Δ = +6 | p = 0.231 -> refusé
Meilleure solution : 1-2-5-4-6-7-3-8-1 coût = 99

===== Optimum exact (énumération) =====
1-2-4-5-6-7-3-8-1 coût = 98
