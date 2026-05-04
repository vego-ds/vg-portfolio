"""Write a function inspect_dataset(rows) that takes a list of dicts (like a mini CSV loaded into memory) and returns a summary dict with: total_rows, column_names, and a sample of the first 2 rows."""

def inspect_dataset(rows):
    
    # Handle the case where rows is empty (an empty dataset) and return the appropriate summary dict
    
    if not rows:
        return {
            "total_rows": 0,
            "column_names": [],
            "sample": []
        }
        
    # Get the column names from the first row (assuming all rows have the same structure)
    
    columns = list(rows[0].keys()) 
    
    # Get the first 2 rows as a sample)
    
    sample = rows[:2]  
    
    
    # Return the summary dict with total_rows, column_names, and sample
    
    return {
        "total_rows": len(rows),
        "column_names": columns,
        "sample": sample
    }
# Test the function with a sample dataset

data = [
    {"name": "Alice", "age": 30, "salary": 70000},
    {"name": "Bob",   "age": 25, "salary": 55000},
    {"name": "Carol", "age": 35, "salary": 90000},
]

print(inspect_dataset(data))
# {
#   "total_rows": 3,
#   "column_names": ["name", "age", "salary"],
#   "sample": [{"name": "Alice", ...}, {"name": "Bob", ...}]
# }