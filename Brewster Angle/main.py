"""
PH2233 Physics Lab II — January 2026
Code used in lab for Brewster Angle experiment.
Refer Pg. 1 in the Lab Manual (LM)

P.S There really is no need to use a Python script for this experiment
as it can easily be done on software like Excel. I am including this j
ust for the sake of completeness.
"""

import numpy as np

theta_b = np.array([...])
theta_b = np.deg2rad(theta_b)

mean_theta = theta_b.mean()
std = theta_b.std(ddof=1)
std_mean = std / np.sqrt(len(theta_b))

n = np.tan(mean_theta)
n_err = (1 / np.cos(mean_theta) ** 2) * std_mean

print(f"Refractive Index: {n:.2f}\nUncertainty: {n_err:.2f}")
