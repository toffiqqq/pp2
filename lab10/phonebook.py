import psycopg2
import csv

# Connect to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        dbname="phonebook", user="postgres", password="32689263", host="localhost"
    )

# Create the table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone_number VARCHAR(15) UNIQUE
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Upload data from a CSV file
def upload_csv_to_phonebook(csv_file):
    conn = connect_db()
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            first_name, last_name, phone_number = row
            cursor.execute(
                "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (first_name, last_name, phone_number)
            )

    conn.commit()
    cursor.close()
    conn.close()

# Insert data via console input
def insert_phonebook_entry():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number)
    )

    conn.commit()
    cursor.close()
    conn.close()

# Update user data (first name or phone number)
def update_phonebook_entry(phone_number):
    new_first_name = input("Enter new first name: ")
    new_phone_number = input("Enter new phone number: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE phonebook
        SET first_name = %s, phone_number = %s
        WHERE phone_number = %s
        """,
        (new_first_name, new_phone_number, phone_number)
    )

    conn.commit()
    cursor.close()
    conn.close()

# Query data from the table (filter by name or phone)
def query_phonebook(filter_type, filter_value):
    conn = connect_db()
    cursor = conn.cursor()

    if filter_type == "name":
        cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == "phone":
        cursor.execute("SELECT * FROM phonebook WHERE phone_number = %s", (filter_value,))

    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")

    cursor.close()
    conn.close()

# Delete user data by name or phone number
def delete_phonebook_entry(delete_type, delete_value):
    conn = connect_db()
    cursor = conn.cursor()

    if delete_type == "name":
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (delete_value,))
    elif delete_type == "phone":
        cursor.execute("DELETE FROM phonebook WHERE phone_number = %s", (delete_value,))

    conn.commit()
    cursor.close()
    conn.close()

# Main menu to interact with the program
def main_menu():
    create_table()  # Ensure the table exists when starting

    while True:
        print("\nPhonebook Menu")
        print("1. Add User")
        print("2. Update User Information")
        print("3. Query User Information")
        print("4. Delete User")
        print("5. Upload Data from CSV")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            insert_phonebook_entry()
        elif choice == "2":
            phone_number = input("Enter the phone number of the user to update: ")
            update_phonebook_entry(phone_number)
        elif choice == "3":
            filter_type = input("Search by name or phone? (name/phone): ")
            filter_value = input("Enter the search value: ")
            query_phonebook(filter_type, filter_value)
        elif choice == "4":
            delete_type = input("Delete by name or phone? (name/phone): ")
            delete_value = input("Enter the value to delete: ")
            delete_phonebook_entry(delete_type, delete_value)
        elif choice == "5":
            csv_file = input("Enter the path to the CSV file: ")
            upload_csv_to_phonebook(csv_file)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()