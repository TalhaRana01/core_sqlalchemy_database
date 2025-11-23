from database import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey


metadata = MetaData()


# User table

users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(length=50), nullable=False),
  Column("email", String, nullable=False, unique=True)
  
)

##-------------------------
# ONE TO MANY Relationship
##-------------------------

## User create multiple posts 
posts = Table(
  "posts",
  metadata,
  Column("id", Integer, primary_key=True),
  
  # User and Post Relationship
  Column("user_id",Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True ),
  
  Column("title", String, nullable=False),
  Column("content", String, nullable=False)
)


##-------------------------
# ONE TO ONE Relationship
##-------------------------

profile = Table(
  "profile",
  metadata, 
  Column("id", Integer, primary_key=True),
  
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),
  
  Column("name", String, nullable=False, unique=True),
  Column("bio", String, nullable=False),
  Column("address", String, nullable=False)
)


##--------------------------
# MANY TO MANY Relationship
##--------------------------

address = Table(
  "address",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("street", String, nullable=False),
  Column("country", String, nullable=False)
)

user_address_association = Table(
  "user_address_association",
  metadata,
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
  Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
  
)

# Create Table in Database

def create_tables():
  metadata.create_all(engine)


# Delete Table in Database

# def delete_tables():
#   metadata.drop_all()
