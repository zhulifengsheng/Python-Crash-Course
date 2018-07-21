import requests
import pygal
from pygal.style import Style

language = 'c++'
url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
r = requests.get(url)
response_dict = r.json()

names, plot_dicts = [], []
for repo_dict in response_dict['items']:
	names.append(repo_dict['name'])
	
	description = repo_dict['description']
	if not description:
		description = "No description provided."
		
	plot_dict = {
		'value': repo_dict['stargazers_count'],
		'label': description,
		'xlink': repo_dict['html_url'],
		}
	plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.show_y_guides = False
my_config.truncate_label = 15
my_config.width = 1000

my_style = Style()
my_style.title_font_size = 24
my_style.label_font_size = 14


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred ' + language.title() + ' Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file(language + '.svg')
