"""
PH2233 Physics Lab II — January 2026
Code used in lab for Brewster Angle experiment.
Refer Pg. 1 in the Lab Manual (LM)
"""

import numpy as np
import matplotlib.pyplot as plt

angle = np.array([36, 34, 32, 30, 28, 26, 24])
intensity1 = np.array([47, 26, 24, 2.5, 21, 44, 60])
intensity2 = np.array([44, 37, 23, 2.7, 22, 37, 69])
intensity3 = np.array([41.5, 27, 20, 2.7, 25, 37, 60])

intensities = np.vstack([intensity1, intensity2, intensity3])

I_mean = np.mean(intensities, axis=0)
I_std = np.std(intensities, axis=0, ddof=1)
I_err = I_std / np.sqrt(3)

# Quadratic weighted fit
coeffs = np.polyfit(angle, I_mean, 2, w=1 / I_err)
p = np.poly1d(coeffs)
xfit = np.linspace(angle.min(), angle.max(), 300)
yfit = p(xfit)

# Plots
fig, ax = plt.subplots()

ax.errorbar(
    angle,
    I_mean,
    yerr=I_err,
    fmt="o",
    capsize=4,
    zorder=3,
    label="Mean intensity ± SEM",
)

ax.plot(xfit, yfit, label="Weighted quadratic fit")

ax.set_xlabel("Angle (degrees)")
ax.set_ylabel("Intensity (mico amp)")
ax.grid()
ax.legend()
plt.show()

print(f"Mean of Intensities: {np.round(I_mean, 1)}")
print(f"Standard Deviation of Intensities: {np.round(I_std, 1)}")
print(f"Standard Error of Intensities: {np.round(I_err, 1)}")
