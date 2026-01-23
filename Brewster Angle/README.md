# Determination of Refractive Index by Brewster Angle Method

**Brewster's angle** (also known as the polarization angle) is the angle of incidence at which light with a particular polarization is **perfectly transmitted** through a transparent dielectric surface, with no reflection. When unpolarized light is incident at this angle, the light that is reflected from the surface is perfectly polarized. — _Wikipedia_

## Overview

Experimental setup is as given in the manual. You calculate 3 sets of intensity for the same set of angles to smooth out errors as the detector reading fluctuates a lot. We calculate average intensity at an angle, along with uncertainty, and plot it.

## Theory

**Polarization, Polarizer, Analyzer:**<br>
Here's a great video by a Scottish guy with a very heavy accent explaining polarizer and analyzer. Highly recommended watch before the experiment. Sir David Brewster was himself a Scottish guy after all, so it seems appropriate.

https://www.youtube.com/watch?v=Wqf1KufGGL4

Key things to note:

- Light is an EM Wave, with mutually perpendicular electric and magnetic waves. If we know the way either one is oriented, the other will always be in the orthogonal direction. Whenever we study polarization, we talk only about the plane of oscillation of the electric field.
- The electric fields in unpolarized light are oriented uniformly in all possible orientations. A polarizer only allows the electric fields along its axis to go through, thereby restricting the orientation of electric fields to a single plane — _polarizing_ it.
- A polarizer and an analyzer are made of the same material, the one the light passes through first is named polarizer, and the other the analyzer.
- The intensity of light after passing though the polarizer-analyzer setup depends on the relative orientation of their axes, a principle know as _Malu's Law_.

**S and P Polarizations:**

![s-p polarizations](pics/image.png)

- Take a look at the figure. Note incident ray, reflected ray, refracted ray and the normal. Also note that the incident ray has two mutually orthogonal electric field orientations (polarizations).
- The component of these that is parallel to the plane made by the normal and incident ray is called the P-polarized (parallel) component, and the other component is perpendicular to the plane (into the screen), and is called the S-polarized (_senkrecht_, German for 'perpendicular') component.
- The **figure is misleading**, it suggests that after reflection at any angle, the refracted ray would be completely P-polarized, and reflected is S-polarized. This is not so, the refracted wave is _always_ just partially polarized. It always has _some_ S-polarized part refracting along with the p. Similarly, the reflected wave is certainly _not_ purely S-polarized for all angles, there may be some P-polarized light along with it.
- **Brewster's angle** of incidence forms a special orientation of the incident, reflected and refracted ways such that the angle between the reflected and refracted ray becomes 90 deg. In this orientation, due to certain properties for which I will leave a footnote, The reflected wave becomes **fully** S-polarized, no P-polarized component will make it to the reflected wave. This is called _polarization by reflection_. Note that the refracted wave is still only partially polarized.
<p align="center">
<br>
  <img src="pics/image-2.png" alt="Brewster's angle" width="300">
</p>

**Experiment:**<br>
Keep in mind that P-polarized light just means that the electric field component oscillates in the plane formed by the normal vector and the direction of incident radiation — it is a geometric property of your arrangement.<br>In the experiment we:

- Initially use the polarizer-analyzer to make the light **fully** P-polarized.
- Now it is **fully** P-polarized light that meets at the air-glass interface. At any arbitrary angle we might not see anything special because the incoming P-polarized wave will get refracted and reflected in most cases.
- However, in **Brewster's angle** configuration, reflected wave will have zero intensity. In this configuration only S-polarized waves are reflected, but our incoming light does not contain any S-polarized waves. P-polarized waves are not reflected in this orientation. Hence there will be no reflection at all.

<p align="center">
<br>
  <img src="pics/image-3.png" alt="Brewster's angle" width="300">
