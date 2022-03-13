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
# cursor.execute("select * from position")
# res = cursor.fetchall()
# print(res)

# Table status

cursor.execute("drop table if exists status")

cursor.execute("""create table if not exists status(
id integer primary key autoincrement not null,
description text);
""")

status = [
    ('работает',), ('уволен',), ('отпуск',), ('командировка',), ('декрет',)
]
cursor.executemany("""insert into status(description) values(?);""", status)
# cursor.execute("select * from status")
# res = cursor.fetchall()
# print(res)

# Table Stuff

cursor.execute("drop table if exists stuff")

cursor.execute("""create table if not exists stuff(
              id integer primary key autoincrement not null,
              name text,
              surname text,
              sex text,
              birthday_at text,
              marital_status text,
              position_id integer not null,
              status_id integer not null,
              foreign key (position_id) references position(id),
              foreign key (status_id) references status(id));
              """)

persons = [
    ('Петр', 'Иванов', 'м', '1982-03-21', 'женат', 1, 1),
    ('Анна', 'Сергеева', 'ж', '1976-07-06', 'замужем', 2, 1),
    ('Федор', 'Федоров', 'м', '1992-05-15', 'холост', 3, 1),
    ('Иван', 'Игнатьев', 'м', '1998-07-24', 'женат', 3, 3),
    ('Сергей', 'Иванов', 'м', '1987-09-12', 'холост', 3, 4),
    ('Николай', 'Петров', 'м', '1989-02-27', 'женат', 4, 1),
    ('Никита', 'Федоров', 'м', '1999-11-14', 'холост', 4, 1),
    ('Юлия', 'Дулова', 'ж', '1991-03-18', 'замужем', 4, 1),
    ('Игорь', 'Петров', 'м', '1977-06-07', 'разведен', 5, 1),
    ('Ольга', 'Симонова', 'ж', '1996-10-08', 'замужем', 6, 1)
]

cursor.executemany(
    """insert into stuff(name, surname, sex, birthday_at, marital_status, position_id, status_id) values(
    ?, ?, ?, ?, ?, ?, ?);
    """, persons)

# cursor.execute("select * from stuff")
# res = cursor.fetchall()
# print(res)

# Table contacts
cursor.execute("drop table if exists contacts")
cursor.execute("""create table if not exists contacts(
               id integer primary key autoincrement not null,
               stuff_id integer not null,
               phone text,
               description_phone text,
               email text,
               description_email text,
               foreign key (stuff_id) references stuff(id));
               """)
contacts = [
    (1, '111', 'служебный', 'ivanov@org.com', 'служебная'),
    (1, '222', 'личный', 'van@net.com', 'личная'),
    (2, '333', 'служебный', 'anna@dot.com', 'служебная'),
    (3, '444', 'служебный', 'fedor@org.com', 'служебная'),
    (3, '555', 'личный', 'fedya@org.com', 'личная'),
    (4, '666', 'личный', 'iv@org.com', 'личная'),
    (5, '777', 'служебный', 'serg@dot.com', 'служебная')
]

cursor.executemany("""insert into contacts(stuff_id, phone, description_phone, email, description_email) values(
              ?, ?, ?, ?, ?);
              """, contacts)
# cursor.execute("select * from contacts")
# res = cursor.fetchall()
# print(res)

# Table addresses

cursor.execute("drop table if exists addresses")
cursor.execute("""create table if not exists addresses(
               id integer primary key autoincrement not null,
               stuff_id integer not null,
               address text,
               description text,
               foreign key (stuff_id) references stuff(id));
               """)
address = [
    (1, 'Москва', 'прописка'), (2, 'Питер', 'прописка'), (2, 'Москва', 'факт'),
    (3, 'Томск', 'прописка'), (3, 'Москва', 'факт')
]
cursor.executemany("""insert into addresses(stuff_id, address, description) values(
              ?, ?, ?);
              """, address)

# cursor.execute("select * from addresses")
# res = cursor.fetchall()
# print(res)

conn.commit()
conn.close()
