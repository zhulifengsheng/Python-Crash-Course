import json

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.maps.world import World

from country_codes import get_country_code

filename = 'global_gdp.json'
with open(filename) as f:
	gdp_data = json.load(f)

cc_gdps = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == '2014':
		country_name = gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_gdps[code] = gdp

cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
	if gdp < 5000000000:
		cc_gdps_1[cc] = round(gdp / 1000000000)
	elif gdp < 50000000000:
		cc_gdps_2[cc] = round(gdp / 1000000000)
	else:
		cc_gdps_3[cc] = round(gdp / 1000000000)

print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Global GDP in 2014, by Country (in billions USD)'
wm.add('0-5bn', cc_gdps_1)
wm.add('5bn- 50bn', cc_gdps_2)
wm.add('>50bn', cc_gdps_3)

wm.render_to_file('global_gdp.svg')
