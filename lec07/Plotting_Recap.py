# Unsere Version von matplotlib generiert ein Fehler, wir müssen erst das richtige
# Backend aktivieren.
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.arange(1,10.01,0.01)
y = [i**3 for i in x]
plt.plot(x,y)
plt.show()


# Erzeugung eines Figurenobjekts
# Maximale Anzahl der Ticks
fig1,ax1 = plt.subplots()
ax1.set_title('Figure 2')
ax1.plot(x,y,label='x^3')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.xaxis.set_major_locator(plt.MaxNLocator(3))
ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
ax1.legend()
fig1.show()


# Spezifische Ticks
# Ticks als Vielfaches von einer Zahl
fig2,ax2 = plt.subplots()
ax2.set_title('Figure 3')
ax2.plot(x,y,label='x^3')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.xaxis.set_major_locator(plt.MultipleLocator(2))
ax2.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax2.yaxis.set_major_locator(plt.MultipleLocator(100))
ax2.legend()
fig2.show()


# Plot abspeichern
fig2.savefig("/Users/lucaslinden/Pythonkurs/plot.png")

# Seaborn save plot
tips = sns.load_dataset("tips")
scatter_plot = sns.scatterplot(data=tips, x="total_bill", y="tip")
fig3 = scatter_plot.get_figure()
fig3.savefig("/Users/lucaslinden/Pythonkurs/plot2.png")


