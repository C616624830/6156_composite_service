import json
from flask import *

def ret_message(status, message, headers ={}):
    j = json.dumps({"status": status, "message": message, "headers": headers}, default=str)
    print("json response: ", j)
    return Response(j, content_type="application/json")

def parse(info1, info2):
    if (info1.get("status")[0] != '2' or info2.get("code")[0] != '2'):
        return ret_message("400","error")
    else:
        msg1 = info1["message"]
        msg2 = info2["message"]
        if (type(msg1) is list):
            if msg1:
                msg1 = msg1[0]
            else:
                msg1 = {}
        if (type(msg2) is list):
            if msg2:
                msg1 = msg1[0]
            else:
                msg2 = {}
        if (type(msg1) is str or type(msg2) is str):
            return ret_message("200", "success", {**info1["headers"], **info2["headers"]})
        else:
            return ret_message("200", {**msg1, **msg2}, {**info1["headers"], **info2["headers"]})