import requests
import asyncio

async def main(cat_id, breeder_id, headers):
    L = await asyncio.gather(
        search_cat(cat_id, headers),
        search_breeder(breeder_id, headers)
    )
    print("main_L: ", L)
    return L


async def search_cat(cat_id, headers):
    para = {"id": cat_id}
    headers = {"Email" : headers.get("Email"), "id_token" : headers.get("id_token")}
    res = requests.get(url="https://d25a811kxhsede.cloudfront.net/dev/getcats", params=para, headers=headers)
    print("cat_res: ", res)
    return res

async def search_breeder(breeder_id, headers):
    para = {"id": breeder_id}
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    res = requests.get(url="https://d25a811kxhsede.cloudfront.net/dev/getbreeders", params=para, headers=headers)
    print("breeder_res: ", res)
    return res


# def parse_cat_breeder(cat_info, breeder_info):
#     if (cat_info.get("status") != "200" or breeder_info.get("status") != "200"):
#         return ret_message("300","get cat or breeder info error")
#     else:
#         return ret_message("200", {"cat": cat_info["message"], "breeder": breeder_info["message"]}, {**cat_info["headers"], **breeder_info["headers"]})