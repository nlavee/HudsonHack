import csv
import json

f = open('nyc-public-school-locations-results.csv', 'rU')
csv_f = csv.reader(f)

next(csv_f)

list_schools = []

for row in csv_f:
	#print row
	name_list = {}
	name = row[5]
	longitude = row[12]
	latitude = row[13]
	name_list['name'] = name
	geometry = {}
	geometry['type'] = "Point"
	geometry['coordinates'] = [longitude, latitude]
	geojson = {}
	name_list['type'] = "Feature"
	name_list['geometry'] = geometry
	if(row[2]):
		print row[2]
		name_list['borough'] = row[2]
	
	if(row[16]):
		print row[16]
		name_list['principal'] = row[16]
	address = str(row[10]).capitalize() + ", " + str(row[14])+ ", " + str(row[15]).capitalize()+""
	print address
	name_list['address'] = address
	list_schools.append(name_list)

##for school in list_schools:
##	print school

with open('school_loc.json', 'w') as outfile:
    json.dump(list_schools, outfile)