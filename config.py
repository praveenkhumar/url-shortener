# Configuration settings

import os

class Config:
    # Secret key for form protection and session management
    SECRET_KEY = os.urandom(24)
    
    # Database connection string
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/url_shortener'
    
    # Disable SQLAlchemy modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False