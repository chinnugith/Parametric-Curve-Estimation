import csv
import numpy as np
from scipy.optimize import differential_evolution


# --------------------------------------------------
# 1. Load the dataset
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
# 2. Define the objective function
# --------------------------------------------------

def objective(params):
    theta_deg, M, X = params

    # Convert degrees to radians
    theta = np.deg2rad(theta_deg)

    # Rotated coordinates
    u = (x - X) * np.cos(theta) + (y - 42) * np.sin(theta)

    v = -(x - X) * np.sin(theta) + (y - 42) * np.cos(theta)

    # Since 6 < t < 60, t is positive
    t = u

    # Predicted v
    v_pred = np.exp(M * t) * np.sin(0.3 * t)

    # Residual
    residual = v - v_pred

    # Penalize parameters producing invalid t values
    lower_violation = np.maximum(6 - t, 0)
    upper_violation = np.maximum(t - 60, 0)

    penalty = (
        np.mean(lower_violation ** 2)
        + np.mean(upper_violation ** 2)
    )

    return np.mean(residual ** 2) + 1000 * penalty


# --------------------------------------------------
# 3. Parameter bounds
# --------------------------------------------------

bounds = [
    (0.000001, 49.999999),   # theta
    (-0.049999, 0.049999),   # M
    (0.000001, 99.999999)    # X
]


# --------------------------------------------------
# 4. Run optimization
# --------------------------------------------------

result = differential_evolution(
    objective,
    bounds,
    seed=42,
    tol=1e-10,
    polish=True
)


# --------------------------------------------------
# 5. Extract estimated parameters
# --------------------------------------------------

theta_est, M_est, X_est = result.x


# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print("===== PARAMETER ESTIMATION =====")

print(f"Theta (degrees): {theta_est:.8f}")
print(f"M              : {M_est:.10f}")
print(f"X              : {X_est:.8f}")

print("\n===== OPTIMIZATION =====")
print(f"Objective value: {result.fun:.12e}")
print(f"Success        : {result.success}")
print(f"Message        : {result.message}")


# --------------------------------------------------
# 7. Recover t values and check the constraints
# --------------------------------------------------

theta = np.deg2rad(theta_est)

t_est = (
    (x - X_est) * np.cos(theta)
    + (y - 42) * np.sin(theta)
)

print("\n===== RECOVERED t RANGE =====")
print(f"Minimum t: {t_est.min():.8f}")
print(f"Maximum t: {t_est.max():.8f}")

print("\n===== CONSTRAINT CHECK =====")
print(f"6 < t < 60 : {np.all((t_est > 6) & (t_est < 60))}")