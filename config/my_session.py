from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = f"mysql+pymysql://root:root@mysql:3306/contract"
engine = create_engine(DB_URI)
conn = engine.connect()
Base = declarative_base(engine)
session = sessionmaker(engine)()
