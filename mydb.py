import mysql.connector

# con = mysql.connector.connect(user="root", password="123456789", host="localhost")
# print(con)
#
# c = con.cursor()#cursor object used to execute sql queries/commands
# c.execute("create database schooldb")
# print("Database file created")

con = mysql.connector.connect(user="root", password="123456789", host="localhost", database="schooldb")
c = con.cursor()
# c.execute("create table student(roll_no int not null primary key,name varchar(20), age int, place varchar(20), phone int, total_mark int)")
# print("Table created successfully")
# c.execute('''insert into student values(101,"Phuwin",23,"Bangkok",98567897,89),
# (102,"Fourth",22,"Phuket",98567895,79),
# (103,"Satang",24,"Chaing Mai",98567897,88),
# (104,"Mark",25,"Bangkok",98567847,96),
# (105,"Gemini",22,"Bangkok",98567797,69);
# ''')

# query = 'insert into student values (%s,%s,%s,%s,%s,%s);'
# data = (106,'Joong',24,'Pattaya',98765444,67)
# c.execute(query,data)
# con.commit() #to save data permenantly inside db
# print("Records inserted successfully")

# READ OPERATION
# query = 'select * from student'
# c.execute(query)
# records = c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print('No records found')

# Read all attributes of a student with rollno = roll number entered by user
# roll = int(input("Enter a roll no: "))
# query = 'select * from student where roll_no = %s'
# data = (roll,)
# c.execute(query,data)
# records = c.fetchone()
# if records:
#     print(records)
# else:
#     print('No records found')

# Update mark of a student with roll no = roll no entered by user
# roll = int(input("Enter a roll no: "))
# mark = int(input("Enter new mark: "))
# query = 'update student set total_mark = %s where roll_no = %s'
# data = (mark,roll,)
# c.execute(query,data)
# con.commit()
# print('Updated')


# delete a record with roll no = roll no entered by user
# roll = int(input("Enter a roll no: "))
# query = 'delete from student where roll_no = %s'
# data = (roll,)
# c.execute(query,data)
# con.commit()
# print('Deleted')

# create new record entered by user
# roll = int(input("Enter a roll no: "))
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# place = input("Enter place: ")
# phn_no = int(input("Enter Phone number:"))
# mark = int(input("Enter mark: "))
# query = 'insert into student values(%s,%s,%s,%s,%s,%s)'
# data = (roll,name,age,place,phn_no,mark,)
# c.execute(query,data)
# con.commit()
# print('Inserted')

Create a database named shop

Create a table `Product` with the following fields:

 `product_id` – Primary Key
 `name`
 `brand`
 `category`
 `price`
 `stock`

Write a menu-driven Python program using MySQL with the following options:

text
1. Insert Product details
2. Read all Product details
3. Search a Product by product_id
4. Update the stock of a Product
5. Delete a Product record
6. Exit

