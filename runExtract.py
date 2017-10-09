import censusAcsExtract

e=censusAcsExtract.censusAcsExtract()

# Census API Key
e.apiKey = ""
# 2-Digit Abbreviations (Use "ALL" for all states)
e.states = ['MA'] 
# Set ACS Variables and provide a Friendly Name
e.stats = [
    ['B25034_010E', 'Built 1940 to 1949']
]

# Set call for Zip, Tract or Census Block Group

e.extractByTract()

# e.extractByZip()
# e.extractByBlockGroup
