import sqlalchemy as sql
from sqlalchemy.ext import declarative
import sqlalchemy.orm as orm
from sqlalchemy import event

DATABASE_URL = "mysql+pymysql://api_sena:password@localhost:3306/api_sena"

engine = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()
