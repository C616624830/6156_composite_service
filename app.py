from flask import *
from flask_cors import CORS
import json
import logging
import middleware.async_helper as asy
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def fun():
    if request.method == "GET":
        template = request.args.to_dict()
        template = {k: v for k, v in template.items() if
                    v}  # remove key-value pairs where value is empty such as 'father': ''
        print("template: ", template)
        print("headers: ", request.headers.get("Email"))
        if (template.get("cat_id") == None or
            template.get("breeder_id") == None
            ):
            return Response(json.dumps({"code": "300", "message": "request does not have data or cat is none"}),
                            content_type="application/json")

        cat_id = template.get("cat_id")
        breeder_id = template.get("breeder_id")
        print("cat_id: ", cat_id)
        print("breeder_id: ", breeder_id)
        res = asyncio.run(asy.main(cat_id, breeder_id, request.headers))
        print("async run res: ", res[0].json(), res[1].json())
        # return Response(json.dumps({"code": "200", "message": {"cat": res[0].json(), "breeder": res[1].json()}}),
        #                     content_type="application/json")
        return Response(json.dumps({"cat": res[0].json(), "breeder": res[1].json()}, default=str), status=200, content_type="application/json")
    else:
        return



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