</p>
From the image you can see that the reflection coefficient (proportional to how much of it is reflected) of P-polarized wave goes to zero at Brewster angle. We exploit this property in our experiment. We polarize the light into P-polarization, then adjust the system until the reflected intensity becomes zero, and we measure the angle of incidence in that configuration — this is Brewster's angle.
<br><br>
Using the fact that at Brewster angle the reflected and refracted ways are orthogonal, and approximating refractive index of air as unity, if you can calculate Brewster angle from experiment, you can apply Snell's Law at the glass-air interface to arrive at the following relation:

$$
n_{glass} = tan(\theta_{B})
$$

Where $\theta_{B}$ is Brewster's angle. And that is our experiment.

## Procedure

I thought I should drop a few points here, because the lab manual is rather lacking.<br>

![alt text](pics/image-4.png)

**Apparatus:**

- Detector on the left. Very fault. At least mine was. There are two settings — measure in milli amps or micro amps. You will be using micro amps. The actual detector is on the platform and is wired to the detector box.
- Laser setup on the right. Pretty straight forward, just connect the wire to the laser mounted on the platform and you're good to go.
- The "breadboard" it is said in the manual, I'll call it a platform — from right to left it consists of i) the laser ii) polarizer iii) analyzer iv) mini-platform which holds our glass slide in the center. The mini-platform has a smaller rotating platform within it - it is this that hold the glass slide. This inner platform has angular graduations of 2 deg least count. The detector is attached to the mini-platform, you can rotate it around as well, angular graduations of least count 1 deg is present.

1. Firstly, you need to use the polarizer-analyzer to make the incoming wave purely P-polarized. For a fixed orientation of the polarizer, rotate the analyzer till your transmitted light disappears. This means the axes of the polarizer and analyzer are perpendicular. Now rotate the analyzer 90 deg in any sense. You should see a transmitted beam of max intensity. Now rotate the analyzer and polarizer _together_ until the analyzer has its transmission axis lies in the plane of incidence. You can confirm by rotating 90 deg to get no transmission. (Honestly getting this thing aligned to have P-polarization is the most excruciating part of this whole deal) Remove the analyzer after you have aligned the polarizer. It is redundant now.

> Note: Since our alignment might not be _perfect_ there might still be some S-polarized waves in our incident beam. This might reflect from the glass slide and give non-zero intensity at Brewster angle. This is fine. Just take the angle at which intensity becomes minimum as Brewster angle.

2. You need to figure out how to measure angle of incidence. There are graduations on the rotating platform. You first send the reflected way back into the laser. Whatever reading you have now is what corresponds to 0 deg incidence. Take that reading as zero-error and proceed.

3. Use a file or something as a screen and just rotate you glass slide once — if you have aligned the polarizer properly you should be able to see where it becomes minimum. Start somewhere close to that value (see footnote). Step down by 2 deg in each measurement and note intensities. You will clearly see which angle corresponds to Brewster's angle (hint: it should be around 57 deg for glass)

4. Take 3 sets of values (atleast) for the same set of angles, plot the graph, error analysis and the rest.

## Notes

The calculations required in this experiment can be completely done on a software like Excel. I am including it mostly for completion. Do read the theory and experimental setup section — I clear some confusions I faced there.

Error is propagated as shown below:

$$
\delta n = sec^{2}(\bar{\theta})\times \delta \theta
$$

## Footnotes

1. The mathematics of it has to do with the Fresnel equations which describe light reflection and transmission at boundaries. There is an atomic picture as well, based on the difference of radiation of dipoles. The dipoles of our transparent medium align their axis along the direction of refracted ray, and in Brewster condition, they cannot support a reflection of P-polarized waves. Look at <a href="https://en.wikipedia.org/wiki/Polarization_(waves)">wikipedia </a> for more.
2. If we take measurements too far from Brewster angle, we wont be able to see a good fit to the curve. This is because Fresnel equations are hardly quadratic — but it is to a quadratic we are trying to fit our graph into. This wont work in general. But near a minima (or maxima) any function can be approximated to a quadratic (Taylor expansion) so it'll work if you take points sufficiently close to Brewster angle.
