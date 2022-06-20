from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from os.path import isfile
from create_db2 import create2

# Create a Flask app and an SQLAlchemy database
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Places(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)
    city = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Place('{self.name}', '{self.city}', '{self.country}')"

# Checks if database file does not exists it creates and populates db
# Uses create2 from file create_db2.py
if not isfile("db2.db"):
    db.create_all()
    create2()

# A dictionary to define database model to be used in getPlaces
resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'city': fields.String,
    'country': fields.String
}

# Used to retrieve all places where country is equal to the input
# @marshal_with is used to serialize the data and present it in json format
class getPlaces(Resource):
    @marshal_with(resource_fields)
    def get(self, cntry):
        result = Places.query.filter_by(country=cntry).all()
        return result

# Api created to allow web service 1 to connect
api.add_resource(getPlaces, "/countries/<string:cntry>")

# Port to run application
if __name__ == "__main__":
    app.run(debug=True, port=8080)
