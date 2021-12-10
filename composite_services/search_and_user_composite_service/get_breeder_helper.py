import requests
import asyncio
from composite_services.utility import ret_message
from composite_services.utility import parse

def helper(request):
    print("request.args.to_dict: ", request.args.to_dict)
    template = request.args.to_dict()
    template1 = {k: v for k, v in template.items() if
                 v and k != 'id_token' and k != 'Email'}
    template2 = {k: v for k, v in template.items() if
                 v and (k == 'name' or k == 'Email' or k == 'id_token')}

    res = asyncio.run(main(template1, template2, request.headers))
    print("res[0].json: ", res[0])
    print("res[1].json: ", res[1])
    return parse(res[0], res[1])

async def main(template1, template2, headers):
    L = await asyncio.gather(
        get_searchdb_breeder(template1, headers),
        get_userdb_breeder(template2, headers)
    )
    print("main_L: ", L)
    return L


async def get_searchdb_breeder(template, headers):
    headers = {"Email" : headers.get("Email"), "id_token" : headers.get("id_token")}
    res = requests.get(url="https://d25a811kxhsede.cloudfront.net/dev/getbreeders", params=template, headers=headers)
    print("searchdb_res: ", res.json())
    return res.json()

async def get_userdb_breeder(template, headers):
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    res = requests.get(url="https://d25a811kxhsede.cloudfront.net/dev/user", params=template, headers=headers)
    print("userdb_res: ", res.json())
    return res.json()