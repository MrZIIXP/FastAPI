import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_url = os.getenv('DATABASE_URL')
engine = create_engine(DB_url)
sessionLocal = sessionmaker(engine)
Base = declarative_base()
