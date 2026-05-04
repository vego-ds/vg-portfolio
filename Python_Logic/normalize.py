"""Write normalize(values) that applies min-max normalization to a list of numbers, scaling all values to the range [0, 1]. This is one of the most common preprocessing steps before training ML models."""

def normalize(values):
   
    if not values:
        return []
    
    min_val = min(values)
    max_val = max(values)
    
    # Handle edge case where all values are identical
    if max_val == min_val:
        return [0.0] * len(values)  # or return values as-is, depending on your choice
    
    normalized = [(x - min_val) / (max_val - min_val) for x in values]
    return normalized

scores = [10, 20, 30, 40, 50]
print(normalize(scores))
# [0.0, 0.25, 0.5, 0.75, 1.0]

# Edge case: what if all values are identical?
print(normalize([5, 5, 5]))
# [0.0, 0.0, 0.0]  or return as-is — your choice, but handle it!
# Hint: formula is (x - min) / (max - min). Watch out for division by zero when max == min.

