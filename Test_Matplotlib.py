import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabel=["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabel)
plt.legend(title = "For Fruits:")
plt.show() 