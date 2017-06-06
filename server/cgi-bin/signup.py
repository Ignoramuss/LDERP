#!/home/mayank/Envs/lderp/bin/python
import cgi
from db import insert_in_collection
from config import API_KEY_USER

import cgitb
cgitb.enable(display=0, logdir="server.log")

def cgiFieldStorageToDict( fieldStorage ):
   """Get a plain dictionary, rather than the '.value' system used by the cgi module."""
   params = {}
   for key in fieldStorage.keys():
      params[ key ] = fieldStorage[ key ].value
   return params

form_data = cgi.FieldStorage()
required_parameters = ["key", "name", "password", "email"]
key = form_data['key'].value
print('Content-type: text/html\n')
if key not in API_KEY_USER:
    print("Unauthorized access")
else:
    dev_access_user = API_KEY_USER[key]
    print("Hi", dev_access_user + "!")
    missing_data = False
    for param in required_parameters:
        if param not in form_data:
            print(param, "field not set")
            missing_data = True
            break
    if not missing_data:
        form_data_dict = cgiFieldStorageToDict(form_data)
        success = insert_in_collection("teachers", form_data_dict)
        if success:
             print("Success")
        else:
            print("Failed to update database")
