import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# input your values - default is just monte carlo
T = np.array([30, 40, 50, 60, 70, 80])          # Temperature (°C)
R = np.array([12.30, 12.34, 12.39, 12.43, 12.48, 12.53])  # Spherometer reading (mm)

# Instrument details
least_count = 0.01   # mm (spherometer least count)
L0 = 0.50            # Initial length of rod (m)
L0_unc = 0.001       # Uncertainty in L0 (m)

R0 = R[0]
delta_R = R - R0
delta_L = delta_R * 1e-3
delta_T = T - T[0]

delta_L_unc = least_count * 1e-3   # convert to meters

slope, intercept, r_value, p_value, std_err = stats.linregress(delta_T, delta_L)

print("Slope (dL/dT) =", slope, "m/°C")
print("Uncertainty in slope =", std_err)

alpha = slope / L0

# Error propagation
alpha_unc = alpha * np.sqrt((std_err/slope)**2 + (L0_unc/L0)**2)

print("Alpha =", alpha, "per °C")
print("Uncertainty in alpha =", alpha_unc)

plt.errorbar(delta_T, delta_L, 
             yerr=delta_L_unc,
             fmt='o', capsize=4)

plt.plot(delta_T, slope*delta_T + intercept)

plt.xlabel("Temperature Change (°C)")
plt.ylabel("Length Change (m)")
plt.title("Linear Expansion")

plt.grid()
plt.show()