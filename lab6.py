# Algorytm roju cząstek

# Wybiermay najlepszą cząsteczke z roju
# Każdą pozycje zapamiętujemy jako najlepszą pozycję tej cząsteczki
# Nadajemy im prędkości i kierunek
# Iterujemy przez wszystkie cząsteczki i modyfikujemy prędkość biorąc pod uwagę trzy czynniki
# V = a1 * v + a2 * c + a3 * r
# c - mądrość samej cząsteczki
# r - mądrość roju
# a3 * r(R-x)
# r - liczba losowa [0; 1]
# x = x + V
# Nadpisujemy cząsteczkę jeśli osiągnęła lepszą pozycję i wartość najlepszej cząsteczki

# V = p1 * V + p2 * r1 (C - x) + p3 * r2 * (R - x)
# p2 - jak czasteczka ufa samej sobie
# r1 - liczba losowa
# p3 - jak ufam calemu rojowi

# 0.5, 2, 2
