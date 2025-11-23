from database import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete


# Insert user in table

def create_user(name: str, email: str):
  with engine.connect() as conn:
    statement = insert(users).values(name=name, email=email)
    conn.execute(statement)
    conn.commit()  
    
 
# Insert post in table

def create_post(user_id: str, title:str, content: str):
  with engine.connect() as conn:
    statement = insert(posts).values(user_id=user_id, title=title, content=content)
    conn.execute(statement)
    conn.commit()
    

# Get single user 
def get_user_by_id(user_id: int):
  with engine.connect() as conn:
    statement = select(users).where(users.c.id == user_id)
    result = conn.execute(statement).first()
    return result
  

def get_all_users():
  with engine.connect() as conn:
    statement = select(users)
    result = conn.execute(statement).fetchall()
    return result
  
def get_post_by_user_id(user_id: int):
  with engine.connect() as conn:
    statement = select(posts).where(posts.c.id == user_id)
    result = conn.execute(statement).first()
    return result