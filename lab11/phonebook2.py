import psycopg2
import csv

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname="phonebook", user="postgres", password="32689263", host="localhost"
    )

# Create the phonebook table
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

# Create required functions and procedures in PostgreSQL
def setup_db_extensions():
    conn = connect_db()
    cursor = conn.cursor()

    # Pattern search function
    cursor.execute("""
    CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
    RETURNS TABLE(id INT, first_name TEXT, last_name TEXT, phone_number TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook
        WHERE first_name ILIKE '%' || pattern || '%'
           OR last_name ILIKE '%' || pattern || '%'
           OR phone_number ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Insert or update user procedure
    cursor.execute("""
    CREATE OR REPLACE PROCEDURE insert_or_update_user(
        in_first_name TEXT,
        in_last_name TEXT,
        in_phone_number TEXT
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = in_first_name AND last_name = in_last_name) THEN
            UPDATE phonebook
            SET phone_number = in_phone_number
            WHERE first_name = in_first_name AND last_name = in_last_name;
        ELSE
            INSERT INTO phonebook(first_name, last_name, phone_number)
            VALUES (in_first_name, in_last_name, in_phone_number);
        END IF;
    END;
    $$;
    """)

    # Insert many users with phone validation
    cursor.execute("""
    CREATE OR REPLACE PROCEDURE insert_many_users(
        users TEXT[][],
        OUT invalid_users TEXT[]
    )
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT := 1;
        name TEXT;
        surname TEXT;
        phone TEXT;
        invalid_list TEXT[] := '{}';
    BEGIN
        WHILE i <= array_length(users, 1) LOOP
            name := users[i][1];
            surname := users[i][2];
            phone := users[i][3];

            IF phone ~ '^\\+\\d{7,15}$' THEN
                BEGIN
                    INSERT INTO phonebook (first_name, last_name, phone_number)
                    VALUES (name, surname, phone);
                EXCEPTION
                    WHEN unique_violation THEN
                        RAISE NOTICE 'Phone % already exists, skipping.', phone;
                END;
            ELSE
                invalid_list := array_append(invalid_list, name || ' ' || surname || ': ' || phone);
            END IF;
            i := i + 1;
        END LOOP;
        invalid_users := invalid_list;
    END;
    $$;
    """)

    # Pagination function
    cursor.execute("""
    CREATE OR REPLACE FUNCTION get_users_by_page(limit_num INT, offset_num INT)
    RETURNS TABLE(id INT, first_name TEXT, last_name TEXT, phone_number TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook
        ORDER BY id
        LIMIT limit_num OFFSET offset_num;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Delete user by name or phone
    cursor.execute("""
    CREATE OR REPLACE PROCEDURE delete_user(
        delete_value TEXT,
        delete_type TEXT
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF delete_type = 'name' THEN
            DELETE FROM phonebook WHERE first_name = delete_value;
        ELSIF delete_type = 'phone' THEN
            DELETE FROM phonebook WHERE phone_number = delete_value;
        ELSE
            RAISE EXCEPTION 'Unknown delete type. Use "name" or "phone".';
        END IF;
    END;
    $$;
    """)

    conn.commit()
    cursor.close()
    conn.close()

# Upload from CSV file
def upload_csv_to_phonebook(csv_file):
    conn = connect_db()
    cursor = conn.cursor()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            first_name, last_name, phone_number = row
            try:
                cursor.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (first_name, last_name, phone_number)
                )
            except psycopg2.IntegrityError:
                conn.rollback()
                print(f"Error: phone number {phone_number} already exists.")
    conn.commit()
    cursor.close()
    conn.close()

# Insert single user manually
def insert_phonebook_entry():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Query by name or phone
def query_phonebook(filter_type, filter_value):
    conn = connect_db()
    cursor = conn.cursor()
    if filter_type == "name":
        cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == "phone":
        cursor.execute("SELECT * FROM phonebook WHERE phone_number = %s", (filter_value,))
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]} {row[2]} - {row[3]}")
    cursor.close()
    conn.close()

# Pattern search
def pattern_search():
    pattern = input("Enter part of a name or phone number: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} {row[2]} - {row[3]}")
    cursor.close()
    conn.close()

# Insert or update using stored procedure
def insert_or_update_user():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone number: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CALL insert_or_update_user(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cursor.close()
    conn.close()

# Insert multiple users
def insert_many_users():
    users = []
    n = int(input("How many users do you want to add? "))
    for _ in range(n):
        first = input("First name: ")
        last = input("Last name: ")
        phone = input("Phone number (+123456789): ")
        users.append([first, last, phone])

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CALL insert_many_users(%s, %s)", (users, None))
    conn.commit()
    print("Users added (check PostgreSQL NOTICE for errors).")
    cursor.close()
    conn.close()

# Pagination
def get_users_by_page():
    limit = int(input("Number of records per page: "))
    offset = int(input("Offset: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM get_users_by_page(%s, %s)", (limit, offset))
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} {row[2]} - {row[3]}")
    cursor.close()
    conn.close()

# Delete user by procedure
def delete_user_proc():
    value = input("Enter name or phone: ")
    delete_type = input("Type (name/phone): ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CALL delete_user(%s, %s)", (value, delete_type))
    conn.commit()
    print("User deleted successfully.")
    cursor.close()
    conn.close()

# Main menu
def main_menu():
    create_table()
    setup_db_extensions()

    while True:
        print("\nPhonebook Menu")
        print("1. Add user manually")
        print("2. Insert or update user (procedure)")
        print("3. Search by name or phone")
        print("4. Delete user (procedure)")
        print("5. Upload from CSV")
        print("6. Search by pattern")
        print("7. Insert multiple users (procedure)")
        print("8. Paginated user listing")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            insert_phonebook_entry()
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            filter_type = input("Search by 'name' or 'phone': ")
            filter_value = input("Enter search value: ")
            query_phonebook(filter_type, filter_value)
        elif choice == "4":
            delete_user_proc()
        elif choice == "5":
            csv_file = input("Enter path to CSV file: ")
            upload_csv_to_phonebook(csv_file)
        elif choice == "6":
            pattern_search()
        elif choice == "7":
            insert_many_users()
        elif choice == "8":
            get_users_by_page()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()