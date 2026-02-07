import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()
DB_url = os.getenv('DATABASE_URL')
engine = create_engine(DB_url)
sessionLocal = sessionmaker(engine)
Base = declarative_base()
