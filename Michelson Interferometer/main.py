import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

calib_const = 0.01773
GREEN_WAVELEN = 532e-9
d = 8.5e-2
dd = 1e-3
ATMOS_P = 101325

# Wavelenght of laser  beam
fringe_num = np.array([20, 25, 30, 35])
micrometer_dis = np.array([0.35, 0.45, 0.53, 0.63]) * 10e5
wavelenght = 2 * micrometer_dis * calib_const / fringe_num
print(wavelenght)
print(f"Mean wavelenght: {np.round(np.mean(wavelenght), 2)}")
print(
    f"Standard deviation in wavelenght: {np.round(std_wavelenght:=np.std(wavelenght), 2)}"
)
print(
    f"Standard error in wavelenght: {np.round(std_error:=std_wavelenght/ np.sqrt(len(wavelenght)), 2)}"
)

# Refractive index of air
fringe_num = np.array([9, 14, 10, 16])
pressure = np.array([20, 134, 90, 160])
res = linregress(pressure, fringe_num)
slope = res.slope
slope_err = res.stderr
n = 1 + slope * GREEN_WAVELEN * ATMOS_P / (2 * d)
n_err = n * np.sqrt(
    (
        slope_err * GREEN_WAVELEN * ATMOS_P / (2 * d) ** 2
        + (slope * GREEN_WAVELEN * ATMOS_P * dd / (2 * (d) ** 2))
    )
)
print("----------------------------------")
print(f"Slope : {np.round(slope, 2)}")
print(f"Slope error : {np.round(slope_err, 2)}")
print(f"Mean refractive index : {np.round(n, 3)}")
print(f"Uncertainty in refractive index : {np.round(n_err, 3)}")

plt.ylim(0, 20)
plt.xlim(0, 200)
plt.xlabel(r"$\Delta P$")
plt.ylabel("No. of fringes")
plt.scatter(pressure, fringe_num, zorder=3)
plt.plot(
    pressure,
    slope * pressure + res.intercept,
    label=f"Slope : {np.round(slope, 2)} +/- {np.round(slope_err, 2)}",
)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
