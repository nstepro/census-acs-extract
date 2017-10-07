from census import Census
from us import states
import csv
import datetime

class censusAcsExtract():
    states="ALL"
    stats=[]
    apiKey=""

    def extractByZip(self):
        fipsData = getFipsSet(self.states)
        stats = getStats(self.stats)
        c = Census(self.apiKey)
        
        self.statData = c.acs5.zipcode(stats['apiInputs'], Census.ALL)
        outputData(self.statData, stats['statMap'], 'zip-' + str(len(self.stats)-1) + 'vars')

    def extractByTract(self):
        fipsData = getFipsSet(self.states)
        stats = getStats(self.stats)
        c = Census(self.apiKey)
        
        statData = []
        i=0
        while i<len(fipsData):
            ii=0
            while ii<len(fipsData[i]['counties']):
                print('Calling Census API for ' + fipsData[i]['counties'][ii]['fipsDescription'])
                
                thisStat = c.acs5.state_county_tract(stats['apiInputs'], fipsData[i]['fips'], fipsData[i]['counties'][ii]['fips'], Census.ALL)
                statData=statData+thisStat
                ii+=1
            i+=1
        
        outputData(statData, stats['statMap'], 'blockGroup-' + str(len(self.stats)-1) + 'vars')

    def extractByBlockGroup(self):
        fipsData = getFipsSet(self.states)
        stats = getStats(self.stats)
        c = Census(self.apiKey)
        
        statData = []
        i=0
        while i<len(fipsData):
            ii=0
            while ii<len(fipsData[i]['counties']):
                print('Calling Census API for ' + fipsData[i]['counties'][ii]['fipsDescription'])
                
                thisStat = c.acs5.state_county_blockgroup(stats['apiInputs'], fipsData[i]['fips'], fipsData[i]['counties'][ii]['fips'], Census.ALL)
                statData=statData+thisStat
                ii+=1
            i+=1
        
        outputData(statData, stats['statMap'], 'blockGroup-' + str(len(self.stats)-1) + 'vars')
                
        
        


def getStats(stats):
    stats.append(['NAME', 'Geography Name'])
    apiInputs = []
    statMap = {}
    i=0
    while i<len(stats):
        if not stats[i][0] == 'NAME':
            statMap[stats[i][0]]=stats[i][1]
        apiInputs.append(stats[i][0])
        i+=1
    return {'statMap': statMap, 'apiInputs': apiInputs}
        
    
