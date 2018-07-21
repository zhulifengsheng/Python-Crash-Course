import pygal

from random_walk import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Randomwalk'
#pygal.Line(include_x_axis=False, include_y_axis=False)

xy_list = []
for (x, y) in zip(rw.x_values, rw.y_values):
	xy_list.append((x, y))
	
xy_chart.add('data', xy_list)

xy_chart.render_to_file('RandomWalk.svg')
