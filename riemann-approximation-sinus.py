import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Rectangle

resolution = 30


def getriemannaccuracy(resolution):
    wert = []
    i = 0
    # Evenly spacing the array of one period
    wert = (np.linspace(0, 2 * np.pi, resolution))

    # Sin on every element , DEG to RAD
    wert = np.sin(wert)

    # Multiplying every element by period length / resolution
    wert = abs(wert * ((np.pi * 2) / resolution))

    # Summing all the areas
    riemann = np.sum(wert)

    # Getting the accuracy
    accuracy = riemann / 4 * 100
    return accuracy


# Plot for the accuracy
xaxis = np.arange(1, 41)
yaxis = np.array([getriemannaccuracy(int(r)) for r in xaxis])

#Line for current accuracy
xline = np.array([0, 30])
yline = np.array([getriemannaccuracy(resolution), getriemannaccuracy(resolution)])

plt.figure()
plt.plot(xline, yline, linestyle = 'dotted')
plt.xlabel("Auflösung")
plt.ylabel("Genauigkeit der Riemann Summe [%]")
plt.plot(xaxis ,yaxis)


#Plot für den Sinus mit eingezeichnetem dings

xaxis2 = np.arange(0, 360 , 1)
yaxis2 = np.sin(xaxis2 / 180 * np.pi)
xaxis2points = np.linspace(0, 360 , resolution, endpoint=False)
yaxis2points = np.sin(xaxis2points / 180 * np.pi)

plt.figure()
plt.xlabel("Periode [°]")
plt.ylabel("Funktionswert Sinus")
plt.plot(xaxis2, yaxis2,)
plt.plot(xaxis2points, yaxis2points, 'o')
#Plotting Rectangles
width = 360 / resolution
for x, y in zip(xaxis2points, yaxis2points):
    rect = patches.Rectangle((x, 0), width, y, edgecolor='green', facecolor='lightblue')
    plt.gca().add_patch(rect)

plt.show()

