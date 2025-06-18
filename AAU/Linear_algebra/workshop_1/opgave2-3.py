from sage.all import *

# Definér symboler
theta = var('theta')

# Definér Rx(theta) - en rotationsmatrix omkring x-aksen
Rx = matrix(SR, 3, 3, [
    [1, 0, 0],
    [0, cos(theta), -sin(theta)],
    [0, sin(theta), cos(theta)]
])

# Definér T og T^-1 over QQbar
T = (1/2) * matrix(QQbar, 3, 3, [
    [1, -sqrt(2), -1],
    [1, sqrt(2), -1],
    [sqrt(2), 0, sqrt(2)]
])

T_inv = (1/2) * matrix(QQbar, 3, 3, [
    [1, 1, sqrt(2)],
    [-sqrt(2), sqrt(2), 0],
    [-1, -1, sqrt(2)]
])

# (i) Tjek om T * T^-1 = I (identitetsmatricen)
identity_check = T * T_inv
print("T * T^-1 =\n", identity_check.simplify())  # Simplificér for at fjerne afrundingsfejl

# Beregn Ru(theta) = T * Rx(theta) * T^-1
Ru = (T * Rx * T_inv).simplify()
print("\nRu(theta) =\n", Ru)

# (ii) Bestem rangen og dimensionen af nulrummet for Ru(theta)
rank_Ru = Ru.rank()
nullity_Ru = 3 - rank_Ru
print("\nRang af Ru(theta):", rank_Ru)
print("Dimension af nulrummet for Ru(theta):", nullity_Ru)

# (iii) Find rotationsaksen for Ru(theta) (egenvektor for λ = 1)
eigenvectors_Ru = Ru.eigenvectors_right()
print("\nEgenvektorer for Ru(theta):", eigenvectors_Ru)

# Udvind u som egenvektor for λ = 1
u = None
for val, vecs, mult in eigenvectors_Ru:
    if val == 1:
        u = vecs[0]
        print("Rotationsakse (u) for Ru(theta):", u)
        # Verificér Ru(theta) * u = u
        Ru_u = (Ru * u).simplify()
        print("Ru(theta) * u =", Ru_u)
        break

if u is None:
    print("Ingen egenvektor fundet for λ = 1.")

# Tjek TRxT^-1 * u
if u is not None:
    TRxTinv_u = (T * Rx * T_inv * u).simplify()
    print("T * Rx(theta) * T^-1 * u =\n", TRxTinv_u)