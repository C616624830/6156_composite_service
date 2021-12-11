import json
from flask import *

def ret_message(status, message, headers ={}):
    j = json.dumps({"status": status, "message": message, "headers": headers}, default=str)
    print("json response: ", j)
    return Response(j, content_type="application/json")
