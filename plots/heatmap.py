import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.random.randint(5,100,(5,5))

plt.figure(figsize=(10,10))
sns.heatmap(x,annot=True, cmap='coolwarm')

plt.show()
