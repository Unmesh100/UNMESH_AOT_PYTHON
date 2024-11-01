sampleDict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york" }

# Rename key 'city' to 'location'
sampleDict['location'] = sampleDict.pop('city')

print(sampleDict)
