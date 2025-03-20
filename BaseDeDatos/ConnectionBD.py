import sqlite3 #Importación modulo conexion con SQLite
from sqlite3 import Error #Importación función Error

#Function crear conexión con BD que se pase por param
def create_connection_db(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print('Opened database successfully')
    except Error as err:
        print(f'Error in connection {err.sqlite_errorname}')
        print(f'Error code: {err.sqlite_errorcode}')
    finally:
        connection.close() #Buena práctica cerrar la conexión

#Ejecuto la function
if __name__ == '__main__':
    create_connection_db('little_lemon_COURSERA.db')

#Creación objeto cursor para manipular la BD
connection = sqlite3.connect('little_lemon_COURSERA.db')
cursor = connection.cursor()

#Una vez creado el objeto cursor ejecuto las sentencias SQL desde el metodo execute()

#Creación table Menu
create_menu_table = "CREATE TABLE Menus(MenuID INT,ItemID INT,Cuisine VARCHAR(100),PRIMARY KEY (MenuID,ItemID))"
try:
    cursor.execute(create_menu_table)
    print('Table Menu created successfully')
except Error as er:
    print('Error')
    print(f'Error: {er.sqlite_errorname}')

#Creación table MenuItem
create_menuitem_table = """CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
)"""
try:
    cursor.execute(create_menuitem_table)
    print('Table MenuItem created successfully')
except Error as er:
    print('Error table not created')
    print(f'Error: {er.sqlite_errorname}')

#Creación table Booking
Create_booking_table = """CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
)"""
try:
    cursor.execute(Create_booking_table)
    print('Table Booking created successfully')
except Error as er:
    print(f'Error! {er.sqlite_errorname}')

#Creation table Orders
create_orders_table = """CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""
try:
    cursor.execute(create_orders_table)
    print('Table Orders created successfully')
except Error as er:
    print(f'Error: {er.sqlite_errorname}')
    print(f'Error: {er.sqlite_errorcode}')