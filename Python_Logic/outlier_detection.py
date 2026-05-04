"""EDA · Statistics
Write find_outliers(values) that uses the IQR method to detect outliers. 
Calculate Q1 (25th percentile) and Q3 (75th percentile) manually, then flag any value outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR]. 
This is a common technique to identify extreme values that may skew your analysis or model training. Handle edge cases like small datasets gracefully."""


def find_outliers(values):
    # 1. Safety Check: You need at least 4 points to have a Q1 and Q3
    if len(values) < 4:
        return []
    
    # 2. Sort the data (Required for the IQR method)
    sorted_v = sorted(values)
    n = len(sorted_v)
    mid = n // 2
    
    # 3. Slice the data into two "Piles" (Lower and Upper halves)
    # If the list is odd, we skip the exact middle item to keep piles equal
    low_pile = sorted_v[:mid]
    high_pile = sorted_v[mid if n % 2 == 0 else mid + 1:]
    
    # 4. Helper to find the median of a pile
    # This ensures we get a fair middle even if the pile size is even
    def get_median(pile):
        length = len(pile)
        m = length // 2
        if length % 2 == 0:
            # Average the two middle numbers
            return (pile[m - 1] + pile[m]) / 2
        # Return the single middle number
        return pile[m]

    # 5. Calculate the "Box" boundaries
    Q1 = get_median(low_pile)
    Q3 = get_median(high_pile)
    
    # 6. Calculate the "Fences" using the 1.5x IQR rule
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # 7. Scan the original list and flag values outside the fences
    return [x for x in values if x < lower_bound or x > upper_bound]

# Test the function with a sample dataset
data = [10, 12, 11, 13, 9, 100, 11, 10, 12, -50]
print(f"Outliers detected: {find_outliers(data)}")
# Output: [100, -50]
