# Michelson Interferometer

The Michelson interferometer is a common configuration for optical interferometry and was invented by the American physicist Albert Abraham Michelson in 1887. Using a beam splitter, a light source is split into two arms. Each of those light beams is reflected back toward the beamsplitter which then combines their amplitudes using the superposition principle. The resulting interference pattern that is not directed back toward the source is typically directed to some type of photoelectric detector or camera. For different applications of the interferometer, the two light paths can be with different lengths or incorporate optical elements or even materials under test. — _Wikipedia_.

<p align="center"> <img src="./docs/image.png" style="width:300"></p>

## Overview<br>

This experiment has two parts, firstly to determine the wavelength of a laser source, and secondly to determine the refractive index of air. The Michelson Interferometer setup splits the laser beam and makes them interfere again, creating a path difference between the interfering waves, and this creates fringes on the screen. As we vary the path length, we can observe the fringes shifting. The wavelength and refractive index can be calculated by using relations between number of fringes shifted and the path length changed.

## Theory<br>

**Measuring the calibration constant:**<br>
The calibration constant of a Michelson interferometer is the proportionality factor that relates the measurable fringe shift to a physical change in optical path length. When one mirror is displaced by a small distance Δx, the optical path difference changes by 2Δx, causing fringes to move; counting N fringes corresponds to a known path change Nλ. The calibration constant therefore connects mirror displacement (or an equivalent physical quantity like pressure or refractive index change) to the observed number of fringes, typically taking the form “fringes per unit displacement” or its inverse. Once determined using a known wavelength, this constant allows the interferometer to convert fringe counts into precise quantitative measurements.

**Measuring the wavelength of laser source** <br>

Using the calibration constant determined earlier, the wavelength of the laser is measured with a Michelson interferometer by relating mirror displacement to the observed fringe shift: when one mirror is displaced by $\Delta x$, the optical path difference changes by $2\Delta x$, and if $N$ fringes cross a fixed reference point, the condition $2\Delta x = N\lambda$ holds, giving the laser wavelength as $\lambda = \frac{2\Delta x}{N}$, with the calibration constant ensuring accurate conversion between mirror displacement and fringe count.

**Measuring the refractive index of air**

Using the calibration constant of the Michelson interferometer, the refractive index of air is measured by introducing a sealed gas cell in one arm and varying the air pressure inside it using a pressure gauge: a change in pressure alters the refractive index of air, producing a change in optical path length and hence a shift of interference fringes. If the gas cell has length $L$ and a change in refractive index $\Delta n$ causes $N$ fringes to cross the reference point, the optical path condition is $2L\,\Delta n = N\lambda$, allowing $\Delta n$ to be determined, and by correlating $\Delta n$ with the measured pressure change, the refractive index of air at different pressures can be accurately obtained.

## Procedure

In the docs, the official Holmarc manual is provided, with procedural steps with images better than what I can describe so please refer to that. One thing I will say, It is at times, very, _very_ difficult to get it to align properly. The experiment is basically done if you can get an interference pattern to appear.

## Footnote<br>

1. Here is the video link for the apparatus that we're using, you might wanna turn down your volume before playing this. https://www.youtube.com/watch?v=eIHixC_PUHQ
