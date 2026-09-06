import numpy as np


# --------------------------------------------------
# Reference parameters
# --------------------------------------------------

theta_true_deg = 30.0
M_true = 0.03
X_true = 55.0


# --------------------------------------------------
# Estimated parameters
# --------------------------------------------------

theta_est_deg = 29.99997293
M_est = 0.0299999969
X_est = 54.99999821


# --------------------------------------------------
# Uniform t values
# --------------------------------------------------

t = np.linspace(6.0, 60.0, 1500)


# --------------------------------------------------
# Function to generate curve
# --------------------------------------------------

def generate_curve(theta_deg, M, X):

    theta = np.deg2rad(theta_deg)

    wave = np.exp(M * t) * np.sin(0.3 * t)

    x = (
        t * np.cos(theta)
        - wave * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + wave * np.cos(theta)
    )

    return x, y


# --------------------------------------------------
# Generate both curves
# --------------------------------------------------

x_true, y_true = generate_curve(
    theta_true_deg,
    M_true,
    X_true
)

x_est, y_est = generate_curve(
    theta_est_deg,
    M_est,
    X_est
)


# --------------------------------------------------
# Point-wise Euclidean distance
# --------------------------------------------------

distance = np.sqrt(
    (x_true - x_est) ** 2
    + (y_true - y_est) ** 2
)


# --------------------------------------------------
# Metrics
# --------------------------------------------------

L1 = np.sum(distance)

MAE = np.mean(distance)

RMSE = np.sqrt(np.mean(distance ** 2))

maximum = np.max(distance)


# --------------------------------------------------
# Results
# --------------------------------------------------

print("===== PARAMETER ACCURACY =====")

print(f"Reference theta : {theta_true_deg}")
print(f"Reference M     : {M_true}")
print(f"Reference X     : {X_true}")

print("\nEstimated parameters:")

print(f"Theta : {theta_est_deg}")
print(f"M     : {M_est}")
print(f"X     : {X_est}")

print("\n===== UNIFORM CURVE COMPARISON =====")

print(f"Number of samples : {len(t)}")
print(f"L1 distance       : {L1:.12e}")
print(f"MAE               : {MAE:.12e}")
print(f"RMSE              : {RMSE:.12e}")
print(f"Maximum distance  : {maximum:.12e}")