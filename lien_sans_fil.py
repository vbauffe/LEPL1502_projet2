# LEPL1502 - Projet 2
#
# Ce programme sert à calculer les différentes valeurs du circuit
# rapidement lors de changement de variables
#
# Vincent Bauffe, 2020


from math import pi, sqrt

# Définition des constantes
mu = 4e-7 * pi
N = 80
r = 2.65e-2
k = 0.35e-3  # Epaisseur du fil
R1 = 150

# Gain de l'ampli op
# Gain = (R2 + R3) / R3
gain = 2.25
R2 = 310000
R3 = int(R2 / (gain - 1))
print("Gain de l'ampli op : R2 = {} ohm, R3 = {} ohm".format(R2, R3))

# Calcul de l'inductance réelle
C = 10e-9
f1 = f2 = 64000
L1 = L2 = 1 / (4*pi**2 * f1**2 * C)
print(f"Valeur réelle de l'inductance : L1 = L2 = {L1*1000:.4} mH")

# Calcul de la valeur de l'inductance théorique
S = pi * r**2
L = mu * N * S / k
print(f"Valeur théorique de l'inductance : L = {L*1000:.4} mH")

# Inductance mutuelle calculée experimentalement
# mesure = L1 + L2 + 2M -> M = (mesure - L1 - L2) / 2
fm = 58000
mesure = 1 / (4*pi**2 * fm**2 * C)
M = -(mesure - L1 - L2) / 2
print(f"Valeur de l'inductance mutuelle : {M*1000:.4} mH")

# Calcul de la fréquence
# On a posé les capacités à 10nF
f = 1 / (2 * pi * sqrt(L * C))
print(f"Fréquence de résonance théorique du circuit : {f/1000:.4} kHz")

# Choix des résistances équivalentes
# Pour que Vx = 1/4 Vs
fraction1, fraction2 = 1/3, 3/5
Req1 = int((R1 * fraction1) / (1 - fraction1))
Req2 = int((R1 * fraction2) / (1 - fraction2))
print(f"Résistances équivalentes : Req1 = {Req1} ohm, Req2 = {Req2} ohm")

# Calcul des résistances du tag
omega = 2 * pi * f
RL0 = int((M * omega)**2 / Req1)
RL1 = int((M * omega)**2 / Req2)
print("Résistances du tag : RL0 : {} ohm, RL1 : {} ohm".format(RL0, RL1))
