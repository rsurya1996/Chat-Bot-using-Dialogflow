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
    if req.get("result").get("action") != "cust_plan.cust_plan-custom":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("Users")

    cost = {'C0001':'Cricket Basic Validity 12-12-18', 'C0002':'Cricket Infinity Validity 1-6-18', 'C0003':'Cricket Student Validity 5-2-18', 'C0004':'Cricket Family Validity 6-6-18', 'C0005':'Cricket Basic Validity 28-2-18', 'C0006':'Cricket Infinity Validity 5-5-18', 'C0007':'Cricket Plus Vality 31-12-18', 'C0008':'Cricket Plus Validity 12-10-18', 'C0009':'Cricket Student Validity 25-5-18', 'C0010':'Cricket Family Validity 22-8-18', 'C0011':'Cricket Basic validity 22-4-18', 'C0012':'Cricket Plus Validity 22-3-18', 'C0013':'Cricket Infinity Validity 28-6-18'}

    speech = "Hi" + zone + " you are enrolled under" + str(cost[zone])
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
