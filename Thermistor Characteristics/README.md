# Thermistor Characteristics

A **Thermistor** is a semiconductor type of resistor in which the resistance is strongly **dependent on temperature**. The varying resistance with temperature allows these devices to be used as temperature sensors, or to control current as a function of temperature. Some thermistors have **decreasing** resistance with temperature, while other types have **increasing** resistance with temperature. — _Wikipedia_

## Overview

In this experiment, we establish and verify the inverse temperature-resistance relationship of a thermistor, given by

$$
T^{-1} = A + B(\ln{R}) + C(\ln{R})^3
$$

By establishing coefficients $A$, $B$ and $C$. To do this, we heat up the thermistor in a water bath, note stable temperature with a mercury thermometer and corresponding resistance with a multimeter. We then fit the curve to an equation of the form given above and report the coefficients.

## Flow of the program

1. We have measured T values in Kelvin and corresponding R values.

2. We set `x = np.log(R)` as required from the relation.

3. We employ <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html">`scipy.optimize.curve_fit`</a> to fit the data points to a model we define beforehand. The function returns the required coefficients.

4. We plot the data points, and use the coefficients to plot the best fit curve.

## Notes

**Uncertainty Band**: When we calculate coefficients $A$, $B$ and $C$, there is some degree of uncertainty in the calculated values. This uncertainty is not just from error in measurement of temperature — which is indeed present, and we do include that — but also because our fitted curve depends on uncertain parameters, and we wanted to show how that parameter uncertainty propagates to the model prediction.

And yeah, Linear Regression also has an uncertainty band. We don't usually plot this for our experiments because well, usually we're after slope or intercept. Once we get that we're basically golden. Uncertainty bands are a bit more relevant here because the system itself is non linear.

**Disclaimer**: I _do not_ recommend anyone to plot the uncertainty band for pasting in the lab journal, nor do I recommend anyone to even mention it in your report. The math involved is quite painful, and I doubt most of us will be able to answer a viva question based on it. I kept it here simply for our awareness of it, and to appreciate the math.

The only other uncertainty is the error in temperature which is easily managed by

$$
\delta y = \frac{dT}{T^{2}}
$$
