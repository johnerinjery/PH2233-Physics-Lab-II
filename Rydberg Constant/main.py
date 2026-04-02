import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

nf = 2
ni = np.array([3 , 4, 5 ,6 ])

lambda_nm = np.array([656.3, 476.70, 450.91, 403.45])
lambda_si = lambda_nm * 1e-9

x = ((1/nf**2) - (1/ni**2))
y = 1/lambda_si

m, c, se = ((r := linregress(x, y)).slope, r.intercept, r.stderr)
x_ = np.linspace(x.min(), x.max(), 200)
y_ = m*x_ + c

plt.ylabel(r"$\frac{1}{\lambda}$ ($m^{-1}$)")
plt.xlabel(r"$\frac{1}{2^2} - \frac{1}{ni^2}$")
plt.plot(x_, y_, label=rf"Fit | Slope : {np.round(m, 4)} +/- {np.round(se, 4)}")
plt.scatter(x, y)
plt.legend()
plt.show()