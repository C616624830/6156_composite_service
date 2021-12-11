import requests
import asyncio
from composite_services.utility import ret_message
import json

def parse(info1, info2):
    if (info1.get("status")[0] != '2'):
        return ret_message(info1.get("status"),info1.get("message"))
    elif (info2.get("code")[0] != '2'):
        return ret_message(info2.get("status"), info2.get("message"))
    else:
        return ret_message("201", "success", {**info1["headers"], **info2["headers"]})

def helper(request):
    print("request.get_json(): ", request.get_json())
    template = request.get_json()

    if not template:
        return ret_message("400", "error")

    template1 = {k: v for k, v in template.items() if
                v and k!='id_token' and k!='Email'}
    template2 = {k: v for k, v in template.items() if
                 v and (k == 'Name' or k == 'Email' or k == 'id_token')}

    res = asyncio.run(main(template1, template2, request.headers))
    print("res[0].json: ", res[0])
    print("res[1].json: ", res[1])
    return parse(res[0], res[1])

async def main(template1, template2, headers):
    L = await asyncio.gather(
        post_searchdb_breeder(template1, headers),
        post_userdb_breeder(template2, headers)
    )
    print("main_L: ", L)
    return L


async def post_searchdb_breeder(template, headers):
    headers = {"Email" : headers.get("Email"), "id_token" : headers.get("id_token")}
    res = requests.post(url="https://d25a811kxhsede.cloudfront.net/dev/postbreeders", data=template, headers=headers)
    print("searchdb_res: ", res.json())
    return res.json()

async def post_userdb_breeder(template, headers):
    print("template: ", template)
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    print("headers: ", headers)
    res = requests.post(url="https://d25a811kxhsede.cloudfront.net/dev/user", data=template, headers=headers)
    print("userdb_res: ", res.json())
    return res.json()