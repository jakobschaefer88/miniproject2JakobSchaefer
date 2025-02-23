'''
INF601 - Programming in Python
Assignment Mini Project 2
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''
### INF601 - Advanced Programming in Python
### Jakob Schaefer
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

driver = pd.read_csv("NASCAR Champion History Dataset.csv", index_col=0)
#print(driver["Wins"].describe())

#print(driver.head())

#Graph 1 - Champion Wins per year
plt.plot(driver["Year"], driver["Wins"])
plt.xlabel('Year')
plt.ylabel('Wins')
plt.title('NASCAR Champion Wins per Year')
plt.show()

#Graph 2 - Champion Car Number per year
driver.plot.scatter(x="Year", y="Car Number", alpha=0.1)
plt.title('NASCAR Champion Car Number per Year')
plt.show()

#Graph 3 - Number of Championships per Driver
championship_count = driver["Driver"].value_counts().head(10)
championship_count.plot()
plt.xticks(ticks=range(len(championship_count)), labels=championship_count.index, rotation=45, fontsize=10)
plt.xlabel('Driver')
plt.ylabel('Championship Wins')
plt.title('NASCAR Driver Championships')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Graph 4 - Number of Championships per Car Manufacturer
manufacturer_count = driver["Car Manufacturer"].value_counts()
manufacturer_count = manufacturer_count.sort_index()
manufacturer_count.plot(kind='bar')
plt.xlabel('Manufacturer')
plt.ylabel('Championship Wins')
plt.title('NASCAR Manufacturer Championships')
plt.show()

#Graph 5 -

