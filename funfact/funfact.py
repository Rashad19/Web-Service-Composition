"""
REST API of Web Service1

This is an implementation of a REST API
using flask-restful, it provides the
GET method to the client, which takes a
number as input, and returns back a fact

Author: Rashad Salim

"""

from flask import Flask, jsonify
from flask_restful import Resource, Api
import sqlite3

# creating a flask instance
# and using __name__ to tell flask to look for resources
# relative to this file
service = Flask(__name__)

# here we initialize our REST-API instance
service_api = Api(service)


# This Connects to our database
# and returns a connection object to the caller
def connect_db(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except sqlite3.Error as E:
        print('failed to connect')


# this converts the data object retrieved from the query
# to a dictionary, which is essentially JSON.
# hence here we are using json as a data format in our API
def get_dict(cursor, data, connection):
    dict = {}
    i = 0
    # populating the dictionary
    # with 'attribute': value
    for row in cursor.description:
        dict[str(row[0])] = data[0][i]
        i += 1
    cursor.close()
    connection.close()
    return dict


# This gets the fact which has the fact_id as primary key
# It executes an SQL query, to find the fact instance
# in the database
def get_fact(connection, fact_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM facts WHERE fact_id = ?", [fact_id])
    data = cursor.fetchall()
    return get_dict(cursor, data, connection)


# This is our API class, which provides a method to
# interact with the database (.db file)
# which provide an interface to the client.
class FunFact(Resource):

    # initializing database name
    def __init__(self):
        self.db = 'facts.db'

    # This is our Resource get method
    # It supplies the facts to the client
    def get(self, fact_id):
        return jsonify(get_fact(connect_db(self.db), fact_id))


# here we the define the resources that will be used.
# using fact_id as an argument
service_api.add_resource(FunFact, '/facts/<int:fact_id>')

# Ensuring service.run() runs first
if __name__ == '__main__':
    service.run(debug=True)
