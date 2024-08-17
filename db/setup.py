from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

SQLITE_DATABASE = 'sqlite:///./todo.db'

engine = create_engine(SQLITE_DATABASE, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()