import csv
import numpy as np

# -----------------------------
# 1. Load dataset
# -----------------------------

file_path = "data/xy_data.csv"

x_values = []
y_values = []

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x_values.append(float(row["x"]))
        y_values.append(float(row["y"]))

x = np.array(x_values)
y = np.array(y_values)


# -----------------------------
# 2. Basic dataset information
# -----------------------------

print("===== DATASET INFORMATION =====")
print(f"Number of points : {len(x)}")
print(f"Number of columns: 2")
print(f"Columns          : x, y")


# -----------------------------
# 3. Check missing values
# -----------------------------

print("\n===== DATA QUALITY =====")
print(f"Missing x values: {np.isnan(x).sum()}")
print(f"Missing y values: {np.isnan(y).sum()}")


# -----------------------------
# 4. Summary statistics
# -----------------------------

print("\n===== SUMMARY STATISTICS =====")

print(f"x minimum : {x.min():.6f}")
print(f"x maximum : {x.max():.6f}")
print(f"x mean    : {x.mean():.6f}")
print(f"x std     : {x.std():.6f}")

print(f"\ny minimum : {y.min():.6f}")
print(f"y maximum : {y.max():.6f}")
print(f"y mean    : {y.mean():.6f}")
print(f"y std     : {y.std():.6f}")


# -----------------------------
# 5. Check duplicate points
# -----------------------------

points = np.column_stack((x, y))
unique_points = np.unique(points, axis=0)

print("\n===== DUPLICATES =====")
print(f"Total points : {len(points)}")
print(f"Unique points: {len(unique_points)}")
print(f"Duplicates   : {len(points) - len(unique_points)}")