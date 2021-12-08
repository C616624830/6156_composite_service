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
    res = requests.get(url="https://zhm5v3fgp5.execute-api.us-east-2.amazonaws.com/dev/cats", params=para, headers=headers)
    print("cat_res: ", res)
    return res

async def search_breeder(breeder_id, headers):
    para = {"id": breeder_id}
    headers = {"Email": headers.get("Email"), "id_token": headers.get("id_token")}
    res = requests.get(url="https://zhm5v3fgp5.execute-api.us-east-2.amazonaws.com/dev/breeders", params=para, headers=headers)
    print("breeder_res: ", res)
    return res