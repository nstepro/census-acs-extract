# census-acs-extract
Simple method to query Census API for multiple ACS variables, multiple geographies.

### Example

Requires a Census API Key: https://www.census.gov/developers/
Also requires DataMade's Census tool: https://github.com/datamade/census

```python
import censusAcsExtract
e=censusAcsExtract.censusAcsExtract()
e.apiKey = "<MY API KEY>"
```
Set states to be included in the extract. Requires 2-digit abbreviations. Use "All" to extract for all US States.
```python
e.states = ['MA', 'NH'] 
```
Set ACS Variables and provide a friendly name for export. The \DataInput\ directory has the list of variables in an Excel sheet for reference.
```python
e.stats = [
    ['B25034_010E', 'Built 1940 to 1949'],
    ['B25034_011E', 'Built 1939 or earlier']
]
```
Call an extract function either by Zip, Tract or Block Group. Note: When calling Zip Codes, you cannot filter by State. All states will be returned regardless.
```python
e.extractByTract()
e.extractByZip()
e.extractByBlockGroup()
```
Results are exported to \DataOutput\ directory as a CSV file.