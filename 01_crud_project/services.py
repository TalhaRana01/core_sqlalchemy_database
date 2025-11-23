from database import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete


# Insert user in table

def create_user(name: str, email: str):
  with engine.connect() as conn:
    statement = insert(users).values(name=name, email=email)
    conn.execute(statement)
    conn.commit()
  