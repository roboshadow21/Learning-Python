import sqlite3


conn = sqlite3.connect('office.db')
cursor = conn.cursor()

# Table Position
cursor.execute("drop table if exists position")

cursor.execute("""create table if not exists position(
               id integer primary key autoincrement not null,
               position text not null,
               salary integer not null);
               """)
cursor.execute("""insert into position(position, salary) values('Директор', '10000');""")
conn.commit()

# Table status

cursor.execute("drop table if exists status")

cursor.execute("""create table if not exists status(
id integer primary key autoincrement not null,
description text);
""")

cursor.execute("""insert into status(description) values('работает');""")

# Table Stuff
# Add field birthday_at!

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

cursor.execute(
    """insert into stuff(name, surname, sex, birthday_at, marital_status, position_id, status_id) values(
    'Alex', 'Doe', 'm','1969-09-29', 'married', 1, 1);
    """)

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

cursor.execute("""insert into contacts(stuff_id, phone, description_phone, email, description_email) values(
              1, '12-345', 'личный', 'alex@mail.ru', 'служебная');
              """)

# Table addresses

cursor.execute("drop table if exists addresses")
cursor.execute("""create table if not exists addresses(
               id integer primary key autoincrement not null,
               stuff_id integer not null,
               address text,
               description text,
               foreign key (stuff_id) references stuff(id));
               """)
cursor.execute("""insert into addresses(stuff_id, address, description) values(
              1, 'Москва', 'по прописке');
              """)
conn.commit()

# Show age
cursor.execute("""select datetime() - birthday_at from stuff;""")
x = cursor.fetchone()
print(x)

# User input

# while True:
#     data = input('Enter name, surname, position_id: ').split()
#     if data == ['q']:
#         break
#     else:
#         cursor.execute("""insert into stuff(name, surname, position_id) values(?, ?, ?);""", data)
#         conn.commit()

# Change the value in the table

# cursor.execute("""update stuff set name='Bob' where name='Alex';""")
# conn.commit()

cursor.execute("select * from position;")
result = cursor.fetchone()
print(result)

cursor.execute("select * from stuff;")
res = cursor.fetchall()
print(res)

cursor.execute("select * from status;")
res = cursor.fetchall()
print(res)

cursor.execute("select * from contacts")
res = cursor.fetchall()
print(res)

cursor.execute("select * from addresses")
res = cursor.fetchall()
print(res)

# Insert variable into query

# mode = 'Alex'
# cursor.execute("""select surname from stuff where name=?;""", (mode,))
# res = cursor.fetchall()
# print(res)

# Join tables

cursor.execute("select stuff.name, stuff.surname, position.salary "
               "from stuff left join position on stuff.position_id=position.id;")

res = cursor.fetchall()
print(res)

conn.close()

