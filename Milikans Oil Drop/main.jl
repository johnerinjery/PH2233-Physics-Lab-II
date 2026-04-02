using Statistics
using Printf
include("definitions.jl")

fmt_array(arr) = join([@sprintf("%.3e", v) for v in arr], "\n ")

function stat(data)
    m = mean(data)
    std_err = std(data) / sqrt(length(data))
    return m, std_err
end

# Free fall analysis
free_fall_times = [[12.67, 12.6, 12.25], [7.79, 7.76, 7.67], [7.2, 7.07, 7.15], [4.3, 4.43, 4.46], [9.75, 10.32, 11.17], [7.17, 7.56, 7.71], [9.49, 8.76, 8.68], [4.15, 3.91, 4.15]] # (s)
r = stat.(free_fall_times)
mean_time = getindex.(r, 1)
std_err_time = getindex.(r, 2)
mean_free_fall_velocities = L ./ mean_time
std_err_velocities = (L ./ mean_time .^ 2) .* std_err_time

print("\nMean free fall velocities:\n", fmt_array(mean_free_fall_velocities), " m/s\n")
print("\nStandard errors:\n", fmt_array(std_err_velocities), " m/s\n")

# Uncertainty in r

function uncertainty_r(r, v_f_err)
    dC_dvf = -9 * η / (2 * g * (ρ - ρₐ))
    dr_dC = -1 / (2 * r + b / p)
    return dC_dvf * dr_dC * v_f_err
end

rad = radius.(mean_free_fall_velocities)
rad_err = uncertainty_r.(rad, std_err_velocities)

print("\nMean radius: ", fmt_array(rad), " m\n")
print("\nUncertainty in radius: ", fmt_array(rad_err), " m\n")

# forced rise analysis
rise_times = [[4.29, 4.3, 4.25], [10.8, 10.35, 10.14], [8.37, 8.79, 8.44], [7.32, 7.22, 7.16], [6.11, 6.03, 6.36], [13.97, 12.67, 12.49], [9.64, 9.70, 9.81], [9.6, 9.32, 10.3]] # (s)
V_rise = [933, 934, 588, 573, 933, 493, 427, 755] # (V)

r = stat.(rise_times)
mean_time = getindex.(r, 1)
std_err_time = getindex.(r, 2)
mean_rise_velocities = L ./ mean_time
std_err_velocities_rise = (L ./ mean_time .^ 2) .* std_err_time

print("\nMean rise velocities:\n", fmt_array(mean_rise_velocities), " m/s\n")
print("\nStandard errors:\n", fmt_array(std_err_velocities_rise), " m/s\n")

# Charge calculation from Dynamic method
q_dynamic = charge.(mean_free_fall_velocities, mean_rise_velocities, rad, V_rise)

function uncertainty_q(q, r, vf, vr, V_rise, delta_r, delta_vf, delta_vr, delta_V)

    A = 1 + b / (p * r)
    term_r = ((1 + 2b / (p * r)) / (A * r)) * delta_r
    term_vf = delta_vf / (vf + vr)
    term_vr = delta_vr / (vf + vr)
    term_V = delta_V / V_rise

    return q * sqrt(term_r^2 + term_vf^2 + term_vr^2 + term_V^2)
end

q_dynamic_err = uncertainty_q.(q_dynamic, rad, mean_free_fall_velocities, mean_rise_velocities, V_rise, rad_err, std_err_velocities, std_err_velocities_rise, δV)
print("\nMean charge measured using dynamic method:\n", fmt_array(q_dynamic), " C\n")
print("\nStandard error in q using dynamic method:\n", fmt_array(q_dynamic_err), " C\n")

# Charge calculation using balancing method
V_balance = [234, 525, 304, 357, 355, 316, 212, 549] # (V)
q_static = charge_balance.(V_balance, rad)

function uncertainty_r_balance(r, r_err, Vb, dV)
    r_term = (4 * π * r^2 * (ρ - ρₐ) * g * d * r_err) / Vb
    V_term = (-(4 / 3) * π * r^3 * (ρ - ρₐ) * g * d) * dV / (Vb^2)

    return sqrt(r_term^2 + V_term^2)
end

q_balance_error = uncertainty_r_balance.(rad, rad_err, V_balance, δV)
print("\nMean charge measured using balance method:\n", fmt_array(q_static), " C")
print("\nStandard error in q using balance method:\n", fmt_array(q_balance_error), " C")