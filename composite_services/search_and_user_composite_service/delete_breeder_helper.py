import requests
import asyncio
from composite_services.utility import ret_message


def parse(info1, info2):
    if (info1.get("status")[0] != '2'):
        return ret_message(info1.get("status"),info1.get("message"))
    elif (info2.get("code")[0] != '2'):
        return ret_message(info2.get("code"), info2.get("message"))
    else:
        return ret_message("204", "success", {**info1["headers"], **info2["headers"]})


def helper(request):
    print("request.headers.get('Email'): ", request.headers.get('Email'))
    id = request.headers.get('Email')
    if not id:
        return ret_message("422", "you did not provide email to be deleted")

    res = asyncio.run(main(id, request.headers))
    print("res[0].json: ", res[0])
    print("res[1].json: ", res[1])
    return parse(res[0], res[1])


async def main(id, headers):
    L = await asyncio.gather(
        delete_searchdb_breeder(id, headers),
        delete_userdb_breeder(id, headers)
    )
    print("main_L: ", L)
    return L


async def delete_searchdb_breeder(id, headers):
    data = {"id": id}
    headers = {"Email" : headers.get("Email"), "id_token" : headers.get("id_token")}
    res = requests.delete(url="https://d25a811kxhsede.cloudfront.net/dev/breeders", data=data, headers=headers)
    print("searchdb_res: ", res.json())
    return res.json()

async def delete_userdb_breeder(id, headers):
    data = {"id": id}
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    res = requests.delete(url="https://d25a811kxhsede.cloudfront.net/dev/user", data=data, headers=headers)
    print("userdb_res: ", res.json())
    return res.json()


# def parse_delete_breeder(searchdb_info, userdb_info):
#     if (searchdb_info.get("status") != "200" or userdb_info.get("status") != "200"):
#         return ret_message("400","get cat or breeder info error")
#     else:
#         return ret_message("200", {"cat": searchdb_info["message"], "breeder": userdb_info["message"]}, {**searchdb_info["headers"], **userdb_info["headers"]})