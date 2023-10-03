import pandas as pd
df = pd.read_csv("iris_saved.csv")

import matplotlib.pyplot as plt
plt.plot(df['sepal_length'])
plt.title('Sepal-length-over-index')
plt.xlabel('index')
plt.ylabel('Sepal-length-(cm)')
plt.savefig('line_plot.png')

# histogram
plt.hist(df['sepal_length'], bins-10)
plt.ticks([4,5,6,7,8])
plt.title('Hisogram of sepal length')
plt.ylabel('frequency')
plt.savefig('histogram.png')

# pie chart
species_count = df['class'].value_counts()
plt.pie(species_count, labels=species_count.index, autopct='%1.1f%%')
plt.title('Species-distribution')
plt.savefig('pie_chart.png')

# scatter and subplot
fig, axs = plt.subplots(1,2, figsize=(12, 6))
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
markers = {'Iris-setosa': 'o', 'Iris-versicolor': 'x', 'Iris-virginica': 's'}

for species, group in df.groupby('class'):
    axs[0].scatter(group['sepal_length'], group['sepal_width'], color=colors[species], marker=markers[species], label=species)

axs[0].set_title('Sepal-length vs sepal width')
axs[0].set_xlabel('sepal-length(cm)')
axs[0].set_ylabel('sepal-widgth(cm)')
axs[0].legend()

for species, group in df.groupby('class'):
    axs[1].scatter(group['petal_length'], group['petal_width'], color=colors[species], marker=markers[species], label=species)
axs[1].set_title('Petal-length vs petal width')
axs[1].set_xlabel('petal-length(cm)')
axs[1].set_ylabel('petal-widgth(cm)')
axs[1].legend()
plt.tight_layout()
plt.savefig('scatter_plots.png')
