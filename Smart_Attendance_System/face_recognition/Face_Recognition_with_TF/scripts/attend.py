import sqlite3
from datetime import datetime


def attendance(roll_no, name, mark):
    roll_no = str(roll_no)
    # connecting to the database
    connection = sqlite3.connect("Attendance2.db")

    # cursor
    crsr = connection.cursor()

    # Create Table if not exist
    sql_command = """CREATE TABLE IF NOT EXISTS attend (id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no VARCHAR(20),
    name VARCHAR(20), unique(roll_no));"""


    crsr.execute(sql_command)

    # Get Column names
    crsr = connection.execute("Select * from attend")
    names = list(map(lambda x: x[0], crsr.description))
    a = names[-1]

    date = str(datetime.date(datetime.now()))

    # if current date is not present then add current date in Table
    if a != date:
        crsr.execute("ALTER TABLE Attend ADD COLUMN '{cn}' DATE".format(cn=date))

    try:
        sql = """INSERT INTO attend (roll_no, name) Values(?, ?)"""
        val = (roll_no, name)
        crsr.execute(sql, val)
    except:
        pass

    crsr.execute("UPDATE Attend set ('{}')=('{}')  WHERE roll_no=('{}') ".format(date, mark, roll_no))

    connection.commit()

    # close the connection
    connection.close()

    print("Done DB Attendance")
