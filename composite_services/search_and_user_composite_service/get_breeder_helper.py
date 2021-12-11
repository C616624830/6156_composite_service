import requests
import asyncio
from composite_services.utility import ret_message

def parse(info1, info2):
    if (info1.get("status")[0] != '2' or info2.get("code")[0] != '2'):
        return ret_message("400","error")
    else:
        msg1 = info1['message'].get('data')
        # msg2 = info2['message']
        # print("info1['message']: ", info1["message"])
        # print("info1['message'].get('data'): ", info1['message'].get('data'))
        # print("info1['message'].get('data')[0]: ", info1['message'].get('data')[1])
        return ret_message("200", msg1, {**info1["headers"], **info2["headers"]})

def helper(request):
    print("request.args.to_dict: ", request.args.to_dict)
    template = request.args.to_dict()
    template1 = {k: v for k, v in template.items() if
                 v and k != 'id_token' and k != 'Email'}
    template2 = {k: v for k, v in template.items() if
                 v and (k == 'Name' or k == 'Email' or k == 'id_token')}

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