import sqlite3

def create_connection(db_file):
  
    conn = sqlite3.connect(db_file)
    return conn

def initialize_db(conn):
    """tables in the database."""
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')

def add_item(conn, name, quantity, price):
    """Add a new item """
    with conn:
        conn.execute('''
            INSERT INTO items (name, quantity, price)
            VALUES (?, ?, ?)
        ''', (name, quantity, price))

def get_items(conn):
    """Retrieve all items"""
    with conn:
        cursor = conn.execute('SELECT * FROM items')
        return cursor.fetchall()

def update_item_quantity(conn, item_id, quantity):
    """Update the quantity"""
    with conn:
        conn.execute('''
            UPDATE items
            SET quantity = quantity - ?
            WHERE id = ?
        ''', (quantity, item_id))

def get_item_by_id(conn, item_id):
    """Retrieve an item by its ID."""
    with conn:
        cursor = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,))
        return cursor.fetchone()
