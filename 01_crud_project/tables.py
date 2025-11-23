from database import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey



metadata = MetaData()



users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(length=50), nullable=False),
  Column("email", String, nullable=False, unique=True)
)


posts = Table(
  "posts",
  metadata, 
  Column("id", Integer, primary_key=True),
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False ),
  Column("title", String, nullable=False),
  Column("content", String, nullable=False),
)
  
  



# Table creation function
def create_table():
  metadata.create_all(engine)


# Delete tables
def delete_table():
  metadata.drop_all()