from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///./crud.db"
engine = create_engine(DATABASE_URL, echo=True)