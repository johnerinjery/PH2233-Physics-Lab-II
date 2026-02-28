import numpy as np

# input values from experiment here

delta_m = 0.1       # g
delta_T = 0.1        # °C

m1 = 70          # g (cold water mass)
m2 = 72.3           # g (hot water mass)

T1 = 22.1            # °C (cold water temp)
T2 = 52.5            # °C (hot water temp)
Tf = 35.2            # °C (final temp)

ms = 62.5           # g (metal shots mass)
mw = 180.6           # g (water mass)

Ts = 97.6           # °C (shots temp)
Tw = 23.2           # °C (initial water temp)
Tm = 26.1            # °C (final temp)

mf = np.abs((m2 * (T2 - Tf) / (Tf - T1)) - m1)

# Equivalent Mass

d_mf_m2 = (T2 - Tf) / (Tf - T1)
d_mf_m1 = -1
d_mf_T2 = m2 / (Tf - T1)
d_mf_Tf = (-m2/(Tf - T1)) - (m2*(T2 - Tf)/(Tf - T1)**2)
d_mf_T1 = (m2*(T2 - Tf)/(Tf - T1)**2)

delta_mf = np.sqrt(
    (d_mf_m2 * delta_m)**2 +
    (d_mf_m1 * delta_m)**2 +
    (d_mf_T2 * delta_T)**2 +
    (d_mf_Tf * delta_T)**2 +
    (d_mf_T1 * delta_T)**2
)

print("Equivalent mass of flask (mf) =", mf, "g")
print("Uncertainty in mf =", delta_mf, "g")

# Specific Heat
cs = ((mw + mf) * (Tm - Tw)) / (ms * (Ts - Tm))

d_cs_mw = (Tm - Tw) / (ms * (Ts - Tm))
d_cs_mf = (Tm - Tw) / (ms * (Ts - Tm))
d_cs_ms = -((mw + mf) * (Tm - Tw)) / (ms**2 * (Ts - Tm))
d_cs_Ts = -((mw + mf)*(Tm - Tw)) / (ms*(Ts - Tm)**2)
d_cs_Tm = (
    (mw + mf)/(ms*(Ts - Tm))
    + ((mw + mf)*(Tm - Tw))/(ms*(Ts - Tm)**2)
)
d_cs_Tw = -((mw + mf) / (ms*(Ts - Tm)))

delta_cs = np.sqrt(
    (d_cs_mw * delta_m)**2 +
    (d_cs_mf * delta_mf)**2 +
    (d_cs_ms * delta_m)**2 +
    (d_cs_Ts * delta_T)**2 +
    (d_cs_Tm * delta_T)**2 +
    (d_cs_Tw * delta_T)**2
)

print("\nSpecific heat in SI =", cs*4184, "J/kgK")
print("Uncertainty in SI =", delta_cs*4184)
