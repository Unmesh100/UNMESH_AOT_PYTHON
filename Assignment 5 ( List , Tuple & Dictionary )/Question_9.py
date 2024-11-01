sampleDict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}

# Filter out non-numeric values
numeric_values = {k: v for k, v in sampleDict.items() if isinstance(v, (int, float))}

# Find the key with the minimum value
min_key = min(numeric_values, key=numeric_values.get)

print("Key with the minimum value:", min_key)