def outputData(statData, statMap, fileTag):
    
    print('Beginning output of ' + str(len(statData)) + ' rows.')
    
    statHeaders = []
    for attr in statData[0]:
        if not attr in statMap:
            statHeaders.append(attr)
    fixedHeaders = statHeaders[:]
    statHeaders.append("Var ID")
    statHeaders.append("Var Name")
    statHeaders.append("Var Value")

    statRows = []
    for stat in statMap:
        i=0
        while i<len(statData):
            statRow=[]
            for h in fixedHeaders:
                statRow.append(statData[i][h])
            statRow.append(stat)
            statRow.append(statMap[stat])
            statRow.append(statData[i][stat])
            statRows.append(statRow)
            i+=1
    statOutput = [statHeaders]+statRows

    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fileName = fileTag + '-' + time + '.csv'
    with open('dataOutput/'+fileName, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(statOutput)
        
def getFipsSet(abbrev):
    stateList = {
    'AL': {'abbrev': 'AL', 'fips':'01', 'data': states.AL}, 
    'AK': {'abbrev': 'AK', 'fips':'02', 'data': states.AK}, 
    'AZ': {'abbrev': 'AZ', 'fips':'04', 'data': states.AZ}, 
    'AR': {'abbrev': 'AR', 'fips':'05', 'data': states.AR}, 
    'MO': {'abbrev': 'MO', 'fips':'29', 'data': states.MO}, 
    'MT': {'abbrev': 'MT', 'fips':'30', 'data': states.MT}, 
    'NE': {'abbrev': 'NE', 'fips':'31', 'data': states.NE}, 
    'MN': {'abbrev': 'MN', 'fips':'27', 'data': states.MN}, 
    'MS': {'abbrev': 'MS', 'fips':'28', 'data': states.MS}, 
    'MD': {'abbrev': 'MD', 'fips':'24', 'data': states.MD}, 
    'MA': {'abbrev': 'MA', 'fips':'25', 'data': states.MA}, 
    'MI': {'abbrev': 'MI', 'fips':'26', 'data': states.MI}, 
    'WI': {'abbrev': 'WI', 'fips':'55', 'data': states.WI}, 
    'WY': {'abbrev': 'WY', 'fips':'56', 'data': states.WY}, 
    'VA': {'abbrev': 'VA', 'fips':'51', 'data': states.VA}, 
    'WA': {'abbrev': 'WA', 'fips':'53', 'data': states.WA}, 
    'WV': {'abbrev': 'WV', 'fips':'54', 'data': states.WV}, 
    'KY': {'abbrev': 'KY', 'fips':'21', 'data': states.KY}, 
    'LA': {'abbrev': 'LA', 'fips':'22', 'data': states.LA}, 
    'ME': {'abbrev': 'ME', 'fips':'23', 'data': states.ME}, 
    'TX': {'abbrev': 'TX', 'fips':'48', 'data': states.TX}, 
    'UT': {'abbrev': 'UT', 'fips':'49', 'data': states.UT}, 
    'VT': {'abbrev': 'VT', 'fips':'50', 'data': states.VT}, 
    'SD': {'abbrev': 'SD', 'fips':'46', 'data': states.SD}, 
    'TN': {'abbrev': 'TN', 'fips':'47', 'data': states.TN}, 
    'IA': {'abbrev': 'IA', 'fips':'19', 'data': states.IA}, 
    'KS': {'abbrev': 'KS', 'fips':'20', 'data': states.KS}, 
    'OR': {'abbrev': 'OR', 'fips':'41', 'data': states.OR}, 
    'PA': {'abbrev': 'PA', 'fips':'42', 'data': states.PA}, 
    'RI': {'abbrev': 'RI', 'fips':'44', 'data': states.RI}, 
    'SC': {'abbrev': 'SC', 'fips':'45', 'data': states.SC}, 
    'OH': {'abbrev': 'OH', 'fips':'39', 'data': states.OH}, 
    'OK': {'abbrev': 'OK', 'fips':'40', 'data': states.OK}, 
    'FL': {'abbrev': 'FL', 'fips':'12', 'data': states.FL}, 
    'GA': {'abbrev': 'GA', 'fips':'13', 'data': states.GA}, 
    'CA': {'abbrev': 'CA', 'fips':'06', 'data': states.CA}, 
    'CO': {'abbrev': 'CO', 'fips':'08', 'data': states.CO}, 
    'CT': {'abbrev': 'CT', 'fips':'09', 'data': states.CT}, 
    'DE': {'abbrev': 'DE', 'fips':'10', 'data': states.DE}, 
    'DC': {'abbrev': 'DC', 'fips':'11', 'data': states.DC}, 
    'HI': {'abbrev': 'HI', 'fips':'15', 'data': states.HI}, 
    'ID': {'abbrev': 'ID', 'fips':'16', 'data': states.ID}, 
    'IL': {'abbrev': 'IL', 'fips':'17', 'data': states.IL}, 
    'IN': {'abbrev': 'IN', 'fips':'18', 'data': states.IN}, 
    'NC': {'abbrev': 'NC', 'fips':'37', 'data': states.NC}, 
    'ND': {'abbrev': 'ND', 'fips':'38', 'data': states.ND}, 
    'NV': {'abbrev': 'NV', 'fips':'32', 'data': states.NV}, 
    'NH': {'abbrev': 'NH', 'fips':'33', 'data': states.NH}, 
    'NJ': {'abbrev': 'NJ', 'fips':'34', 'data': states.NJ}, 
    'NM': {'abbrev': 'NM', 'fips':'35', 'data': states.NM}, 
    'NY': {'abbrev': 'NY', 'fips':'36', 'data': states.NY}}
    
    
    countyList = csv.reader(open("dataInput/counties.csv", "r"))
    counties = []
    
    for row in countyList:
        counties.append(row)
            
    countiesPrepped = []
    i=1
    while i<len(counties):
        row = {}
        for idx, col in enumerate(counties[0]):
            row[col] = counties[i][idx]
        countiesPrepped.append(row)
        i+=1
        
    output = []
    if abbrev=='ALL' or abbrev==['ALL']:
        for state in stateList:
            stateList[state]['counties'] = [a for a in countiesPrepped if a['abbrev'] in state]
            output.append(stateList[state])
    else:
        if not isinstance(abbrev, list):
            abbrev = abbrev.split(',')
        for state in abbrev:
            stateList[state]['counties'] = [a for a in countiesPrepped if a['abbrev'] in state]
            output.append(stateList[state])
    
    return output