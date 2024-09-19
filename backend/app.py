from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from routes import auth, user, document

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
JWTManager(app)

app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.register_blueprint(document.bp)

if __name__ == '__main__':
    app.run(debug=True)
