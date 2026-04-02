"""
PH2233 Physics Lab II — January 2026
Code used in lab for Thermistor Characteristics experiment.
Refer Pg. 9 in the Lab Manual (LM)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# controls if an uncertainty band will be computed and plotted. Recommended False.
uncertainty_band = False

# fill temp in Kelvin here.
R = np.array([16.32,12.20,11.65,11.20,10.10,9.23,9.73,9.35,8.90,8.52,8.18,7.85,7.46,7.16,6.86,6.57,6.33,6.06,5.80,5.62,5.39,5.16,4.94,4.79,4.62,4.43,4.25,4.09,3.93,3.78,3.65,3.52,3.40, 3.27, 3.153, 3.043, 2.95])
T = np.array([19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50.1, 51, 52, 53, 54.1, 55, 56, 57, 58, 59, 60])

R2 = np.array([35.22,33.80,31.65,30.21,28.82,27.68,26.51,25.28,24,22.69,21.12,19.02,16.60,16.54,15.9,15.1,14,13.12,12.36,11.85,11.43,10.93,10.25,9.86,9.39,8.78,8.40,8.23,7.91,7.69,7.22,6.75,6.56,6.31,6.12,5.85,5.58,5.31,5.14,4.96,4.83,4.45,4.27,4.11,3.949,3.787,3.641,3.506,3.362,3.235,3.092,3,2.882])
T2 = np.array([5,6,7,8,9,10,11,12,13,14,15,16,17,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
dT = 0.1 

x = np.log(R)
T = T + 273.15
y = 1 / T
yerr = dT / T**2

x2 = np.log(R2)
T2 = T2 + 273.15
y2 = 1 / T2
yerr2 = dT / T2**2
# model function of 1/T we want to try fitting into. This method is prefered over np.polyfit as the latter try to fit into a square term as well.
def cubic_thermistor_model(R, A, B, C):
    x = np.log(R)
    return A + B * x + C * x**3


# we input the error in Temperature as well, which will be taken into account when calculating uncertainty in A, B, C
coeffs, cov = curve_fit(cubic_thermistor_model, R, y, sigma=yerr, absolute_sigma=True)
A, B, C = coeffs

coeffs2, cov2 = curve_fit(cubic_thermistor_model, R2, y2, sigma=yerr2, absolute_sigma=True)
A, B, C = coeffs2

# plotting the cubic curve
x_fit = np.linspace(x.min(), x.max(), 500)
y_fit = A + B * x_fit + C * (x_fit**3)

x_fit2 = np.linspace(x2.min(), x2.max(), 500)
y_fit2 = A + B * x_fit2 + C * (x_fit2**3)
# plotting the data points
#plt.errorbar(x, y, yerr=yerr, fmt="o", capsize=3, label="Heating")
#plt.plot(x_fit, y_fit, label=f"Best Fit : {A:.5f} + {B:.5f}x + {C:.5f}x³")

plt.errorbar(x2, y2, yerr=yerr2, fmt="o", capsize=3, label="Cooling")
plt.plot(x_fit2, y_fit2, label=f"Best Fit : {A:.5f} + {B:.5f}x + {C:.5f}x³")

if uncertainty_band:
    """
    This is just standard procedure when computing uncertainity band.
    The math behind this is kinda heavy, J is the Jacobian, np.einsum is the "Einstein Sum" over repeated indexes using a covariance matrix we get along with the coefficients in curve_fit.
    The diagonal elements of that matrix is the variance of the coefficients A B C, and the off diagonal elements is the covariance of pairs of coefficients.
    Don't really know how it works tbh; would NOT recommend including this for lab journal cause we'll probably not be able to answer all questions related to it. I just added it so we're aware about it, and to appreciate the math.
    """
    J = np.vstack([np.ones_like(x_fit), x_fit, x_fit**3]).T
    y_var = np.einsum("ij,jk,ik->i", J, cov, J)
    y_std = np.sqrt(y_var)
    plt.fill_between(
        x_fit, y_fit - y_std, y_fit + y_std, alpha=0.3, label="Fit uncertainty"
    )


plt.xlabel(r"$\ln R$")
plt.ylabel(r"$1/T\ \mathrm{(K^{-1})}$")
plt.title(r"$1/T$ vs $lnR$")
plt.legend()
plt.tight_layout()
plt.show()
