import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

T = np.array([78.6, 77.7, 76.8, 75.8, 74.9, 74, 73.1, 72.3, 71.6, 70.7])
t = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270])

plt.xlabel("Time (s)")
plt.ylabel("Temperature (deg celsius)")
plt.title("Cooling curve for Wood")
plt.scatter(t, T)
slope, intercept, r_value, p_value, std_err = linregress(t, T)
print(f"Slope : {slope:.4f} +/- {std_err:.4f}")
x = np.linspace(0, 270, 200)
y = slope*x + intercept
plt.plot(x, y, label=f"Slope : {slope:.4f} +/- {std_err:.4f}")
plt.legend()

# Measured values
m = 865.6
l = 2.66e-3
r = 5.05e-2
dTdt = np.abs(slope)
T1 = 74.5
T2 = 92.3
s = 0.380

# Uncertainties
dm = 0.1
dl = 0.01e-3
dr = 0.1e-3
ddTdt = std_err
dT1 = 0.1
dT2 = 0.1

# Compute k
DeltaT = T2 - T1
k = (m * s * l * dTdt) / (np.pi * r**2 * DeltaT)

# Uncertainty in DeltaT
dDeltaT = np.sqrt(dT1**2 + dT2**2)

# Relative uncertainty
rel_error = np.sqrt(
    (dm/m)**2 +
    (dl/l)**2 +
    (ddTdt/dTdt)**2 +
    (2*dr/r)**2 +
    (dDeltaT/DeltaT)**2
)

dk = k * rel_error

print("k =", k)
print("Uncertainty in k =", dk)
plt.show()