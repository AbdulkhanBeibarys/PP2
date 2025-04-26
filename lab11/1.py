import psycopg2
import csv
import re

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="050307"
)

cur = conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Phonebook(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()

def insert_or_update_user(name, phone):
    cur.execute("SELECT * FROM Phonebook WHERE first_name = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE Phonebook SET phone = %s WHERE first_name = %s", (phone, name))
        print(f"Phone updated for {name}.")
    else:
        cur.execute("INSERT INTO Phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        print(f"New user {name} added.")
    conn.commit()

def insert_csv(filename):
    people = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["first_name"]
            phone = row["phone"]
            if not re.match(r"^\+?\d{10,15}$", phone):
                people.append((name, phone))
            else:
                cur.execute("INSERT INTO Phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    if people:
        print("Invalid phones:")
        for entry in people:
            print(entry)

def find_by_pattern(pattern):
    cur.execute("SELECT * FROM Phonebook WHERE first_name LIKE %s OR phone LIKE %s", ('%' + pattern + '%', '%' + pattern + '%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM Phonebook WHERE first_name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM Phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("User deleted successfully.")


create_table()
# insert_or_update_user("Samal", "87005556677")
insert_csv("contacts.csv")
# find_by_pattern("Samal")
#delete_user(name="Samal")

cur.close()
conn.close()
