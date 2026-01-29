## Task 2: Model Debugging & Stability

### Problem Observed
The model produced unstable results across multiple runs and inconsistent predictions.

### Root Cause
- Random seed was not fixed
- Data leakage during preprocessing
- Inconsistent train-test splits

### Fixes Applied
- Fixed random seed for reproducibility
- Applied scaling only on training data

### Results
- Before Fix: Unstable F1 score (~0.03 - 0.08)
- After Fix: Stable F1 score (~0.56)

### Conclusion
After fixing randomness and preprocessing order, the model became stable and reliable.
