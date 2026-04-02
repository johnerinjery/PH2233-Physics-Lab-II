# Defining Constants 
η = 1.81e-5  # Dynamic viscosity of air (Pa·s)
b = 6.17e-8  # Cunningham correction factor (m)
p = 1.01325e5  # Atmospheric pressure (Pa)
g = 9.81  # Acceleration due to gravity (m/s²)
ρₐ = 1.225  # Density of air at sea level (kg/m³)
ρ = 928 # Density of oil (kg/m³)
d = 5e-3 # Distance between the plates (m)
L = 1e-3 # Distance between reference lines (m)
δV = 3 # Least count of Voltmeter
# using this value of vf and the constants above, we can solve a quadratic to get the radius of the oil drop.

function radius(vf)
    B = b / p
    C = -(9 * η * vf) / (2 * g * (ρ - ρₐ))
    Δ = B^2 - 4 * C
    r = (-B + sqrt(Δ)) / 2
    return r
end

# Now there are two methods of doing this.
# Dynamic (using a rising terminal velocity), and a static method (where we balance the oil drop).

# rising terminal velocity (dynamic) method

function charge(vf, vr, r, V_rise)
    A = 1 + b / (p * r)
    q = (6 * π * η * r * (vf + vr) * d) / (V_rise * A)
    return q
end

# balanced (static) method

function charge_balance(V_balance, r)
    q = ((4 / 3) * π * r^3 * (ρ - ρₐ) * g * d) / V_balance
    return q
end