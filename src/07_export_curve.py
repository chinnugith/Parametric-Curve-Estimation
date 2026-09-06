import csv
import numpy as np

# Estimated parameters
theta_deg = 29.99997293
M = 0.0299999969
X = 54.99999821

theta = np.radians(theta_deg)

# Uniform t values
t = np.linspace(6, 60, 1500)

# Parametric curve
x = (
    t * np.cos(theta)
    - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)
    + X
)

y = (
    42
    + t * np.sin(theta)
    + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
)

# Save predicted curve
with open("results/fitted_curve.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["t", "x", "y"])

    for ti, xi, yi in zip(t, x, y):
        writer.writerow([ti, xi, yi])

print("Fitted curve saved to results/fitted_curve.csv")
print("Number of points:", len(t))
print("t range:", t.min(), "to", t.max())