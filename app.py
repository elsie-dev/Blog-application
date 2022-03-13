from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from db import db 
from controllers.users import auth,public


app = Flask(__name__)
CORS(app)
api = Api(app,title='Simple RESTFul Service')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///csye6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# with app.app_context():
#     db.create_all()

api.add_namespace(auth)
api.add_namespace(public)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
