import psycopg2
import csv

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="050307",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1 design table
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(50) NOT NULL
    )
    """)
    conn.commit()

# 2 upload data from csv file
def insert_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("Data inserted from CSV successfully.")

# 2 console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Data inserted from console successfully.")

# 3 updating
def update_data(user_id, new_name=None, new_phone=None):
    if new_name:
        cur.execute(
            "UPDATE PhoneBook SET name = %s WHERE id = %s",
            (new_name, user_id)
        )
    if new_phone:
        cur.execute(
            "UPDATE PhoneBook SET phone = %s WHERE id = %s",
            (new_phone, user_id)
        )
    conn.commit()
    print("Data updated successfully.")

# 4 querying
def query_data(name_filter=None, phone_filter=None):
    query = "SELECT * FROM PhoneBook WHERE TRUE"
    params = []
    if name_filter:
        query += " AND name ILIKE %s"
        params.append(f"%{name_filter}%")
    if phone_filter:
        query += " AND phone ILIKE %s"
        params.append(f"%{phone_filter}%")
    cur.execute(query, params)
    results = cur.fetchall()
    for row in results:
        print(row)

# 5 deleting
def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted successfully.")

if __name__ == "__main__":
    create_table()

    cur.close()
    conn.close()
