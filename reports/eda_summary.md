# EDA Summary Report

## Dataset Overview

* Total Records: 100
* Total Columns: 5
* Date Range: 2026-06-01 08:00:00 to 2026-06-05 11:00:00
* Sampling Frequency: Approximately 1 hour between consecutive observations

## Data Quality Report

### Summary Statistics

| Metric | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Yield (kg) |
| ------ | ---------------- | ------------ | --------- | ---------- |
| Mean   | 24.84            | 85.10        | 905.21    | 13.09      |
| Min    | 21.10            | 77.00        | 641.00    | 11.30      |
| Max    | 27.80            | 96.00        | 1208.00   | 14.75      |

### Data Quality Checks

* Temperature < 0: 0 violations
* Humidity < 0: 0 violations
* Humidity > 100: 0 violations
* CO₂ < 0: 0 violations
* Yield < 0: 0 violations

All records passed the validation checks, indicating that the dataset is clean and suitable for analysis.

### Distribution Analysis

The mean yield (13.09 kg) and median yield (13.04 kg) are very close, indicating minimal skewness in the yield distribution. The yield standard deviation is approximately 0.71 kg, suggesting sufficient variability for predictive modeling.

## Correlation Analysis

A correlation matrix was generated to examine relationships between environmental variables and mushroom yield.

| Variable    | Correlation with Yield |
| ----------- | ---------------------- |
| Temperature | -0.17                  |
| Humidity    | -0.02                  |
| CO₂         | 0.00                   |

The results indicate weak linear relationships between the environmental variables and yield.

## Key Insights

1. Average mushroom yield was 13.09 kg, with values ranging from 11.30 kg to 14.75 kg.
2. Temperature showed a weak negative correlation with yield, suggesting slightly lower yields at higher temperatures.
3. Humidity exhibited almost no linear relationship with yield within the observed range.
4. CO₂ concentration showed negligible correlation with yield in this dataset.
5. The weak correlations suggest that yield may depend on nonlinear interactions among environmental variables rather than individual factors alone.
6. Additional data and advanced modeling techniques may help uncover more complex relationships.

## Generated Figures

The following visualizations were created and saved in the `reports/figures/` directory:

* correlation_heatmap.png
* humidity_vs_yield.png
* temperature_vs_yield.png
* co2_vs_yield.png

## Conclusion

The dataset passed all quality checks and contains sufficient variation in environmental conditions and yield measurements for exploratory analysis. Correlation analysis revealed only weak linear relationships between temperature, humidity, CO₂ concentration, and yield. The generated visualizations provide a foundation for feature selection and predictive modeling in subsequent stages of the project.


