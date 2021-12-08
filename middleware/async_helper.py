import json
import requests
import asyncio

id_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkzNDFhYmM0MDkyYjZmYzAzOGU0MDNjOTEwMjJkZDNlNDQ1MzliNTYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiNzgzNTgwOTQxMjQ4LWZocGc1MXZwcDd0bnA0bDNoYmJqa2JtYzJrNDducjFkLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiNzgzNTgwOTQxMjQ4LWZocGc1MXZwcDd0bnA0bDNoYmJqa2JtYzJrNDducjFkLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE2NTA0MzM1NTMxNjg3NDkzMjMwIiwiZW1haWwiOiJjaGVuNjE2NjI0ODMwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoidnVvd1E5cUNVUHBwX1FhZGlfdklpdyIsIm5hbWUiOiJDaGVuIExpZXlhbmciLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUFUWEFKd0J0dGkzMlh1WE4xZ2ZRYlhoNDlnRXJrNVNGZzE5b1B4eVh3UGI9czk2LWMiLCJnaXZlbl9uYW1lIjoiQ2hlbiIsImZhbWlseV9uYW1lIjoiTGlleWFuZyIsImxvY2FsZSI6InpoLUNOIiwiaWF0IjoxNjM4ODk0MTU1LCJleHAiOjE2Mzg4OTc3NTUsImp0aSI6ImIzMGNlOTRmMjExMDdjZWM2YmZhMGU4MTFhZWVhZjEzMTZlMTRiZmQifQ.NvDVlK4xMaFdN1XWa83r-X8ohLR5Bs37cPzUmlIPReN4Xain3sJdHyAG-lO0fA27lFjSuBSkUCarGfLK8mLPgHX6JBp6juvIxUwG9r31G8aAEwBtEn3f7UnVGfcYf7xBLqPyZxdzoEklzD8OnVJTIS1zh7Mc4h6PaKRGbBf5Jip7AT1L8NE4L70Kaxs0mjWFRHrkIgXo5vFibleHAGAl52pU9OdTX_R-IiNDxHc74zD9edldCt66GE95yLU2w3BP9xqUipRagH2hz8Q3qXfMLhl91lO-77FXl2bFXlaemxymcsNlwGoZRPqeeaXQg2m7NHegVglfsstSQZ3-Hx4pCg"

async def main(cat_id, breeder_id):
    L = await asyncio.gather(
        search_cat(cat_id),
        search_breeder(breeder_id)
    )
    print("main_L: ", L)
    return L



async def search_cat(cat_id):
    para = {"id": cat_id}
    headers = {'Content-Type': 'text/plain', 'id_token': id_token, 'Email': "chen616624830@gmail.com"}
    res = requests.get(url=b"http://3.16.40.130:5000/cats", params=para, headers=headers)
    print("cat_res: ", res.json())
    return res

async def search_breeder(breeder_id):
    para = {"id": breeder_id}
    headers = {'Content-Type': 'text/plain', 'id_token': id_token, 'Email': "chen616624830@gmail.com"}
    res = requests.get(url=b"http://3.16.40.130:5000/breeders", params=para, headers=headers)
    print("breeder_res: ", res.json())
    return res