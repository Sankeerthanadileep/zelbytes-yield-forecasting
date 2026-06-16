# Model Comparison

| Model | Test MAE | Test RMSE | Test R² |
|---------|---------:|---------:|---------:|
| Linear Regression | 0.4939 | 0.5734 | -0.4740 |
| Default Random Forest | 0.8830 | 1.0263 | -0.2964 |
| Tuned Random Forest | 0.8336 | 0.9679 | -0.1530 |

## Champion Model

Linear Regression

## Justification

Linear Regression was selected as the champion model because it achieved the lowest test MAE (0.4939) and RMSE (0.5734) among all evaluated models. Although the tuned Random Forest obtained a higher R² score, its prediction errors were larger. Given the small dataset size (100 observations), the simpler Linear Regression model demonstrated better generalization and greater interpretability.

## Limitations

- The dataset contains only 100 observations.
- Limited training data may reduce model generalization.
- Predictions should be considered advisory and not a substitute for grower judgment.