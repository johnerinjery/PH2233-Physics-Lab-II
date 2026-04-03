using Statistics
using Printf
include("definitions.jl")
include("data.jl")

# Free fall analysis
r = stat.(free_fall_times)
mean_time_fall = getindex.(r, 1)
std_err_time = getindex.(r, 2)
mean_free_fall_velocities = L ./ mean_time_fall
std_err_velocities = (L ./ mean_time_fall .^ 2) .* std_err_time
print("\nMean free fall times:\n", fmt_array(mean_time_fall), " s\n")
print("\nStandard errors:\n", fmt_array(std_err_time), " s\n")
print("\nMean free fall velocities:\n", fmt_array(mean_free_fall_velocities), " m/s\n")
print("\nStandard errors:\n", fmt_array(std_err_velocities), " m/s\n")

# Uncertainty in r

rad = radius.(mean_free_fall_velocities)
rad_err = uncertainty_r.(rad, std_err_velocities)

print("\nMean radius: ", fmt_array(rad), " m\n")
print("\nUncertainty in radius: ", fmt_array(rad_err), " m\n")

# forced rise analysis
r = stat.(rise_times)
mean_time = getindex.(r, 1)
std_err_time = getindex.(r, 2)
mean_rise_velocities = L ./ mean_time
std_err_velocities_rise = (L ./ mean_time .^ 2) .* std_err_time

print("\nMean rise velocities:\n", fmt_array(mean_rise_velocities), " m/s\n")
print("\nStandard errors:\n", fmt_array(std_err_velocities_rise), " m/s\n")

# Charge calculation from Dynamic method
q_dynamic = charge.(mean_free_fall_velocities, mean_rise_velocities, rad, V_rise)
q_dynamic_err = uncertainty_q.(q_dynamic, rad, mean_free_fall_velocities, mean_rise_velocities, V_rise, rad_err, std_err_velocities, std_err_velocities_rise, δV)

print("\nMean charge measured using dynamic method:\n", fmt_array_19(q_dynamic), " C\n")
print("\nStandard error in q using dynamic method:\n", fmt_array_19(q_dynamic_err), " C\n")

# Charge calculation using balancing method
q_static = charge_balance.(V_balance, rad)
q_balance_error = uncertainty_r_balance.(rad, rad_err, V_balance, δV)

print("\nMean charge measured using balance method:\n", fmt_array_19(q_static), " C")
print("\nStandard error in q using balance method:\n", fmt_array_19(q_balance_error), " C")

# value of n
print("\nValues of n (dynamic method):\n", fmt_array_n(q_dynamic), "\n")
print("\nValues of n (balance method):\n", fmt_array_n(q_static), "\n")