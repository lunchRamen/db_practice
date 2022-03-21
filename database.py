import json
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, ".vscode/secrets.json")
secrets = json.loads(open(SECRET_FILE).read())

DB = secrets["DB"]


DB_URL = f"postgresql+psycopg2://{DB['username']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}"  # noqa

engine = create_engine(DB_URL, encoding="utf-8")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
