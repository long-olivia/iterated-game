import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

gpt_discrim_final = [322.4219999999999,
                     295.77599999999984,
                     281.63999999999993,
                     305.4460000000001,
                     280.11,
                     219.52399999999997,
                     322.39,
                     270.124,
                     254.43999999999988]

claude_discrim_final = [279.082,
                        285.6159999999998,
                        286.2099999999999,
                        248.19600000000003,
                        268.63000000000005,
                        219.40399999999997,
                        245.1,
                        256.13399999999996,
                        252.05999999999992]

width=0.3
labels = ['Collective Collective', 
          'Collective Neutral', 
          'Collective Self', 
          'Neutral Collective', 
          'Neutral Neutral', 
          'Neutral Self', 
          'Self Collective', 
          'Self Neutral', 
          'Self Self']

x = np.arange(9)
plt.title("Average Final Points Accumulated, Name Condition")
plt.bar(np.arange(len(gpt_discrim_final)), gpt_discrim_final, width=width, color='powderblue', label='GPT-4o')
plt.bar(np.arange(len(claude_discrim_final)) + width, claude_discrim_final, width=width, color='teal', label='Sonnet 4')
plt.xticks(x, labels, rotation=-45, ha='left')
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
plt.legend()
ax = plt.gca()
y_major_step=10
ax.yaxis.set_minor_locator(mticker.MultipleLocator(y_major_step))
plt.tight_layout()
plt.show()