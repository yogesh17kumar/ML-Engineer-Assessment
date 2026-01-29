## Task 3: Model Performance Improvement

### Baseline Performance
The initial Logistic Regression model achieved an F1 score of approximately 0.56.

### Improvement Strategy
Threshold tuning was applied to adjust the classification decision boundary
from the default 0.5 to 0.3.

### Result
After threshold tuning, the F1 score improved to approximately 0.63,
achieving more than 10% improvement.

### Justification
Lowering the threshold increased recall for the positive class,
which improved the overall F1 score.
