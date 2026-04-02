using Plots
using Statistics
gr()

default(
    size=(1200, 900),          # overall figure size
    margin=10Plots.mm,         # padding around each subplot
    left_margin=12Plots.mm,
    right_margin=12Plots.mm,
    top_margin=10Plots.mm,
    bottom_margin=10Plots.mm,
    legendfontsize=10,
    guidefontsize=12,
    tickfontsize=9
)

# data
lambda = [460e-9, 500e-9, 540e-9, 570e-9, 635e-9]
freq = 299792458.0 ./ lambda

V_sets = [
    [1.08, 0.84, 0.73, 0.56, 0.35],
    [0.4, 0.9, 1.4, 1.9, 2.4],
    [0.3, 0.8, 1.3, 1.8, 2.3],
    [0.2, 0.7, 1.2, 1.7, 2.2]
]

e = 1.602e-19  # electron charge

plots = []
h_values = []

for (i, V) in enumerate(V_sets)

    # least squares using X \ y
    X = [freq ones(length(freq))]
    coeffs = X \ V
    m, b = coeffs

    h = m * e
    push!(h_values, h)

    p = scatter(freq, V,
        xlabel="Frequency (Hz)",
        ylabel="Stopping Potential (V)",
        title="d = $(i)",
        label="data"
    )

    plot!(p, freq, m .* freq .+ b,
        label="fit (h ≈ $(round(h, sigdigits=3)))"
    )

    push!(plots, p)
end

p_all = plot(plots..., layout=(2, 2), size=(1200, 900))
display(p_all)

# ---- statistics ----
h_mean = mean(h_values)
h_std = std(h_values)
h_se = h_std / sqrt(length(h_values))

println("Planck constant estimates: ", h_values)
println("Mean h = ", h_mean)
println("Standard error = ", h_se)