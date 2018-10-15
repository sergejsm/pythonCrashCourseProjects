from random import randint
import pygal

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze results:
frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# Visualizing with Pygal
hist = pygal.Bar()
hist.title = "Results of rolling two Dices 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Two Dices', frequencies)
hist.render_to_file('die_visual.svg')