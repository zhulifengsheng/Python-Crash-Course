import matplotlib.pyplot as plt

from die import Die

die_1 = Die()

results = []
for i in range(1000):
	results.append(die_1.roll())
	
frequencies = []
for value in range(1, 7):
	frequencies.append(results.count(value))

inputresults = [x for x in range(1, 7)]
plt.plot(inputresults, frequencies, linewidth=5)

plt.title("Results of a D6", fontsize=24)
plt.xlabel("Results", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
