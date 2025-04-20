import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from database import Base

load_dotenv()

postgress_host = os.getenv('POSTGRESS_HOST')
postgress_port = os.getenv('POSTGRESS_PORT')
postgress_database = os.getenv('POSTGRESS_DATABASE')
postgress_user = os.getenv('POSTGRESS_USER')
postgress_password = os.getenv('POSTGRESS_PASSWORD')

engine = create_engine(f"postgresql://{postgress_user}:{postgress_password}"
                       f"@{postgress_host}:{postgress_port}/{postgress_database}?sslmode=require", echo=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

