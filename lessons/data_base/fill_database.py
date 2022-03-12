import sqlite3

conn = sqlite3.connect("office.db")
cursor = conn.cursor()

# Table Position
cursor.execute("drop table if exists position")

cursor.execute("""create table if not exists position(
               id integer primary key autoincrement not null,
               position text not null,
               salary integer not null);
               """)

data = [
    ('Директор', 200000), ('Бухгалтер', 100000), ('Менеджер', 50000),
    ('IT-инженер', 300000), ('Водитель', 80000), ('Офис-менеджер', 45000)
]
cursor.executemany("""insert into position(position, salary) values(?, ?);""", data)
cursor.execute("select * from position")
res = cursor.fetchall()
print(res)

conn.close()
