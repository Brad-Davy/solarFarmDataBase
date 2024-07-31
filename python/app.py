import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import os 

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

#print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()

print(students)

fig = plt.figure()
plt.scatter(np.linspace(0, 2*np.pi, 100), np.sin(np.linspace(0, 2*np.pi, 100)))
plt.savefig('img/test.png')

