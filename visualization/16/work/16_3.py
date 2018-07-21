import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, means = [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			mean = int(row[5])
		except ValueError:
			print("Data missing")
		else:
			means.append(mean)
			dates.append(current_date)
		
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, means, c='red')

plt.title("Death", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
