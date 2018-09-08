import sqlite3

db = sqlite3.connect('../database/exampledb')
cursor = db.cursor()
cursor.execute('''UPDATE todo SET done = ? WHERE activity LIKE ? ''', ('1', 'menulis proposal'))
db.commit()
db.close()

db = sqlite3.connect('../database/exampledb')
cursor = db.cursor()
cursor.execute('''DELETE FROM todo WHERE activity LIKE ? ''', ('cuci kendaraan',))
db.commit()
db.close()

db = sqlite3.connect('../database/exampledb')
cursor = db.cursor()
cursor.execute(''' SELECT id, activity, deadline, done FROM todo ''')
q = cursor.fetchall()
for row in q:
    # row[0] -> first column, row[1] -> second column, etc
    print(row[0], row[1], row[2], row[3])
db.commit()
db.close()