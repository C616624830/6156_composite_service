from flask import *
from flask_cors import CORS
import json
import logging
import composite_services.search_and_search_composite.search_breeder_and_cat as asy
import composite_services.search_and_user_composite_service.get_breeder_helper as gb
import composite_services.search_and_user_composite_service.post_breeder_helper as pb
import composite_services.search_and_user_composite_service.delete_breeder_helper as db
from composite_services.utility import parse
from composite_services.utility import ret_message
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/cats_and_breeders', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cats_and_breeders():
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
        message = parse_cat_breeder(res[0].json(), res[1].json())
        # return ret_message("200", {"cat": res[0].json(), "breeder": res[1].json()})
        print("message: ", message)
        return message
    else:
        return


@app.route('/breeders', methods=['GET', 'POST', 'PUT', 'DELETE'])
def breeders():
    if request.method == 'GET':
        res = gb.helper(request)
        return res

    elif request.method == 'POST':
        res = pb.helper(request)
        return res

    elif request.method == 'DELETE':
        res = db.helper(request)
        return res


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
