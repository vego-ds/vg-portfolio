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


# Data Cleaning: Missing Value Detector (First Principles)

This module implements a custom scanner to identify and quantify missing
or empty data within a dataset — without using pandas or any data library.

### Why from scratch?

While `df.isnull().sum()` does this in one line, manual implementation
ensures a deep understanding of:

- **Custom Null Definitions:** Real-world missing data isn't always a
  clean `None`. Empty strings `""`, placeholders like `"N/A"`, or
  sentinel numbers like `-999` require explicit handling that standard
  libraries miss unless configured.
- **Defensive Key Access:** Using `row.get(col)` instead of `row[col]`
  prevents a `KeyError` crash when rows have inconsistent keys — which
  happens more than tutorials suggest.
- **Accumulator Pattern:** Initialising counters with a dict
  comprehension before scanning is a foundational Python pattern that
  appears throughout data pipelines, ML preprocessing, and beyond.

### How it works
The logic iterates through the dataset to calculate the **Missingness Ratio**:

$$\text{Missing Ratio} = \frac{\text{Total Nulls}}{\text{Total Data Points}} \times 100$$

If the percentage of missing values exceeds a specific threshold, the script flags the feature for manual review rather than automatic processing.