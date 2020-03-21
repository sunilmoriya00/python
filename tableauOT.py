import json
import requests
from tableausdk import *
from tableausdk.HyperExtract import *

#Step 1 - call the OneTrust API 

headers = { 'APIKEY' : "c96427205ed420cc213078d8638af962"}
URL = 'https://uat.onetrust.com/api/inventory/v2/inventories/assets'
baseUrl = 'https://uat.onetrust.com/'
request = 'api/inventory/v2/inventories/assets'

#Step 2 - Create the table definition
schema = TableDefinition()
Columns = ["id","name"]
for column in Columns:
	schema.addColumn(column,Type.CHAR_STRING)

#step 3 - create the extract file 
filepath = r'/Users/sunilmoriya/Tableau/OneTrustAssetsExtract.hyper'

#Step 4 - get the number of pages to iterate

#response = requests.get(url = baseUrl + request + '?page=0', headers = headers)
newUrl = r'https://app.onetrust.com/api/consentmanager/v1/datasubjects/purposes'
response = requests.get(newUrl, headers = headers)
json_data = json.loads(response.text)
pagenumber = json_data["meta"]["page"]["totalPages"]

print (response)
print (json_data)
print (pagenumber)

#step 5 
tableName = 'Assets'

#step 6
tdefile = Extract(filepath)
table = tdefile.addTable('Extract', schema)
row = Row(schema)
for i in range (pagenumber):
	response = requests.get(url = baseUrl + request + '?page={}'.format(i),headers = headers)
	json_response = json.loads(response.text)
	for assets in json_response["data"]:
		row.setCharString(0,assets["id"])
		row.setCharString(1,assets["name"])
		table.insert(row)

#step 7

tdefile.close()