# Outlier Detection (First Principles)

This module implements the **Interquartile Range (IQR)** method for identifying statistical outliers. 

### Why from scratch?
While libraries like `scipy` or `pandas` can do this in one line, manual implementation ensures a deep understanding of:
* **Data Slicing:** Handling odd vs. even datasets correctly.
* **Medians:** Calculating middle points within subsets (Q1 & Q3).
* **The 1.5x Rule:** Implementing the mathematical "fences" that define anomalous data.

### How it works
The logic follows the standard statistical formula:
$$IQR = Q3 - Q1$$
Any value outside $[Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]$ is flagged.
