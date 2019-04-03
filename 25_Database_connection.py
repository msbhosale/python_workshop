import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "python"
)

my_cursor = my_db.cursor()

# To Fetch all records

# my_cursor.execute("SELECT * FROM student")

# result = my_cursor.fetchall()

# print(result)

# for record in result:
#     print(type(record))
#     print(record)

# For INSERT record

# query = "INSERT INTO student VALUES (%s,%s,%s)"
# values = (105,"Komal","Madam")

# my_cursor.execute(query,values)

# my_db.commit()

# For UPDATE

# query = "UPDATE student SET last_name=%s WHERE roll_number=%s"
# values = ("Sukhi",105)

# my_cursor.execute(query,values)

# my_db.commit()