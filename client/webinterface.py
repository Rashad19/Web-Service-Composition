"""
Integrated Client

This is our Integrated client Application
It calls Web Service 1,2 and 3 and takes care of
parsing the response data, and it also
renders the web user interface (html/css)

Authors: Rashad Salim and Bassam Yahya

"""

import requests
from flask import Flask, render_template, request

WebInterface = Flask(__name__)

# This is the homepage function which renders
# our homepage html
@WebInterface.route('/client/')
def index():
    return render_template("index.html")


# This where we get and parse data from the external client
# Our External API is Wikipedia with the endpoint
# http://en.wikipedia.org/w/api.php
# it gets pages with title = place.
@WebInterface.route('/client/external/<string:place>', methods=['GET'])
def get_external(place):
    # creating a request session
    session = requests.Session()

    # base URL of our external API
    URL = 'http://en.wikipedia.org/w/api.php'

    # this is our get request parameters
    # place is the search query
    # prop is 'extracts' ensures a summary is returned from the page
    query_params = {
        'action': 'query',
        'titles': place,
        'prop': 'extracts',
        'format': 'json',
        'explaintext': '',
        'exintro': '',
    }

    # getting the response from the wikipedia api
    # this response is a page from the api
    # corresponding to a wikipedia pages that has titles = places
    # this returns one page, since titles are unique.
    response = session.get(url=URL, params=query_params)

    summary = response.json()

    # here we are parsing the json response
    # to get the attribute of the json structure
    # we need to access 'extract attribute'
    keylist = summary['query']['pages'].keys()
    for key in keylist:
        page_id = key

    # here we render the template and pass 'extract' attribute of our response json
    # and this is a summary of the page
    return render_template("external.html", summary=summary['query']['pages'][page_id]['extract'], place=place)


# This function gets the places from webservice 2
# using the country as a parameter
@WebInterface.route('/client/countries/<string:country>', methods=['GET'])
def get_places(country):

    # defining BASE_URL to web service 2
    BASE = "http://127.0.0.1:8080/"

    # requesting the data from the web service using country as a parameter
    response = requests.get(BASE + "countries/" + country)

    # retrieving json of the response object
    place_json = response.json()

    return render_template("places.html", place=place_json)


# This is where we return facts using a number
# between 0 and 9 it calls web service 1 with this
# with this number, and the API returns
@WebInterface.route('/client/facts', methods=['POST', 'GET'])
def get_facts():
    # getting user selected input
    number = request.form['invoke_api_1']

    # calling web service 1 with the user input
    response = requests.get('http://127.0.0.1:5000/facts/' + str(number))

    # getting the json of the response (deserializing)
    facts_json = response.json()

    # Render the fact template and pass the argument 'fact'
    # And 'country' for the next call.
    return render_template("fact.html", fact=facts_json['fact'], country=facts_json['country'])


if __name__ == '__main__':
    WebInterface.run(debug=True, port=9999)
