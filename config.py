import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SeCrEt-KeY' # Replace with environment variable if using for production.