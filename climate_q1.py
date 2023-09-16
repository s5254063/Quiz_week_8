import matplotlib.pyplot as plt
import sqlite3
connection = sqlite3.connect(r"D:\University Study\2023\Tri 2\software tech\Quiz_week_8\climate.db")
cursor = connection.cursor()
years = []
co2 = []
temp = []

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cursor.fetchall())
cursor.execute("SELECT Year FROM climateData")
years = cursor.fetchall()
print(years)

cursor.execute("SELECT CO2 FROM climateData")
co2 = cursor.fetchall()
print(co2)

cursor.execute("SELECT Temperature FROM climateData")
temp = cursor.fetchall()
print(temp)



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
plt.savefig("co2_temp_1.png") 
