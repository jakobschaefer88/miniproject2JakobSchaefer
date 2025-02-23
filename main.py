import pandas as pd
import matplotlib.pyplot as plt

driver = pd.read_csv("NASCAR Champion History Dataset.csv", index_col=0)

print(driver.head())

driver.plot()

plt.show()