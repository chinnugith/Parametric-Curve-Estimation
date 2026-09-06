import csv
import numpy as np

# ============================================================
# 1. Load original data
# ============================================================

x_observed = []
y_observed = []

with open("data/xy_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x_observed.append(float(row["x"]))
        y_observed.append(float(row["y"]))

x_observed = np.array(x_observed)
y_observed = np.array(y_observed)


# ============================================================
# 2. Estimated parameters
# ============================================================

theta_deg = 29.99997293
M = 0.0299999969
X = 54.99999821

theta = np.radians(theta_deg)


# ============================================================
# 3. Generate fitted parametric curve
# ============================================================

t = np.linspace(6, 60, 1500)

x_fitted = (
    t * np.cos(theta)
    - np.exp(M * t) * np.sin(0.3 * t) * np.sin(theta)
    + X
)

y_fitted = (
    42
    + t * np.sin(theta)
    + np.exp(M * t) * np.sin(0.3 * t) * np.cos(theta)
)


# ============================================================
# 4. Create SVG visualization
# ============================================================

xmin = min(x_observed.min(), x_fitted.min())
xmax = max(x_observed.max(), x_fitted.max())
ymin = min(y_observed.min(), y_fitted.min())
ymax = max(y_observed.max(), y_fitted.max())

# Add some margin
xmargin = (xmax - xmin) * 0.05
ymargin = (ymax - ymin) * 0.08

xmin -= xmargin
xmax += xmargin
ymin -= ymargin
ymax += ymargin

width = 1000
height = 650

left = 80
right = 40
top = 70
bottom = 70

plot_width = width - left - right
plot_height = height - top - bottom


def transform_x(x):
    return left + (x - xmin) / (xmax - xmin) * plot_width


def transform_y(y):
    return top + (ymax - y) / (ymax - ymin) * plot_height


# Fitted curve polyline
curve_points = []

for xi, yi in zip(x_fitted, y_fitted):
    px = transform_x(xi)
    py = transform_y(yi)
    curve_points.append(f"{px:.2f},{py:.2f}")

curve_points_string = " ".join(curve_points)


# Observed points
observed_points = []

for xi, yi in zip(x_observed, y_observed):
    px = transform_x(xi)
    py = transform_y(yi)

    observed_points.append(
        f'<circle cx="{px:.2f}" cy="{py:.2f}" r="2" fill="black" opacity="0.45"/>'
    )

observed_points_string = "\n".join(observed_points)


# ============================================================
# 5. Build HTML
# ============================================================

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">

    <title>Parametric Curve Estimation</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 30px;
            background: #f5f5f5;
        }}

        .container {{
            max-width: 1100px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
        }}

        h1 {{
            text-align: center;
        }}

        .info {{
            text-align: center;
            margin-bottom: 20px;
        }}

        svg {{
            width: 100%;
            height: auto;
            border: 1px solid #ddd;
        }}

        .legend {{
            text-align: center;
            margin-top: 15px;
            font-size: 16px;
        }}
    </style>
</head>

<body>

<div class="container">

<h1>Parametric Curve Estimation</h1>

<div class="info">
    Estimated Parameters:
    <b>θ = 30°</b>,
    <b>M = 0.03</b>,
    <b>X = 55</b>
</div>

<svg viewBox="0 0 {width} {height}">

    <!-- Background -->
    <rect
        x="0"
        y="0"
        width="{width}"
        height="{height}"
        fill="white"
    />

    <!-- Grid -->
    <line
        x1="{left}"
        y1="{top + plot_height}"
        x2="{left + plot_width}"
        y2="{top + plot_height}"
        stroke="#888"
    />

    <line
        x1="{left}"
        y1="{top}"
        x2="{left}"
        y2="{top + plot_height}"
        stroke="#888"
    />

    <!-- Observed data points -->
    {observed_points_string}

    <!-- Fitted curve -->
    <polyline
        points="{curve_points_string}"
        fill="none"
        stroke="red"
        stroke-width="2.5"
    />

    <!-- Labels -->
    <text
        x="{width / 2}"
        y="35"
        text-anchor="middle"
        font-size="20"
        font-weight="bold"
    >
        Observed Data vs Fitted Parametric Curve
    </text>

    <text
        x="{width / 2}"
        y="{height - 15}"
        text-anchor="middle"
        font-size="16"
    >
        x
    </text>

    <text
        x="20"
        y="{height / 2}"
        text-anchor="middle"
        font-size="16"
        transform="rotate(-90 20 {height / 2})"
    >
        y
    </text>

</svg>

<div class="legend">
    ● Observed data points &nbsp;&nbsp;&nbsp;
    <span style="color:red;">━</span> Fitted parametric curve
</div>

</div>

</body>
</html>
"""


# ============================================================
# 6. Save HTML
# ============================================================

output_file = "results/curve_visualization.html"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(html)

print("Visualization created successfully.")
print("File:", output_file)
print("Observed points:", len(x_observed))
print("Fitted points:", len(x_fitted))