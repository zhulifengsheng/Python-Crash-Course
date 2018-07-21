import requests
import pygal
from operator import itemgetter

URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(URL)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
count = 1
for submission_id in submission_ids[:30]:
	
	url = ('https://hacker-news.firebaseio.com/v0/item/' + 
			str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(count, ":", submission_r.status_code)
	count += 1
	response_dict = submission_r.json()
	
	submission_dict = {
		'label': response_dict['title'],
		'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
		'value': response_dict.get('descendants', 0),
		}
		
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), 
							reverse=True)

my_style = pygal.style.Style()

my_config = pygal.Config()
my_config.show_legend = False
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.add('', submission_dicts)
chart.render_to_file('17_2.svg')
