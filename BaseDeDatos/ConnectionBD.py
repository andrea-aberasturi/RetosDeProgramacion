import sqlite3

try:
    connection = sqlite3.connect('little_lemon_COURSERA.db')
    print('Opened database successfully')
except:
    print(f'Error in connection')


# create_menu_table = "CREATE TABLE Menus(MenuID INT,ItemID INT,Cuisine VARCHAR(100),PRIMARY KEY (MenuID,ItemID))"

# try:
#     connection.execute(create_menu_table)
#     print('Table created successfully')
# except:
#     print('Error')

# create_menuitem_table = """CREATE TABLE MenuItems (
# ItemID INT AUTO_INCREMENT,
# Name VARCHAR(200),
# Type VARCHAR(100),
# Price INT,
# PRIMARY KEY (ItemID)
# );"""
# try:
#     connection.execute(create_menuitem_table)
#     print('Table created successfully')
# except:
#     print('Error table not created')

# Create_booking_table = """CREATE TABLE Bookings (
# BookingID INT AUTO_INCREMENT,
# TableNo INT,
# GuestFirstName VARCHAR(100) NOT NULL,
# GuestLastName VARCHAR(100) NOT NULL,
# BookingSlot TIME NOT NULL,
# EmployeeID INT,
# PRIMARY KEY (BookingID)
# );"""
# try:
#     connection.execute(Create_booking_table)
#     print('Table created successfully')
# except:
#     print('Error!')
