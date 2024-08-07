# WareHouse

This code manages a warehouse using a PostgreSQL database. Here’s what each file does:

database.py:

create_connection(): Connects to the PostgreSQL database.
initialize_db(conn): Creates a table to store information about items, including name, quantity, price, employee name, client name, purchase date, date added, and city.
add_item(conn, name, quantity, price, employee_name, city): Adds a new item to the database.
get_items(conn): Retrieves all items from the database.
update_item_quantity(conn, item_id, quantity): Updates the quantity of an item by its ID.
get_item_by_id(conn, item_id): Gets an item by its ID.
buy_item(conn, item_id, quantity, client_name): Processes a purchase of an item, updating its quantity and recording client information and purchase date.
main.py:

main_menu(conn): Displays the main menu for managing the warehouse, where you can view items, add new ones, update quantities, and make purchases.
main(): Runs the application by creating a database connection and displaying the main menu.
![f](https://github.com/BlackWaterPark0011010111/WareHouse/blob/master/WareHouse/426.png)
![s](https://github.com/BlackWaterPark0011010111/WareHouse/blob/master/WareHouse/15.png)
