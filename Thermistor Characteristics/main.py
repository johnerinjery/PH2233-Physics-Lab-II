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
R = np.array([...])
T = np.array([...])
dT = 0.5

x = np.log(R)
y = 1 / T
yerr = dT / T**2


# model function of 1/T we want to try fitting into. This method is prefered over np.polyfit as the latter try to fit into a square term as well.
def cubic_thermistor_model(R, A, B, C):
    x = np.log(R)
    return A + B * x + C * x**3


# we input the error in Temperature as well, which will be taken into account when calculating uncertainty in A, B, C
coeffs, cov = curve_fit(cubic_thermistor_model, R, y, sigma=yerr, absolute_sigma=True)
A, B, C = coeffs

# plotting the cubic curve
x_fit = np.linspace(x.min(), x.max(), 500)
y_fit = A + B * x_fit + C * (x_fit**3)

# plotting the data points
plt.errorbar(x, y, yerr=yerr, fmt="o", capsize=3, label="Data")
plt.plot(x_fit, y_fit, label=f"Best Fit : {A:.5f} + {B:.5f}x + {C:.5f}x³")

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
plt.legend()
plt.tight_layout()
plt.show()
