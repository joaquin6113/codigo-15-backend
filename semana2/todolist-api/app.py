from flask import Flask
from app.routes.tasks import task_route
from app.routes.users import user_route
from app.db import db
from app.crypt import bcrypt
from app.jwt import jwt
from app.config import Config
from flask_cors import CORS

# instancia de Flask
app = Flask(__name__) # módulo actual --> __name__
CORS(app)

app.config.from_object(Config)

app.register_blueprint(task_route) #blueprint --> módulo de la db
app.register_blueprint(user_route)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True) # Esto permite que el servidor se actualice con cada cambio