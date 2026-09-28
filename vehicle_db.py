import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root", password="123456789", host="localhost", database="shop"
        )
        print(self.con)
        self.cursor = self.con.cursor()
        print("Successfully connected")
    def list(self):
        # Reading all records from tsble
        query = 'select * from vehicles'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")

    def create(self,brand, model, type, price, year):
        query = 'insert into vehicles(brand, model, type, price, year) values(%s,%s,%s,%s,%s);'
        data = (brand, model, type, price, year)
        self.cursor.execute(query, data)
        self.con.commit()
        print("New record inserted successfully")

    def retrieve(self,id):
        # for reading a specific record
        query = 'select * from vehicles where id = %s'
        data = (id,)
        self.cursor.execute(query,data)
        records = self.cursor.fetchone()
        if records:
            print(records)
        else:
            print('No records found')

    def update(self,id,brand, model, type, price, year):
        query = 'update vehicles set brand=%s, model=%s, type=%s, price=%s, year=%s where id = %s'
        data = (brand, model, type, price, year,id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print('Updated')
        else:
            print("No records found")

    def delete(self,id):
        query = 'delete from vehicles where id = %s'
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print('Deleted')
        else:
            print("No records found")
vehicle = VehicleListCreateRetrieveUpdateDelete()
vehicle.list()
vehicle.create('Honda', 'BRV', 'car', 570000, 2014)
vehicle.retrieve(2)
vehicle.update(1,brand='Suzuki',model='Wagnor',type='car',price=350000,year=2011)
vehicle.delete(id=2)