#this is to import msql connector
import mysql.connector
import datetime

# Establishing the connection
connection = mysql.connector.connect(
    host="localhost",       # Replace with your database host
    user="your_username",   # Your MySQL username
    password="your_password",  # Your MySQL password
    database="your_database"   # Database name (optional)
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to the database")

# Close the connection
connection.close()

#this is the intro pageish thing for cafe
print("              Cafe Management System                 ")
print("--------------------wellcome-------------------------")
print(datetime.datetime.now())
print("""1.to make an order
      2.to view menu
      3.staff management
      4.exit""")
flag = 1
while flag ==1:
    inp=int(input("enter your command code: "))
    if inp == 1:
        print("make an  order")
    elif inp == 2:
        print("        menu        ")
    elif inp == 3:
        print("staff management")
        print("1.view staff list")
        print("2.search for an employee")
        print("3.add new employee")
        print("4.remove an employee")
    elif inp ==4:
        print("exit")
        flag = 0
        