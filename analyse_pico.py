# LEPL1502 - Projet 2
#
# Ce programme sert à récupérer des données du Picoscope afin de les
# plot sur un graphe
#
# Vincent Bauffe, 2020

import csv
import matplotlib
import matplotlib.pyplot as plt


def readFile(filename, offset=0):
    X, U = [], []
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        for row in reader:
            X.append(float(row[0])+offset*50)
            U.append(float(row[1]))
    return X, U


def plotSimpleData(key):
    plt.figure(dico[key][0])
    for filename in dico[key][1]:
        X, U = readFile(filename[0], filename[2])
        plt.plot(X, U, label=filename[1])
    plt.xlabel("Temps (µs)")
    plt.ylabel("Tension (V)")
    plt.grid()
    plt.legend()
    plt.show()


#####################################################
# Les paramètres
#####################################################

dico = {"inductance":   ("Frequence de resonnance",
                         [("indu60k.txt", "60 kHz", 0),
                          ("indu64k.txt", "64 kHz", 0),
                          ("indu70k.txt", "70 kHz", 0)]),
        "mutuelle":     ("Inductance mutuelle",
                         [("indumut50k.txt", "50 kHz", 0),
                          ("indumut58k.txt", "58 kHz", 0),
                          ("indumut65k.txt", "65 kHz", 0)]),
        "amplificateur": ("Amplificateur",
                          [("global64kPico_out.txt", "Sortie du picoscope", 0),
                           ("global64kAmpli_out.txt", "Sortie de l'ampli-op", 0)]),
        "tensionV3":    ("Tension V3",
                         [("global64kV3_SansIndu.txt", "V3 sans tag", 0),
                          ("global64kV3_AvecIndu1.txt",
                           "V3 avec tag 1", 0),
                          ("global64kV3_AvecIndu2.txt", "V3 avec tag 2", 0)]),
        "crete":        ("Crete",
                         [("global64kV3_AvecIndu1.txt",
                           "V5 avec tag 1", 0),
                          ("global64kV3_AvecIndu2.txt", "V5 avec tag 2", 0),
                          ("global64kV6_AvecIndu1.txt", "V6 avec tag 1", 0),
                          ("global64kV6_AvecIndu2.txt", "V6 avec tag 2", 0)]),
        "comparateur":  ("Comparateur",
                         [("global64kV6_AvecIndu1.txt", "V6 avec tag 1", 0),
                          ("global64kV6_AvecIndu2.txt", "V6 avec tag 2", 0),
                          ("global64kV6_SansIndu.txt", "V6 sans tag", 0),
                          ("global64kLED_AvecIndu.txt", "V8 avec tag", 0),
                          ("global64kLED_SansIndu.txt", "V8 sans tag", 0),
                          ("global64kVref_rouge.txt", "Vref1", 0),
                          ("global64kVref_verte.txt", "Vref2", 0)]),
        "global":       ("Circuit global",
                         [("global64KPico_out.txt", "Sortie du Picoscope", 0),
                          ("global64KAmpli_out.txt", "Sortie de l'ampli (V1)", 1),
                          ("global64KV3_SansIndu.txt", "V3 sans tag", 2),
                          ("global64KV3_AvecIndu1.txt", "V3 avec tag 1", 2),
                          ("global64KV3_AvecIndu2.txt", "V3 avec tag 2", 2),
                          ("global64KV6_SansIndu.txt", "V6 sans tag", 3),
                          ("global64KV6_AvecIndu1.txt", "V6 avec tag", 3),
                          ("global64kVref_rouge.txt", "Vref1", 3),
                          ("global64kVref_verte.txt", "Vref2", 3),
                          ("global64kLED_AvecIndu.txt", "V8 avec Indu", 4),
                          ("global64kLED_SansIndu.txt", "V8 sans tag", 4)])}

#####################################################
# Main
#####################################################

plotSimpleData("global")
