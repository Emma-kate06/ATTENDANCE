import sqlite3

# --- Configuration ---
DATABASE_FILE = "dragon.db"
TABLE_NAME = "CUSTOMER"  # !!! IMPORTANT: Replace with your actual table name !!!

# ----------------------------------------------------------------------
# 1. Function to Get Field (Column) Names
# ----------------------------------------------------------------------
def get_field_names():
    """Reads and returns a list of all column names for the specified table."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # PRAGMA table_info is the standard way to get schema information
        cursor.execute(f"PRAGMA table_info({TABLE_NAME});")
        
        # The column names are the second element (index 1) in the returned tuples
        column_names = [info[1] for info in cursor.fetchall()]
        return column_names

    except sqlite3.Error as e:
        print(f"An error occurred while getting field names: {e}")
        return []
    finally:
        if conn:
            conn.close()

# ----------------------------------------------------------------------
# 2. Function to Read Data (View All Records)
# ----------------------------------------------------------------------
def read_data():
    """Connects to the database and prints all records from the table."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Select all columns (*) and all rows
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        
        # Get column names using cursor.description for cleaner output
        column_names = [description[0] for description in cursor.description]
        
        print("\n--- Current Data in Table: " + TABLE_NAME + " ---")
        print(f"Fields: {column_names}")
        
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred while reading data: {e}")
    finally:
        if conn:
            conn.close()

# ----------------------------------------------------------------------
# 3. Function to Edit/Update Data in a Field
# ----------------------------------------------------------------------
def edit_field(field_to_update, new_value, unique_id_field, unique_id_value):
    """
    Updates a specific field's value for a record identified by a unique ID.
    
    :param field_to_update: The column name to change (e.g., 'color').
    :param new_value: The new data to put into the field (e.g., 'Red-Gold').
    :param unique_id_field: The column name used for identification (e.g., 'id').
    :param unique_id_value: The value of the identifying field (e.g., 1).
    """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Parameterized query to safely update data.
        sql_update_query = f"""
            UPDATE {TABLE_NAME}
            SET {field_to_update} = ?
            WHERE {unique_id_field} = ?;
        """
        
        # Execute the update with the values tuple
        cursor.execute(sql_update_query, (new_value, unique_id_value))
        
        # Commit the changes to save them permanently to the database file
        conn.commit()
        
        print(f"\nSuccessfully updated '{field_to_update}' to '{new_value}' for record where {unique_id_field} = {unique_id_value}. ({cursor.rowcount} row(s) affected)")

    except sqlite3.Error as e:
        print(f"An error occurred while editing: {e}")
    finally:
        if conn:
            conn.close()

# ----------------------------------------------------------------------
# --- Execution Demonstration ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    # 1. Display Field Names
    fields = get_field_names()
    print("Fields in the table:", fields)

    # 2. Read Initial Data
    print("\n--- 1. Initial Data Read ---")
    read_data()
    
    # --- Example Editing Operation ---
    # NOTE: You must know the name of a unique column (like 'id') and another column 
    # to update (like 'color'). Adjust these parameters to match your table schema.
    
    # Example: Change the 'color' field to 'Red-Gold' for the dragon with 'id' = 1.
    if 'id' in fields and 'color' in fields:
        edit_field(
            field_to_update="color", 
            new_value="Red-Gold", 
            unique_id_field="id", 
            unique_id_value=1
        )
    else:
        print("\nSkipping edit demonstration because required columns ('id' and 'color') were not found in the table schema.")

    # 3. Read Data After Edit to Verify
    print("\n--- 2. Data Read After Edit ---")
    read_data()