import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Rectangle
from tkinter import *
from sympy import  *
from scipy.optimize import fsolve


#Schaltkreis definieren
schaltkreis = [ 
        ('R', 100),
        ('C', 10e-2),
        ('L', 5e-3),

]

f = 20

def impedanzvon(komponent, frequenz):
	w = 2 * np.pi * f
	t, wert = komponent

	if t == 'R':
		return wert
	elif t == 'L':
		return 1j * w * wert
	elif t == 'C':
		return 1 / (1j * w * wert)


def gesamtimpedanz(f):
	z = 0
	for s in schaltkreis:
		z += impedanzvon(s, f)
	return z


def berechneresonanzfrequenz(f):
	return np.imag(gesamtimpedanz(f))

fres = fsolve(berechneresonanzfrequenz, 1000)[0]

print (fres)
