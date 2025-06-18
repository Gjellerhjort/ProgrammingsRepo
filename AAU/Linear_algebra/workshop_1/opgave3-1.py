from sage.all import *

# Definér matricen A
# Delopgave 3(i): Matricen A
A = (1/8) * matrix(QQbar, 3, 3, [
    -1, 6, -3*sqrt(3),
    -6, -4, -2*sqrt(3),
    -3*sqrt(3), 2*sqrt(3), 5
])

# Find egenværdier og egenvektorer
eigenvalues_A = A.eigenvalues()
eigenvectors_A = A.eigenvectors_right()

# Udskriv resultater
print("Delopgave 3(i): Matricen A")
print("Egenværdier for A:", eigenvalues_A)
print("Egenvektorer for A:", eigenvectors_A)

# Find rotationsaksen (egenvektor for λ = 1)
for val, vecs, mult in eigenvectors_A:
    if val.real() == 1 and val.imag() == 0:
        rotation_axis = vecs[0]
        print("Rotationsakse (egenvektor for λ = 1):", rotation_axis)

# Delopgave 3(ii): Matricen B
B = (1/2) * matrix(QQbar, 3, 3, [
    2, 0, 0,
    0, 1, sqrt(3),
    0, sqrt(3), -1
])

# Find egenværdier og egenvektorer
eigenvalues_B = B.eigenvalues()
eigenvectors_B = B.eigenvectors_right()

# Udskriv resultater
print("\nDelopgave 3(ii): Matricen B")
print("Egenværdier for B:", eigenvalues_B)
print("Egenvektorer for B:", eigenvectors_B)

# Tjek dimensionen af egenrummet for λ = 1 og determinant
for val, vecs, mult in eigenvectors_B:
    if val.real() == 1 and val.imag() == 0:
        print("Multiplicitet af λ = 1:", mult)

det_B = B.det()
print("Determinanten af B:", det_B)

# Er B en rotationsmatrix?
if det_B == 1 and all(abs(val) == 1 for val in eigenvalues_B):
    print("B kan være en rotationsmatrix.")
else:
    print("B kan ikke være en ren rotationsmatrix, da determinanten ikke er 1 eller egenværdierne ikke alle har absolut værdi 1.")