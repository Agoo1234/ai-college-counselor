from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine()

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    name = db.StringField(required=True)
    dream_college = db.StringField()
    is_admin = db.BooleanField(default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
