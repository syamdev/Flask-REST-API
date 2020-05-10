from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///home/syam/Flask/Flask-REST-API/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
