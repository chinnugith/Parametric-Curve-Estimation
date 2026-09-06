import csv
import numpy as np


# --------------------------------------------------
# 1. Load observed data
# --------------------------------------------------

x_values = []
y_values = []

with open("data/xy_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x_values.append(float(row["x"]))
        y_values.append(float(row["y"]))

x = np.array(x_values)
y = np.array(y_values)


# --------------------------------------------------
# 2. Estimated parameters
# --------------------------------------------------

theta_deg = 29.99997293
M = 0.0299999969
X = 54.99999821

theta = np.deg2rad(theta_deg)


# --------------------------------------------------
# 3. Recover t values from observed points
# --------------------------------------------------

t_observed = (
    (x - X) * np.cos(theta)
    + (y - 42) * np.sin(theta)
)


# --------------------------------------------------
# 4. Uniformly sample t
# --------------------------------------------------

n_points = len(t_observed)

t_uniform = np.linspace(
    t_observed.min(),
    t_observed.max(),
    n_points
)


# --------------------------------------------------
# 5. Generate predicted curve
# --------------------------------------------------

wave = (
    np.exp(M * t_uniform)
    * np.sin(0.3 * t_uniform)
)

x_uniform = (
    t_uniform * np.cos(theta)
    - wave * np.sin(theta)
    + X
)

y_uniform = (
    42
    + t_uniform * np.sin(theta)
    + wave * np.cos(theta)
)


# --------------------------------------------------
# 6. Sort observed points by recovered t
# --------------------------------------------------

order = np.argsort(t_observed)

x_sorted = x[order]
y_sorted = y[order]

t_sorted = t_observed[order]


# --------------------------------------------------
# 7. Interpolate observed coordinates
#    onto the uniform t grid
# --------------------------------------------------

x_interp = np.interp(
    t_uniform,
    t_sorted,
    x_sorted
)

y_interp = np.interp(
    t_uniform,
    t_sorted,
    y_sorted
)


# --------------------------------------------------
# 8. Calculate point-wise Euclidean distance
# --------------------------------------------------

distance = np.sqrt(
    (x_interp - x_uniform) ** 2
    + (y_interp - y_uniform) ** 2
)


# --------------------------------------------------
# 9. L1 distance
# --------------------------------------------------

L1 = np.sum(distance)

MAE = np.mean(distance)

RMSE = np.sqrt(np.mean(distance ** 2))

maximum = np.max(distance)


# --------------------------------------------------
# 10. Print results
# --------------------------------------------------

print("===== UNIFORM-T VALIDATION =====")

print(f"Number of uniform samples : {n_points}")

print(f"t minimum : {t_uniform.min():.8f}")
print(f"t maximum : {t_uniform.max():.8f}")

print("\n===== ASSIGNMENT L1 METRIC =====")

print(f"L1 distance : {L1:.12f}")

print("\n===== ADDITIONAL METRICS =====")

print(f"MAE         : {MAE:.12f}")
print(f"RMSE        : {RMSE:.12f}")
print(f"Maximum     : {maximum:.12f}")