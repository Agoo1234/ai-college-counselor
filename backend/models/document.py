from flask_mongoengine import MongoEngine

db = MongoEngine()

class Document(db.Document):
    title = db.StringField(required=True)
    content = db.StringField(required=True)
    user_id = db.ReferenceField('User', required=True)
    created_at = db.DateTimeField(required=True)
    updated_at = db.DateTimeField(required=True)
