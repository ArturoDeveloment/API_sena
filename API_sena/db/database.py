import sqlalchemy as sql
from sqlalchemy.ext import declarative
import sqlalchemy.orm as orm
from dotenv import load_dotenv
from sqlalchemy import event
import os

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.getenv('user_db')}:{os.getenv('passwd_db')}@{os.getenv('host_db')}:{os.getenv('port_db')}/{os.getenv('name_db')}"

engine = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()
