"""
This module contains functions that output LaTeX formatted strings for the data and results of the experiment.
Copy-Paste to TeX file for report writing.
"""

using PrettyTables
using Printf
include("main.jl")
include("data.jl")

drops = ["Drop $i" for i in 1:8]

# free-fall-times mean-time std-err-time mean-fall-vel std-err-vel table
function format_free_fall_results(fall_times, mean_times, std_err_times, mean_velocities, std_err_velocities)
    headers = ["Drop", "Free Fall Times(s)", "Mean(s)", "S.E(s)", "Mean Vel(m/s)", "S.E Vel(m/s)"]
    fall_times_str = [join([@sprintf("%.2f", t) for t in times], ", ") for times in fall_times]
    fall_time_mean_str = string.(round.(mean_times, digits=2))
    fall_time_err_str = string.(round.(std_err_times, digits=2))
    fall_vel_mean_str = string.(fmt_array_plain(mean_velocities))
    fall_vel_err_str = string.(fmt_array_plain(std_err_velocities))
    data = hcat(drops, fall_times_str, fall_time_mean_str, fall_time_err_str, fall_vel_mean_str, fall_vel_err_str)
    print("Free-fall Data Analysis Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)

end

# mean-fall-vel std-err-vel mean-rad std-err-rad table
function format_radius_results(mean_vel, std_vel, mean_rad, std_rad)
    headers = ["Drop", "Mean Vel(m/s)", "S.E Vel(m/s)", "Mean Rad(m)", "S.E Rad(m)"]
    mean_vel_str = string.(fmt_array_plain(mean_vel))
    std_vel_str = string.(fmt_array_plain(std_vel))
    mean_rad_str = string.(fmt_array_plain(mean_rad))
    std_rad_str = string.(fmt_array_plain(std_rad))
    data = hcat(drops, mean_vel_str, std_vel_str, mean_rad_str, std_rad_str)
    print("Radius Calculation Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)
end

# rise-times mean-time std-err-time mean-rise-vel std-err-rise-vel table
function format_rise_results(rise_times, vrise, mean_times, std_err_times, mean_velocities, std_err_velocities)
    headers = ["Drop", "Rise Times(s)", "V", "Mean(s)", "S.E(s)", "Mean Vel(m/s)", "S.E Vel(m/s)"]
    rise_times_str = [join([@sprintf("%.2f", t) for t in times], ", ") for times in rise_times]
    rise_time_mean_str = string.(round.(mean_times, digits=2))
    rise_time_err_str = string.(round.(std_err_times, digits=2))
    rise_vel_mean_str = string.(fmt_array_plain(mean_velocities))
    rise_vel_err_str = string.(fmt_array_plain(std_err_velocities))
    data = hcat(drops, rise_times_str, vrise, rise_time_mean_str, rise_time_err_str, rise_vel_mean_str, rise_vel_err_str)
    print("Rise Data Analysis Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)
end

# balance-volt rad charge-balance charge-balance-err table
function format_balance_results(Vbalance, rad, q_balance, q_balance_err)
    headers = ["Drop", "V Balance(V)", "Radius(m)", "Charge(C)", "Charge S.E(C)"]
    Vbalance_str = string.(Vbalance)
    rad_str = string.(fmt_array_plain(rad))
    q_balance_str = string.(fmt_array_plain(q_balance))
    q_balance_err_str = string.(fmt_array_plain(q_balance_err))
    data = hcat(drops, Vbalance_str, rad_str, q_balance_str, q_balance_err_str)
    print("Balance Method Results Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)
end

# free-fall-vel rise-vel rad charge-dynamic charge-dynamic-err table
function format_dynamic_results(mean_free_fall_vel, mean_rise_vel, q_dynamic, q_dynamic_err)
    headers = ["Drop", "Mean Free Vel(m/s)", "Mean Rise Vel(m/s)", "Charge(C)", "Charge S.E(C)"]
    mean_free_fall_vel_str = string.(fmt_array_plain(mean_free_fall_vel))
    mean_rise_vel_str = string.(fmt_array_plain(mean_rise_vel))
    q_dynamic_str = string.(fmt_array_plain(q_dynamic))
    q_dynamic_err_str = string.(fmt_array_plain(q_dynamic_err))
    data = hcat(drops, mean_free_fall_vel_str, mean_rise_vel_str, q_dynamic_str, q_dynamic_err_str)
    print("Dynamic Method Results Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)
end

# q-dynamic n-dynamic q-balance n-balance table
function format_charge_comparison(q_dynamic, q_balance)
    headers = ["Drop", "Charge Dynamic(C)", "n Dynamic", "Charge Balance(C)", "n Balance"]
    q_dynamic_str = string.(fmt_array_19_plain(q_dynamic))
    n_dynamic_str = string.(fmt_array_n_plain(q_dynamic))
    q_balance_str = string.(fmt_array_19_plain(q_balance))
    n_balance_str = string.(fmt_array_n_plain(q_balance))
    data = hcat(drops, q_dynamic_str, n_dynamic_str, q_balance_str, n_balance_str)
    print("Charge Comparison Table:\n")
    pretty_table(data, column_labels=headers, backend=:latex)
end

format_free_fall_results(free_fall_times, mean_time_fall, std_err_time, mean_free_fall_velocities, std_err_velocities)
format_radius_results(mean_free_fall_velocities, std_err_velocities, rad, rad_err)
format_rise_results(rise_times, V_rise, mean_time, std_err_time, mean_rise_velocities, std_err_velocities_rise)
format_balance_results(V_balance, rad, q_static, q_balance_error)
format_dynamic_results(mean_free_fall_velocities, mean_rise_velocities, q_dynamic, q_dynamic_err)
format_charge_comparison(q_dynamic, q_static)