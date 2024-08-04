from database import create_connection, initialize_db
from ui import main_menu

def main():
    database = "inventory.db"
    conn = create_connection(database)
    
    initialize_db(conn)
    main_menu(conn)
    
    conn.close()

if __name__ == "__main__":
    main()
