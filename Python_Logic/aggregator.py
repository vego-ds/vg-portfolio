"""
Write group_by(rows, key, agg_col) that groups a list of dicts by a given key column and returns the mean of agg_col for each group. This is the pure-Python version of what pandas .groupby().mean() does.

"""

def group_by(rows, key, agg_col):
    # 1. Use a dictionary to collect lists of values for each group
    groups = {}
    
    for row in rows:
        group_name = row[key]      # e.g., "North"
        value = row[agg_col]       # e.g., 200
        
        if group_name not in groups:
            groups[group_name] = []
        
        groups[group_name].append(value)
    
    # 2. Compute the mean for each group
    result = {}
    for group_name, values in groups.items():
        result[group_name] = sum(values) / len(values)
        
    return result

sales = [
    {"region": "North", "revenue": 200},
    {"region": "South", "revenue": 150},
    {"region": "North", "revenue": 300},
    {"region": "South", "revenue": 250},
    {"region": "East",  "revenue": 400},
]

print(group_by(sales, "region", "revenue"))
# Output: {"North": 250.0, "South": 200.0, "East": 400.0}