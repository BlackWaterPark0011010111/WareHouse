# WareHouse


![frst](https://github.com/BlackWaterPark0011010111/WareHouse/blob/main/426.png)


![scnd](https://github.com/BlackWaterPark0011010111/WareHouse/blob/main/15.png)


## Warehouse Management System
This project manages a warehouse using a PostgreSQL database. The system allows adding new items, updating the quantity of existing items, processing purchases, and displaying a list of all items in the warehouse, with detailed information including the time added and employee names.

## Table of Contents
#### Installation and Setup
#### Usage
#### Functionality
#### Additional Information


## Installation and Setup
Requirements:
Python 3.x
PostgreSQL

## Installation Steps
Clone the repository:

bash: git clone https://github.com/yourusername/warehouse.git
cd warehouse
Create and activate a virtual environment:


Set up PostgreSQL:

Launch the PostgreSQL command line (psql):
psql -U postgres
Create a database and user:
sql
Копировать код
CREATE DATABASE warehouse_db;
CREATE USER .... WITH ENCRYPTED PASSWORD '...';
GRANT ALL PRIVILEGES ON DATABASE warehouse_db TO your_user;
Configure the database connection parameters in database.py in the function:


def create_connection():
    conn = psycopg2.connect(
        dbname='warehouse_db',
        user='....',
        password='....',
        host='localhost'
    )
    return conn

Run the project:

## main.py
Follow the instructions in the menu to manage the warehouse:

1. View Items: Display all items in the warehouse.
2. Add Item: Add a new item.
3. Update Item Quantity: Update the quantity of an existing item.
4. Buy Item: Purchase an item and update its quantity.
5. Exit: Exit the application.
### Functionality
View Items: Displays all items in the database.
Add Item: Adds a new item to the database.
Update Item Quantity: Updates the quantity of an existing item by its ID.
Buy Item: Processes the purchase of an item, updates its quantity, and records client information and purchase date.
Exit: Exits the application.
Additional Information
### File Structure
database.py: Contains functions for working with the database.

create_connection(): Connects to the PostgreSQL database.
initialize_db(conn): Creates a table to store information about items.
add_item(conn, name, quantity, price, employee_name, city): Adds a new item to the database.
get_items(conn): Retrieves all items from the database.
update_item_quantity(conn, item_id, quantity): Updates the quantity of an item by its ID.
get_item_by_id(conn, item_id): Retrieves an item by its ID.
buy_item(conn, item_id, quantity, client_name): Processes a purchase of an item.
main.py: Contains the main interface for user interaction.

main_menu(conn): Displays the main menu for managing the warehouse.
main(): Runs the application, creating a database connection and displaying the main menu.
This README file provides users with all the necessary steps to install, set up, and use your warehouse management project.