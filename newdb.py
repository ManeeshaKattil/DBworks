# Create a database named shop
#
# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit
import mysql.connector
# con = mysql.connector.connect(user="root", password="123456789", host="localhost")
# c = con.cursor()
# c.execute('create database shop')
# print("Database created successfully")

con = mysql.connector.connect(user="root", password="123456789", host="localhost", database="shop")
c = con.cursor()
# query = 'create table Product(product_id int not null primary key, name varchar(30), brand varchar(30), category varchar(30), price int, stock int)'
# c.execute(query)
# print("Table created successfully")

def insert_details():
    id = int(input("Enter product id: "))
    name = input("Enter product name: ")
    brand = input("Enter brand: ")
    category = input("Enter category: ")
    price = int(input("Enter price: "))
    stock = int(input("Enter stock: "))

    query = 'insert into Product values(%s,%s,%s,%s,%s,%s);'
    data = (id,name,brand,category,price,stock,)
    c.execute(query,data)
    con.commit()
    print("New record inserted successfully")

def read():
    query = 'select * from Product'
    c.execute(query)
    records = c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print('No records found')

def search():
    p_id = int(input("Enter product id: "))
    query = 'select * from Product where product_id = %s'
    data = (p_id,)
    c.execute(query,data)
    records = c.fetchone()
    if records:
        print(records)
    else:
        print('No records found')

def update():
    p_id = int(input("Enter a product id: "))
    stock = int(input("Enter new stock: "))
    query = 'update Product set stock = %s where product_id = %s'
    data = (stock,p_id,)
    c.execute(query,data)
    con.commit()
    print('Updated')

def delete():
    p_id = int(input("Enter product id: "))
    query = 'delete from Product where product_id = %s'
    data = (p_id,)
    c.execute(query,data)
    con.commit()
    print('Deleted')


while(1):
    ch = int(input("Enter your choice\n1. Insert Product details\n2. Read all Product details\n3. Search a Product by product_id\n4. Update the stock of a Product\n5. Delete a Product record\n6. Exit: "))
    if ch == 1:
        insert_details()
    elif ch == 2:
        read()
    elif ch == 3:
        search()
    elif ch == 4:
        update()
    elif ch == 5:
        delete()
    elif ch == 6:
        exit()
    else:
        print("Invalid choice!")  


