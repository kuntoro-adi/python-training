from pony.orm import *
from datetime import datetime
from uuid import uuid1

db = Database()

# Now bind to the database

db.bind(provider='postgres', user='postgres', password='postgres123', host='localhost', port=5432, database='socmed')

# Table definitions: create or bind the following tables

class User(db.Entity):
    email = PrimaryKey(str, max_len=320)
    name = Required(str)
    user_posts = Set('Post')
    
class Post(db.Entity):
    id = PrimaryKey(str, max_len=36)
    text = Optional(str)
    post_date = Required(datetime)
    author = Required(User)

# Now generate the table(s)

db.generate_mapping(create_tables=True)

@db_session
def save_user(p_email, p_name):
    u = User.get(email=p_email)
    if u == None:
        User(email=p_email, name=p_name)
        commit()
    else:
        u.set(name=p_name)
        commit()

@db_session
def save_post(p_id, p_text, p_post_date, p_email):
    u = User.get(email=p_email)
    if u == None:
        print('user does not exists')
        return
    p = Post.get(id=p_id)
    if p == None:
        Post(id=p_id, text=p_text, post_date=p_post_date, author=u)
        commit()
    else:
        p.set(text=p_text, post_date=p_post_date, author=u)
        commit()

@db_session
def delete_user(p_email):
    u = User.get(email=p_email)
    if u == None:
        print('user not found')
    else:
        u.delete()
        commit()
        
@db_session
def delete_post(p_id):
    p = Post.get(id=p_id)
    if p == None:
        print('post not found')
    else:
        p.delete()
        commit()

@db_session
def print_post_by_user(p_email):
    p = select(p for p in Post if p.author.email == p_email)
    for i in p:
        print(i.id, i.text, i.post_date, i.author.email, i.author.name)

@db_session        
def print_post_by_content_email(p_email, p_contains):
    p = select((u.name, p.id, p.text, p.post_date) for u in User for p in Post if p_contains in p.text and u.email == p_email)
    for i in p:
        print(i[0], i[1], i[2], i[3])

@db_session
def print_all_users():
    q = select(u for u in User)
    for i in q:
        print(i.email, i.name)

@db_session
def print_all_posts():
    q = select(p for p in Post)
    for i in q:
        print(i.id, i.text, i.post_date, i.author.email, i.author.name)