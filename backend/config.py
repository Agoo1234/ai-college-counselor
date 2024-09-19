import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_URI = os.environ.get('MONGODB_URI')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
