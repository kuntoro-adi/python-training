from pony.orm import *
from datetime import datetime
from uuid import uuid1

db = Database()
set_sql_debug(True)

# Now bind to the database

db.bind(provider='postgres', user='postgres', password='postgres123', host='localhost', port=5432, database='money')

class Cashlog(db.Entity):
    id = PrimaryKey(str, max_len=36)
    amount = Required(int)
    description = Optional(str)
    date = Required(datetime)

# Now generate the table(s)

db.generate_mapping(create_tables=True)

@db_session
def outflow():
    q = select(c for c in Cashlog if c.amount < 0)
    for e in q:
        print(e.id, e.description, e.amount)

@db_session
def inflow():
    q = select(c for c in Cashlog if c.amount > 0)
    for e in q:
        print(e.id, e.description, e.amount)