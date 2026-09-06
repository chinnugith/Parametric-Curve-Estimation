# Parametric Curve Estimation

## 1. Problem Statement

The objective of this assignment is to estimate the three unknown parameters:

- θ (theta)
- M
- X

from a given set of `(x, y)` points.

The points are generated from the following parametric curve:

x(t) = t cos(θ) - e^(M|t|) sin(0.3t) sin(θ) + X

y(t) = 42 + t sin(θ) + e^(M|t|) sin(0.3t) cos(θ)

The parameter constraints are:

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60

The goal is to find the values of θ, M, and X that best reproduce the given data points.

---

## 2. Dataset

The input dataset is stored in:

`data/xy_data.csv`

Dataset characteristics:

- Number of observations: 1500
- Number of variables: 2
- Variables: `x`, `y`
- Missing values: 0
- Duplicate points: 0

The data points are not required to be ordered by the parameter `t`, so the parameter corresponding to each point is recovered during the estimation process.

---

## 3. Mathematical Approach

Since the given range satisfies `t > 6`, we have:

|t| = t

Therefore, the equations can be written as:

x(t) = t cos(θ) - e^(Mt) sin(0.3t) sin(θ) + X

y(t) = 42 + t sin(θ) + e^(Mt) sin(0.3t) cos(θ)

To simplify the problem, a rotation and translation transformation is applied.

Define:

u = (x - X) cos(θ) + (y - 42) sin(θ)

v = -(x - X) sin(θ) + (y - 42) cos(θ)

Substituting the original equations gives:

u = t

and

v = e^(Mt) sin(0.3t)

Therefore, for a candidate set of parameters `(θ, M, X)`:

1. `t` can be recovered from `u`.
2. The transformed `v` value can be compared with `e^(Mt) sin(0.3t)`.
3. The parameters can be optimized to minimize the fitting error.

This transformation reduces the problem to fitting the relationship:

v = e^(Mt) sin(0.3t)

---

## 4. Parameter Estimation

The parameter estimation was implemented in Python using numerical optimization.

The optimization variables are:

- θ
- M
- X

The search is restricted to the parameter ranges specified in the assignment.

Differential Evolution was used as the optimization method because it performs global search within bounded parameter ranges.

The objective function measures the difference between:

v_observed

and

e^(Mt) sin(0.3t)

for the recovered values of `t`.

---

## 5. Estimated Parameters

The numerical optimization produced:

| Parameter | Estimated Value | Rounded Value |
|-----------|-----------------|---------------|
| θ | 29.99997293° | **30°** |
| M | 0.0299999969 | **0.03** |
| X | 54.99999821 | **55** |

Therefore, the final estimated parameters are:

**θ = 30°**

**M = 0.03**

**X = 55**

---

## 6. Parameter Constraints Validation

The estimated parameters satisfy all required constraints:

- 0° < 30° < 50°
- -0.05 < 0.03 < 0.05
- 0 < 55 < 100

The recovered parameter values for the data points were also within the required range:

- Minimum recovered `t` ≈ 6.0494
- Maximum recovered `t` ≈ 59.9952

Therefore:

6 < t < 60

is satisfied.

---

## 7. Model Validation

After estimating the parameters, each observed point was transformed back through the model to reconstruct its `(x, y)` coordinates.

The point-wise reconstruction results were:

| Metric | Value |
|--------|-------|
| L1 distance | 0.00383968 |
| MAE | 0.00000256 |
| RMSE | 0.00000349 |
| Maximum error | 0.00001762 |

The very small reconstruction errors indicate that the estimated parameters reproduce the observed data very closely.

A separate 1500-point uniform parameter comparison against the clean reference parameterization produced an L1 distance of approximately:

`0.02221`

This comparison was used as an additional parameter-accuracy validation.

---

## 8. Visualization

The fitted curve was generated using 1500 uniformly spaced values of `t` between 6 and 60.

The visualization compares the observed data points with the fitted parametric curve.

The fitted curve closely overlaps the observed data, confirming the quality of the estimated parameters.

An interactive visualization was also created using Desmos with:

θ = 30°

M = 0.03

X = 55

and:

6 ≤ t ≤ 60

---

## 9. Final Parametric Equation

Using the estimated parameters, the final curve is:

x(t) = t cos(30°) - e^(0.03t) sin(0.3t) sin(30°) + 55

y(t) = 42 + t sin(30°) + e^(0.03t) sin(0.3t) cos(30°)

for:

6 < t < 60

---

## 10. Project Structure

```text
Parametric-Curve-Estimation/
│
├── data/
│   └── xy_data.csv
│
├── src/
│   ├── 01_data_analysis.py
│   ├── 02_estimate_parameters.py
│   ├── 03_validate_model.py
│   ├── 04_uniform_l1.py
│   ├── 05_parameter_accuracy.py
│   ├── 06_save_results.py
│   ├── 07_export_curve.py
│   └── 08_create_visualization.py
│
├── results/
│   ├── parameter_results.json
│   ├── fitted_curve.csv
│   └── curve_visualization.html
│
└── README.md

## 11. How to Run

### 1. Clone the repository

```bash
git clone https://github.com/chinnugith/Parametric-Curve-Estimation.git
cd Parametric-Curve-Estimation
2. Create a virtual environment
python -m venv .venv
3. Activate the environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Run the analysis scripts
python src/01_data_analysis.py
python src/02_estimate_parameters.py
python src/03_validate_model.py
python src/04_uniform_l1.py
python src/05_parameter_accuracy.py
python src/06_save_results.py
python src/07_export_curve.py
python src/08_create_visualization.py
6. View the visualization

Open:

results/curve_visualization.html


### Section 12 — Tools

```markdown
## 12. Tools and Technologies

- Python 3.11
- NumPy
- SciPy
- Differential Evolution
- CSV
- HTML / SVG visualization
- Desmos for interactive visualization
- Git and GitHub
Final Conclusion
## 13. Conclusion

The unknown parameters of the given parametric curve were estimated using bounded numerical optimization.

The final estimated values are:

- θ = 30°
- M = 0.03
- X = 55

The recovered parameter range and reconstruction errors were also validated. The fitted curve closely matches the given data points, demonstrating that the estimated parameters provide a very good fit to the dataset.