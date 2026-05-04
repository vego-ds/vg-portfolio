"""Write find_missing(rows) that scans a list of dicts and returns a dict showing how many None or empty-string values exist per column. This is your first step in any real data cleaning pipeline."""

def find_missing(rows):
    
    # Handle the case where rows is empty
    if not rows:
        return {}
    
    # Get the column names from the first row
    columns = rows[0].keys()
   
    # Initialize a dictionary to count missing values for each column
    missing_counts = {col: 0 for col in columns}

    # Scan each row and count missing values
    for row in rows:
        for col in columns:
            if row.get(col) is None or row.get(col) == '':
                missing_counts[col] += 1

    return missing_counts

# Test the function with the sample dataset

data = [
    {"name": "Alice", "age": 30,   "city": "Delhi"},
    {"name": "Bob",   "age": None, "city": ""},
    {"name": "Carol", "age": 28,   "city": None},
]

print(find_missing(data))
# {"name": 0, "age": 1, "city": 2}
