# Cross Validation Results

## Methodology

TimeSeriesSplit with 3 folds was used to evaluate model performance while preserving chronological order and preventing data leakage.

## Random Forest Cross-Validation

- Fold 1 MAE: 0.644
- Fold 2 MAE: 0.553
- Fold 3 MAE: 0.556
- Average CV MAE: 0.585

## Linear Regression Cross-Validation

- Fold 1 MAE: 0.670
- Fold 2 MAE: 0.467
- Fold 3 MAE: 0.573
- Average CV MAE: 0.570

## Overfitting Analysis

- Train MAE: 0.208
- Test MAE: 0.883

The large gap between training and testing MAE indicates that the Random Forest model exhibits overfitting. The model learned the training data effectively but generalized less successfully to unseen data.

## Conclusion

Linear Regression achieved a slightly lower average CV MAE (0.570) than Random Forest (0.585), indicating marginally better predictive performance on this dataset. Random Forest provided useful feature importance insights but showed signs of overfitting.
