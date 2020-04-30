from math import pi, sqrt

# Définition des constantes
N = 60
l = 2.1e-2
A = 2.21e-3
r = 2.65e-2
mu = 4e-7 * pi
R1 = 150

# Gain de l'ampli op
# Gain = (R2 + R3) / R3
gain = 2.25
R2 = 330000
R3 = int(R2 / (gain - 1))
print("Gain de l'ampli op : R2 = {} ohm, R3 = {} ohm".format(R2, R3))

# Calcul de la valeur de l'inductance
L = mu * N**2 * A / l
print("Valeur de l'inductance : {:e} H".format(L))

# Inductance mutuelle calculée experimentalement
M = 0.5 * L
print("Valeur de l'inductance mutuelle : {:e} H".format(M))

# Calcul de la fréquence
# On a posé les capacités à 10nF
C = 10e-9
f = 1 / (2 * pi * sqrt(L * C))
print("Fréquence de résonance du circuit : {} Hz".format(f))

# Choix des résistances équivalentes
# Pour que Vx = 1/4 Vs
fraction1, fraction2 = 1/3, 3/5
Req1 = int((R1 * fraction1) / (1 - fraction1))
Req2 = int((R1 * fraction2) / (1 - fraction2))
print("Résistances équivalentes : Req1 : {} ohm, Req2 : {} ohm".format(Req1, Req2))

# Calcul des résistances du tag
omega = 2 * pi * f
RL0 = int((M * omega)**2 / Req1)
RL1 = int((M * omega)**2 / Req2)
print("Résistances du tag : RL0 : {} ohm, RL1 : {} ohm".format(RL0, RL1))
