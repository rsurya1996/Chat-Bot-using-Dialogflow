#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "cust_plan.cust_plan-custom":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("Users")

    name = {'C0001':'John', 'C0002':'Patterson', 'C0003':'Tim', 'C0004':'Merl', 'C0005':'Robert', 'C0006':'Andrea', 'C0007':'Lucy', 'C0008':'Nicole', 'C0009':'Breanna', 'C0010':'Daniel', 'C0011':'Mason', 'C0012':'Sasha', 'C0013':'Baylee', 'C0014':'Gabrial'}
    cost = {'C0001':'Cricket Basic', 'C0002':'Cricket Infinity', 'C0003':'Cricket Student ', 'C0004':'Cricket Family', 'C0005':'Cricket Basic', 'C0006':'Cricket Infinity', 'C0007':'Cricket Plus', 'C0008':'Cricket Plus', 'C0009':'Cricket Student', 'C0010':'Cricket Family', 'C0011':'Cricket Basic', 'C0012':'Cricket Plus', 'C0013':'Cricket Infinity', 'C0014':'Cricket Student'}
    validity = {'C0001':'Validity 12-12-18', 'C0002':'Validity 1-6-18', 'C0003':'Validity 5-2-18', 'C0004':'Validity 6-6-18', 'C0005':'Validity 28-2-18', 'C0006':'Validity 5-5-18', 'C0007':'Vality 31-12-18', 'C0008':'Validity 12-10-18', 'C0009':'Validity 25-5-18', 'C0010':'Validity 22-8-18', 'C0011':'validity 22-4-18', 'C0012':'Validity 22-3-18', 'C0013':'Validity 28-6-18',  'C0014':'Validity 4-4-18'}
    speech = "Hi " + str(name[zone]) +" (" + zone + " ) you are enrolled under " + str(cost[zone] + " with " + str(validity[zone]))
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "cust_plan"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
