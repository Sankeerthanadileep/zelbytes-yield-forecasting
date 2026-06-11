diagnostics = """
# Linear Regression Diagnostics

## Model Performance

- MAE: 0.494
- RMSE: 0.573
- R²: -0.474

## Coefficient Interpretation

- Temperature (-0.156): Negative relationship with yield. Higher temperatures are associated with lower predicted yield.
- Humidity (-0.056): Weak negative relationship with yield.
- CO₂ (+0.012): Slight positive relationship with yield.

## Residual Analysis

Residual plots were generated for:
1. Residuals vs Predicted Yield
2. Residuals vs Humidity

The residuals did not indicate strong predictive performance. The negative R² score suggests that the linear regression model performs worse than predicting the mean yield of the test set.

## Findings

- Temperature appears to be the most influential feature.
- Humidity has a relatively weak influence.
- CO₂ shows only a small positive effect.
- The linear model does not adequately capture the relationship between environmental variables and yield.

## Recommendation

A more flexible model such as Random Forest Regression should be evaluated to capture potential nonlinear relationships between sensor readings and crop yield.
"""

with open("../reports/linear_diagnostics.md", "w") as f:
    f.write(diagnostics)

print("Diagnostics report saved.")