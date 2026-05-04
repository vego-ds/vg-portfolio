#1. Outlier Detection (First Principles)

This module implements the **Interquartile Range (IQR)** method for identifying statistical outliers. 

# Why from scratch?
While libraries like `scipy` or `pandas` can do this in one line, manual implementation ensures a deep understanding of:
* **Data Slicing:** Handling odd vs. even datasets correctly.
* **Medians:** Calculating middle points within subsets (Q1 & Q3).
* **The 1.5x Rule:** Implementing the mathematical "fences" that define anomalous data.

# How it works
The logic follows the standard statistical formula:
$$IQR = Q3 - Q1$$
Any value outside $[Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]$ is flagged.

---

#2. Data Cleaning: Missing Value Detector (First Principles)

This module implements a custom scanner to identify and quantify missing
or empty data within a dataset — without using pandas or any data library.

# Why from scratch?

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

# How it works
The logic iterates through the dataset to calculate the **Missingness Ratio**:

$$\text{Missing Ratio} = \frac{\text{Total Nulls}}{\text{Total Data Points}} \times 100$$

If the percentage of missing values exceeds a specific threshold, the script flags the feature for manual review rather than automatic processing.

---

#3. Data Scaling: Min-Max Normalization (First Principles)

This module implements the **Min-Max Scaling** technique to transform numerical features onto a common scale of [0, 1]. This is a critical preprocessing step for algorithms sensitive to the magnitude of data, such as Gradient Descent or KNN.

### Why from scratch?
Implementing this manually ensures a deep understanding of:
* **Feature Scaling:** How to prevent features with larger raw values from dominating the model.
* **Edge Case Handling:** Implementing logic to prevent "Division by Zero" errors when all input values are identical ($max = min$).
* **Data Integrity:** Ensuring the transformation is linear and preserves the relative relationships between data points.

# How it works
The logic applies the following transformation to each value $x$:

$$\text{Normalized Value} = \frac{x - \min(values)}{\max(values) - \min(values)}$$

If $\max = \min$, the function defaults to returning $0.0$ for all entries to maintain a consistent scale.

---

# Data Analysis: Custom Aggregator & Inspector

These modules provide the essential tools for summarizing and auditing datasets using pure Python logic.

#4. Group-By Aggregator 
This mimics the core functionality of `pandas.groupby().mean()` to summarize numerical data across categories.

# Why from scratch?
* **Dictionary Logic:** Mastering how to use hash maps (Python dicts) to bucket data points efficiently.
* **Mean Calculation:** Implementing the two-step process of collection and reduction without external math libraries.

# How it works
The function uses a dictionary to map unique keys to lists of values, then reduces those lists using:
$$\text{Group Mean} = \frac{\sum \text{Group Values}}{\text{Count of Group Values}}$$

---

#5. Dataset Inspector 
A diagnostic tool used to generate a metadata summary of any list-of-dictionaries dataset.

# Why from scratch?
* **Schema Discovery:** Automatically identifying "Column Names" by inspecting dictionary keys.
* **Metadata Auditing:** Quickly validating the size and structure of a dataset before processing.

# How it works
It returns a summary object containing:
1. **Total Rows:** The length of the dataset.
2. **Column Names:** The keys extracted from the first data record.
3. **Samples:** A slice of the first two records for visual verification.