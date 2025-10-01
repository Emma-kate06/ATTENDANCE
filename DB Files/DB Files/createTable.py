import sqlite3

def create_new_table(db_name="dragon.db"):
    """
    Connects to the specified SQLite database (dragon.db) and creates 
    a new table with a user-specified name and basic columns.
    """
    # 1. Get the desired table name from the user
    table_name = input("Enter the desired name for your new table: ")

    # Basic validation
    if not table_name.strip():
        print("Table name cannot be empty. Aborting.")
        return

    # 2. Define the columns for the table
    # We use an f-string to safely insert the user-provided table name.
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        element TEXT,
        power INTEGER
    );
    """

    # 3. Connect to the database file
    conn = None
    try:
        # Connects to 'dragon.db'. If it exists, it opens it; if not, it creates it.
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # 4. Execute the SQL command
        cursor.execute(create_table_sql)

        # 5. Commit the changes and close the connection
        conn.commit()
        print(f"\nSuccess! Table '{table_name}' created in '{db_name}'.")

    except sqlite3.Error as e:
        print(f"\nAn error occurred: {e}")

    finally:
        if conn:
            conn.close()
            
# --- Run the function ---
if __name__ == "__main__":
    # Pass 'dragon.db' to the function
    create_new_table(db_name="dragon.db")