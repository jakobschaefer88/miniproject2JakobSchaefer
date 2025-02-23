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

os.makedirs("charts", exist_ok=True)

if not os.path.exists("NASCAR Champion History Dataset.csv"):
    print("Please download the dataset from https://www.kaggle.com/datasets/jakevdp/nascar-championship-data and save it as NASCAR Champion History Dataset.csv")
    exit()

driver = pd.read_csv("NASCAR Champion History Dataset.csv", index_col=0)

#Graph 1 - Champion Wins per year
plt.plot(driver["Year"], driver["Wins"])
plt.xlabel('Year')
plt.ylabel('Wins')
plt.title('NASCAR Champion Wins per Year')
plt.savefig("charts/champion_wins_per_year.png")

#Graph 2 - Champion Car Number per year
driver.plot.scatter(x="Year", y="Car Number", alpha=0.1)
plt.title('NASCAR Champion Car Number per Year')
plt.savefig("charts/champion_car_number_per_year.png")

#Graph 3 - Top 10 Drivers per Championship wins
driver_wins = driver["Driver"].value_counts()
driver_wins.head(10).plot(kind='bar')
plt.title('Top 10 Drivers per Championship wins')
plt.xlabel('Driver')
plt.ylabel('Championship Wins')
plt.ylim(0, 15)
plt.savefig("charts/top_10_drivers_per_championship_wins.png")

#Graph 4 - Number of Championships per Car Manufacturer
manufacturer_count = driver["Car Manufacturer"].value_counts()
manufacturer_count = manufacturer_count.sort_index()
manufacturer_count.plot(kind='bar')
plt.xlabel('Manufacturer')
plt.ylabel('Championship Wins')
plt.ylim(0, 40)
plt.title('Number of Championships per Car Manufacturer')
plt.savefig("charts/number_of_championships_per_car_manufacturer.png")

#Graph 5 - Percentage of number of wins in championship season
def func(pct, allSizes):
    pct / 100.*sum(allSizes)
    if pct > 5:  # Display percentage only if greater than 10%
        return f"{pct:.1f}%"
    else:
        return ""  # Empty string for smaller slices
driver_wins_season = driver['Wins'].value_counts()
plt.figure(figsize=(10,10))
driver_wins_season.plot(kind='pie', autopct=lambda pct: func(pct, allSizes=''), startangle=90,
                        textprops={'fontsize': 10}, labeldistance=1.05)
plt.title('Percentage of number of wins in championship season')
plt.savefig("charts/percentage_of_number_of_wins_in_championship_season.png")