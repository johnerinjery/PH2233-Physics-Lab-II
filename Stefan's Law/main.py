"""
PH2233 Physics Lab I — January 2026
Code used in lab for Stefan's Law experiment.
Refer Pg. 6 in the Lab Manual (LM)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from scipy.stats import linregress

alpha = 5.21e-3
beta = 7.2e-7
T_G = 800  # K

V = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
I = np.array([0.32, 0.44, 0.55, 0.64, 0.72, 0.78])

dV = 0.01  # volts
dA = 0.01  # amps

# Resistance Calculations
R = V / I
dR = R * np.sqrt((dV / V) ** 2 + (dA / I) ** 2)
R_0 = R[0] / (1 + alpha * T_G + beta * (T_G**2))


# Temperature Calculation
def temp_from_resistance(R):
    func = lambda T: R_0 * (1 + alpha * T + beta * T**2) - R
    return bisect(func, 300, 3000)


def temp_and_dt(R, dR):
    temp = temp_from_resistance(R)
    temp_p = temp_from_resistance(R + dR)
    temp_m = temp_from_resistance(R - dR)
    return temp, 0.5 * (temp_p - temp_m)


T = []
dT = []

for Ri, dRi in zip(R, dR):
    Ti, dTi = temp_and_dt(Ri, dRi)
    T.append(Ti)
    dT.append(dTi)

T = np.array(T)
dT = np.array(dT)

# Power Calculation
P = V * I
dP = P * np.sqrt((dV / V) ** 2 + (dA / I) ** 2)

# Plotting
logT = np.log(T)
logP = np.log(P)

dlogT = dT / T
dlogP = dP / P

plt.errorbar(logT, logP, xerr=dlogT, yerr=dlogP, fmt="o", capsize=3, label="Data")

slope, intercept, *_ = linregress(logT, logP)
xfit = np.linspace(min(logT), max(logT), 100)
yfit = slope * xfit + intercept

plt.plot(
    xfit, yfit, "r", label=f"Fit: slope = {slope:.2f}\ny-intercept = {intercept:.2f}"
)

plt.xlabel(r"$\log T$")
plt.ylabel(r"$\log P$")
plt.legend()
plt.show()

print(f"Slope = {slope:.2f}")
print(f"y-intercept = {intercept:.2f}")
