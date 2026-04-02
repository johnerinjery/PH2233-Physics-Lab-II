import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

sns.set_theme(style="whitegrid")
lamb = np.array([460e-9, 500e-9, 540e-9, 570e-9, 635e-9])
freq = 299792458.0/lamb
d = [30, 33, 35, 40]
V_sets = [
    [1.08, 0.84, 0.73, 0.56, 0.35],
    [1.10, 0.86, 0.75, 0.57, 0.35],
    [1.10, 0.87, 0.76, 0.58, 0.36],
    [1.11, 0.90, 0.79, 0.59, 0.37]
]

e = 1.602e-19

fig, axes = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)

h_values = []

for i, (ax, V) in enumerate(zip(axes.flatten(), V_sets)):
    V = np.array(V)

    # regression (clean + stable)
    result = linregress(freq, V)
    m = result.slope
    b = result.intercept

    h = m * e
    h_values.append(h)

    # scatter
    sns.scatterplot(x=freq, y=V, ax=ax, label="data")

    # line
    ax.plot(freq, m*freq + b, label=f"fit (h ≈ {h:.2e})")

    ax.set_title(f"d = {d[i]} cm")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Stopping Potential (V)")
    ax.legend()

# stats
h_values = np.array(h_values)
h_mean = np.mean(h_values)
h_se = np.std(h_values) / np.sqrt(len(h_values))

print("Planck constant estimates:", h_values)
print("Mean h =", h_mean)
print("Standard error =", h_se)

plt.show()