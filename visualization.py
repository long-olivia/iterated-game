import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

gpt_basic_final = [322.872, 
             306.4719999999999, 
             191.40600000000003, 
             299.90200000000004, 
             273.70399999999995,
             206.74799999999996, 
             324.19000000000005,
             233.558,
             203.044]

claude_basic_final = [305.332,
                305.59199999999987,
                330.37600000000003,
                235.78200000000004,
                261.10400000000004,
                217.67799999999997,
                214.62,
                217.418,
                208.46400000000003]

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
plt.title("Average Final Points Accumulated, GPT-4o and Sonnet 4")
plt.bar(np.arange(len(gpt_basic_final)), gpt_basic_final, width=width, color='powderblue', label='GPT-4o')
plt.bar(np.arange(len(claude_basic_final)) + width, claude_basic_final, width=width, color='teal', label='Sonnet 4')
plt.xticks(x, labels, rotation=45, ha='right')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()
