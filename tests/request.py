from requests import get, post


host = "http://127.0.0.1:8000/posts/"

req_get = get(url=host)
print(req_get)
print(req_get.json())

post_data =  {"title": "Hi this is me", "post_content": "Just testing this stuff"}
req_post = post(host, json=post_data)
print(req_post)
print(req_post.json())