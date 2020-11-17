import random
import matplotlib.pyplot as plt
import numpy as np

generated_values = []
positions = [0]
up_counter = 0
down_counter = 0
for i in range(0, 1001):
    generated_values.append(random.randrange(-1, 1))
for i in range(1, len(generated_values)):
    if generated_values[i] > -0.5:
        positions.append(positions[i - 1] + 1)
        up_counter += 1
    else:
        positions.append(positions[i - 1] - 1)
        down_counter += 1

rows = ('Min value', 'Max value', 'Abs (max-min)', 'Mean', 'Std', 'Steps up', 'Steps down')
columns = ['val']
mean = np.round(np.mean(positions), 2)
std = np.round(np.std(positions), 2)

cell_text = [
    [min(positions)], [max(positions)], [np.abs(max(positions) - min(positions))], [mean], [std], [up_counter],
    [down_counter]]

fig, axs = plt.subplots(2, 1)
axs[0].axis('tight')
axs[0].axis('off')
the_table = axs[0].table(cellText=cell_text, colLabels=columns, rowLabels=rows, loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(14)

x_axis = np.arange(len(positions))
axs[1].hlines(y=np.mean(positions), xmin=0, xmax=1000, color='r', label="Mean value")
axs[1].plot(x_axis, positions, label="Value")
axs[1].grid(True)
plt.ylabel('Value')
plt.xlabel('Step')
plt.legend()
plt.xlim([0, 1000])
plt.title("1D walk")

plt.show()
