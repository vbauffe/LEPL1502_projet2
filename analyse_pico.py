# LEPL1502 - Projet 2
#
# Ce programme sert à récupérer des données du Picoscope afin de les
# plot sur un graphe
#
# Vincent Bauffe, 2020

import csv
import matplotlib
import matplotlib.pyplot as plt


def readFile(filename):
    X, U = [], []
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        for row in reader:
            X.append(float(row[0]))
            U.append(float(row[1]))
    return X, U


def plotSimpleData(index, xlab="Tension (V)", ylab="Temps (µs)"):
    plt.figure(dico[index][0])
    for filename in dico[index][1]:
        X, U = readFile(filename[0])
        plt.plot(X, U, label=filename[1])
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.grid()
    plt.legend()
    plt.show()


dico = {"inductance": ("Fréquence de résonnance",
                       [("indu60k.txt", "60 kHz"), ("indu64k.txt",
                                                    "64 kHz"), ("indu70k.txt", "70 kHz")]),
        "mutuelle": ("Inductance mutuelle",
                     [("indumut50k.txt", "50 kHz"), ("indumut58k.txt",
                                                     "58 kHz"), ("indumut65k.txt", "65 kHz")])}

#####################################################
# Main
#####################################################


# Mesure de l'inductance
plotSimpleData("inductance")

# Mesure de l'inductance mutuelle
plotSimpleData("mutuelle")
