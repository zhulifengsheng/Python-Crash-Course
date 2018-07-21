from die import Die

import pygal

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die_1.roll() * die_2.roll()
	results.append(result)
	
# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two 1,000 times."
hist.x_labels = [x for x in range(1, 37)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')
