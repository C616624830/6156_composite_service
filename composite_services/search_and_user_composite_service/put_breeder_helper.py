import requests
import asyncio
from composite_services.utility import ret_message
from composite_services.utility import parse

def helper(request):
    print("request.get_json(): ", request.get_json())
    template = request.get_json()
    template1 = {k: v for k, v in template.items() if
                v and k!='id_token' and k!='Email'}
    template2 = {k: v for k, v in template.items() if
                 v and (k == 'name' or k == 'Email' or k == 'id_token')}

    res = asyncio.run(main(template1, template2, request.headers))
    return parse(res[0].json, res[1].json)


async def main(template1, template2, headers):
    L = await asyncio.gather(
        searchdb_put(template1, headers),
        userdb_put(template2, headers)
    )
    print("main_L: ", L)
    return L


async def put_searchdb_breeder(template, headers):
    headers = {"Email" : headers.get("Email"), "id_token" : headers.get("id_token")}
    res = requests.put(url="https://d25a811kxhsede.cloudfront.net/dev/breeders", data=template, headers=headers)
    print("searchdb_res: ", res)
    return res

async def put_userdb_breeder(template, headers):
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    res = requests.put(url="https://d25a811kxhsede.cloudfront.net/dev/user", data=template, headers=headers)
    print("userdb_res: ", res)
    return res