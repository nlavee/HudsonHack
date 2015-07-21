import csv
import json

f = open('nyc-public-school-locations-results.csv', 'rU')
csv_f = csv.reader(f)

next(csv_f)

list_schools = []

for row in csv_f:
	school_name = row[5]
	address = row[10]
	region = row[14]
	borough = row[2]
	principal = row[16]
	school = {}
	school['name'] = school_name
	school['principal'] = principal.title()
	#print school
	list_schools.append(school)

#with open('school_info.json', 'w') as outfile:
#    json.dump(list_schools, outfile)

print list_schools