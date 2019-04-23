import sqlite3


def fetching(roll):
    connection = sqlite3.connect("Attendance2.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM attend WHERE roll_no=('{}') ".format(roll))
    rows = crsr.fetchall()
    for row in rows:
        print("enrollment number =", row[1])
        enrollment_no = row[1]
        print("Name=", row[2])
        name = row[2]
        count = 0
        s = 0
        for i in row:
            count = count+1
            if(i=='p'):
                s = s+1
        p = (s/(count-3))*100
        print("Total Number of Days", (count-3))
        total_days = count-3
        print("Number of days Present", s)
        total_present_days = s
        print("Percentage=", p)
        precentage = p

        return enrollment_no, name, total_days, total_present_days, precentage


    connection.commit()
    connection.close()


