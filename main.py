import sqlite3
import file


# Yet to complete work on update function

# Start of Program Function
def start():
    while True:
        print("\nWelcome to ENGATA COLLEGE")
        prompt = input("DO YOU WISH TO CONTINUE TO MENU [y/n] => ").lower()
        quit(0) if prompt == 'n' else ''
        if prompt == 'y':
            options()
        else:
            break



# Options Function
def options():
    print("\n OPTIONS: \n"
          "1) DISPLAY USERS\n"
          "2) INSERT USER\n"
          "3) UPDATE USER\n"
          "4) DELETE USER\n"
          "5) EXIT\n")
    option = int(input("SELECT =>[1/2/3/4/5]<= "))
    if option == 1:
        display()
    elif option == 2:
        insert()
    elif option == 3:
        update()
    elif option == 4:
        delete()
    elif option == 5:
        quit(0)
    else:
        print("INVAlID")


# Connect to Database
conn = sqlite3.connect('admin.sqlite3')
# Connect Cursor
cur = conn.cursor()
# Create Table
cur.execute(file.CREATE_TABLE)
# Commit to Database
conn.commit()


# Display Users Function
def display():
    cur.execute("SELECT * FROM details")
    items = cur.fetchall()
    for item in items:
        print(item)

    conn.commit()
    return


# Insert Function
def insert():
    id = None
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email: ").lower()
    age = int(input("Age: "))
    gender = input("Gender: ").upper()

    cur.execute("INSERT INTO details(id, firstName, lastName, email, age, gender) VALUES(?, ?, ?, ?, ?, ?)",
                (id, firstName, lastName, email, age, gender))
    conn.commit()
    print("\nINSERTED SUCCESSFULLY...")
    return

# Update Function
def update():
    di = int(input("ID: "))
    firstName = input("Update First Name: ")
    lastName = input("Update Last Name: ")
    email = input("Update Email: ")
    age = int(input("Update Age: "))
    gender = input("Update Gender: ")

    new = "UPDATE details SET (firstName, lastName, email, age, gender) = (?, ?, ?, ?, ?) WHERE rowid = (?)"
    cur.execute(new, (firstName, lastName, email, age, gender, di))
    conn.commit()
    print("UPDATED SUCCESSFULLY...")
    return


# Delete Function
def delete():
    di = input("ID: ")
    cur.execute("DELETE FROM details WHERE rowid = (?)", di)
    print("DELETED SUCCESSFULLY...")
    return


# dis checks only d update
# Remove d update function bellow to get ful experience of my code.{smile} leave d """start()"""
start()

# Close Database
conn.close()