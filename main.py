import sqlite3

# Create a connection to the database
conn = sqlite3.connect("registration.db")
cursor = conn.cursor()

# Create operation
def create_record(name, email, dob):
    try:
        cursor.execute("INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (?, ?, ?)",
                       (name, email, dob))
        conn.commit()
        print("Record created successfully!")
    except Exception as e:
        print("Error creating record:", e)

# Read operation
def get_record(record_id):
    try:
        cursor.execute("SELECT * FROM Registration WHERE ID = ?", (record_id,))
        record = cursor.fetchone()
        if record:
            print("ID:", record[0])
            print("Name:", record[1])
            print("Email:", record[2])
            print("Date of Birth:", record[3])
        else:
            print("Record not found.")
    except Exception as e:
        print("Error retrieving record:", e)

# Update operation
def update_record(record_id, name, email, dob):
    try:
        cursor.execute("UPDATE Registration SET Name = ?, Email = ?, DateOfBirth = ? WHERE ID = ?",
                       (name, email, dob, record_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Record updated successfully!")
        else:
            print("Record not found.")
    except Exception as e:
        print("Error updating record:", e)

# Delete operation
def delete_record(record_id):
    try:
        cursor.execute("DELETE FROM Registration WHERE ID = ?", (record_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Record deleted successfully!")
        else:
            print("Record not found.")
    except Exception as e:
        print("Error deleting record:", e)

# Close the database connection
conn.close()
