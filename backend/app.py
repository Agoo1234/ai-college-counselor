from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes import auth, user, document
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
JWTManager(app)

# Configure SQLAlchemy to use PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@"
    f"{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
)

db = SQLAlchemy(app)

# Import models after db is initialized
from models.user import User
from models.document import Document

# Create tables
with app.app_context():
    db.create_all()

app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.register_blueprint(document.bp)

if __name__ == '__main__':
    app.run(debug=True)
