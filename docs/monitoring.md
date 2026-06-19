# Monitoring Plan

## Model Artifact Handling

The application loads the trained model from:

- models/random_forest.joblib

The model artifact is stored in the repository and deployed together with the application.

## Prediction Logging

Example log entry:

| Timestamp | Temperature | Humidity | CO₂ | Prediction |
|------------|------------|----------|-----|------------|
| 2026-06-19 12:00:00 | 25.0 | 60.0 | 800 | 13.16 |

## Monitoring Objectives

- Track incoming sensor values
- Monitor prediction trends
- Detect abnormal input values
- Identify potential model drift

## Retraining Triggers

Retraining should be considered when:

1. New production data becomes available
2. Input distributions differ significantly from training data
3. Prediction behavior changes noticeably
4. Model performance degrades on new observations