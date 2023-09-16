import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\University Study\2023\Tri 2\software tech\Quiz_week_8\climate.csv")


years = []
co2 = []
temp = []

years = df['Year']
#print(years)
co2 = df['CO2']
temp = df['Temperature']

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

