import sqlite3
#
# # Connect and create database
# conn = sqlite3.connect("11_DB_SQLite/app.db")
#
# cursor = conn.cursor()  # Consult
# cursor.execute(
#     """
#     CREATE TABLE if not exists users
#     (id INTEGER primary key, name VARCHAR(50));
#     """
# )
# conn.commit()  # Changes applied
# conn.close()  # Important


# `with` saves 2 lines to run
with sqlite3.connect("11_DB_SQLite/app.db") as conn:
    cursor = conn.cursor()
    # Insert multiple
    # users = [
    #    (6, "Main Method 106"),
    #    (7, "Main Method 107"),
    #    (8, "Main Method 108"),
    # ]

    cursor.execute(
        # cursor.executemany(  # Insert multiple data

        # CONSULT | First argument
        # VALUES | Second argument in tuples
        # AVOID SQL INJECTION

        # (5, "Main Method 007"),

        # "INSERT INTO users VALUES(?,?)",
        # users,
        "SELECT * FROM users"  # SELECT ONE
    )

    print(cursor.fetchone())  # SELECT ONE
    print(cursor.fetchall())  # SELECT ALL
