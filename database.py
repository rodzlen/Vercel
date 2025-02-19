import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = os.getenv("postgresql://neondb_owner:npg_PUuf6pzcO8Wr@ep-curly-morning-a8vitdnh-pooler.eastus2.azure.neon.tech/neondb?sslmode=require")

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

