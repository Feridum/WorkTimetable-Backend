from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://%s:%s@%s/%s?driver=SQL+Server' % (config['database']['user'], config['database']['password'], config['database']['server'], config['database']['database'])


db = SQLAlchemy(app)
