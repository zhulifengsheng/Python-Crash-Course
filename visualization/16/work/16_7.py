import csv

from pygal.maps.world import World
from country_codes import get_country_code

filename = 'H2O.csv'
with open(filename, encoding='UTF-8') as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	H2O_dict = {}
	for row in reader:
		try:
			country_name = row[0]
			value = float(row[58])
		except ValueError:
			print('Data missing')
		else:
			code = get_country_code(country_name)
			if code:
				H2O_dict[code] = value
			
wm = World()
wm.title = "H2O, by Country"
wm.add("2014", H2O_dict)

wm.	render_to_file('H2O.svg')		
	
	
	
