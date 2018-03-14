#!/usr/bin/env python

import urllib
import json
import os
import csv

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
        
        result = req.get("result")
        parameters = result.get("parameters")
        zone1 = parameters.get("Users")
        zone = zone1.lower()
        csv_file = csv.reader(open('users.csv'), delimiter=",")
       
        for row in csv_file:    
            if zone == row[0]:
                speech = ("\n\nHi " + row[1] + " you are enrolled under the " + row[2] + " with " + row[3])
        
        print(speech)
        
        
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "cust_plan"
               }
    
    elif req.get("result").get("action") == "Complaint_status.Complaint_status-selectnumber.Complaint_status-customer-id-custom":
        result = req.get("result")
        parameters = result.get("parameters")
        zone1 = parameters.get("Users")
        zone = zone1.lower()
        
        
        csv_file = csv.reader(open('complaint.csv'), delimiter=",")
       
        for row in csv_file:    
            if zone == row[0]:
                speech = ("\n\nHi " + row[1] + "\nyour complaint id: " + row[2] + "\nType of complaint: " + row[3] + "\nComment: " + row[4] + "\nStatus: " + row[5])
        
        
        print("Response:")
        print(speech)
        return{
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "Complaint_status - customer-id - custom"
              }
        
    elif req.get("result").get("action") == "Complaint_status.Complaint_status-custom.Complaint_status-complaint_id-custom":
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("number")
        
        
        
        csv_file = csv.reader(open('complaint.csv'), delimiter=",")
       
        for row in csv_file:    
            if str(zone) == row[2]:
                speech = ("\n\nHi " + row[1] + "\nyour complaint id: " + row[2] + "\nType of complaint: " + row[3] + "\nComment: " + row[4] + "\nStatus: " + row[5])
        
        
        print("Response:")
        print(speech)
        return{
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "Complaint_status - complaint_id - custom"
              }
      
    
    
        
    
    else:
       return{}
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
