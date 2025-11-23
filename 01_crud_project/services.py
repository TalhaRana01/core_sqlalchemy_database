from database import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete



# Insert user in table
def create_user(name: str, email: str):
  with engine.connect() as conn:
    statement = insert(users).values(name=name, email=email)
    conn.execute(statement)
    conn.commit()  
    
 


    

# Get single User
def get_user_by_id(user_id: int):
  with engine.connect() as conn:
    statement = select(users).where(users.c.id == user_id)
    result = conn.execute(statement).first()
    return result
  

# Get all User
def get_all_users():
  with engine.connect() as conn:
    statement = select(users)
    result = conn.execute(statement).fetchall()
    return result


# Get Post by User
def get_post_by_user_id(user_id: int):
  with engine.connect() as conn:
    statement = select(posts).where(posts.c.id == user_id)
    result = conn.execute(statement).first()
    return result


# Update User Email
def update_user_email(user_id: int, new_email: str):
  with engine.connect() as conn:
    statement = update(users).where(users.c.id == user_id).values(email=new_email)
    conn.execute(statement)
    conn.commit()
    

# Delete User 
def delete_user(user_id: int):
  with engine.connect() as conn:
    statement = delete(users).where(users.c.id == user_id)
    conn.execute(statement)
    conn.commit()
    


# Insert post in table
def create_post(user_id: str, title:str, content: str):
  with engine.connect() as conn:
    statement = insert(posts).values(user_id=user_id, title=title, content=content)
    conn.execute(statement)
    conn.commit()
    
    
# Update Post title
def update_post_title(post_id: int, new_title: str):
  with engine.connect() as conn:
    statement = update(posts).where(posts.c.id == post_id).values(title=new_title)
    conn.execute(statement)
    conn.commit()


# Delete Post
def delete_post(post_id:int):
  with engine.connect() as conn:
    statement = delete(posts).where(posts.c.id == post_id)
    conn.execute(statement)
    conn.commit()