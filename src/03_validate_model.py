import csv
import numpy as np


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
# 2. Estimated parameters
# --------------------------------------------------

theta_deg = 29.99997293
M = 0.0299999969
X = 54.99999821

theta = np.deg2rad(theta_deg)


# --------------------------------------------------
# 3. Recover t from observed data
# --------------------------------------------------

t_observed = (
    (x - X) * np.cos(theta)
    + (y - 42) * np.sin(theta)
)


# --------------------------------------------------
# 4. Calculate predicted curve
# --------------------------------------------------

v_pred = np.exp(M * t_observed) * np.sin(0.3 * t_observed)

x_pred = (
    t_observed * np.cos(theta)
    - v_pred * np.sin(theta)
    + X
)

y_pred = (
    42
    + t_observed * np.sin(theta)
    + v_pred * np.cos(theta)
)


# --------------------------------------------------
# 5. Calculate point-wise errors
# --------------------------------------------------

x_error = x - x_pred
y_error = y - y_pred

point_distance = np.sqrt(
    x_error**2 + y_error**2
)


# --------------------------------------------------
# 6. Error metrics
# --------------------------------------------------

l1_distance = np.sum(point_distance)

mae = np.mean(point_distance)

rmse = np.sqrt(np.mean(point_distance**2))

max_error = np.max(point_distance)


# --------------------------------------------------
# 7. Residual statistics
# --------------------------------------------------

v_observed = (
    -(x - X) * np.sin(theta)
    + (y - 42) * np.cos(theta)
)

v_error = v_observed - v_pred


# --------------------------------------------------
# 8. Print validation results
# --------------------------------------------------

print("===== MODEL VALIDATION =====")

print(f"Number of observed points : {len(x)}")

print("\n===== L1 DISTANCE =====")
print(f"L1 distance : {l1_distance:.12f}")

print("\n===== ERROR METRICS =====")
print(f"MAE         : {mae:.12f}")
print(f"RMSE        : {rmse:.12f}")
print(f"Maximum     : {max_error:.12f}")

print("\n===== RESIDUAL STATISTICS =====")
print(f"Residual mean      : {np.mean(v_error):.12e}")
print(f"Residual MAE       : {np.mean(np.abs(v_error)):.12e}")
print(f"Residual RMSE      : {np.sqrt(np.mean(v_error**2)):.12e}")
print(f"Residual maximum   : {np.max(np.abs(v_error)):.12e}")


# --------------------------------------------------
# 9. Verify t range
# --------------------------------------------------

print("\n===== T RANGE =====")
print(f"Minimum t : {t_observed.min():.8f}")
print(f"Maximum t : {t_observed.max():.8f}")
print(f"Valid     : {np.all((t_observed > 6) & (t_observed < 60))}")