from database import engine
from sqlalchemy import MetaData, Table, Column, Integer, String


metadata = MetaData()


# User table

users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(length=50), nullable=False),
  Column("email", String, nullable=False, unique=True)
  
)

# Create Table in Database

def create_tables():
  metadata.create_all(engine)
  
# def delete_tables():
#   metadata.drop_all()
