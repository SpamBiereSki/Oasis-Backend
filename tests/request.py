from requests import get, post
from pprint import pprint


host = "http://127.0.0.1:8000/comments/"

post_data =  {"content": "Un commentaire très utile.", "idpost": "5"}
req_post = post(host, json=post_data)
print(req_post)
print(req_post.json())

req_get = get(url=host)
pprint(req_get)
pprint(req_get.json())
