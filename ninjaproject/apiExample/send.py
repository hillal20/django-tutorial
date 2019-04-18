import requests 

headers ={}
headers['Authorization'] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTMzMjY0OTQ4LCJqdGkiOiI3OTQyMDViMjYwMGY0NGZjYTVmZDFhOGIzMzBmNDU5MyIsInVzZXJfaWQiOjF9.s_aREfHhOF98_c1JaKvsE9od_HkXbUvbq99p7I8Ie5M"
r = requests.get('http://localhost:8000/paradigms',headers=headers)
print(r.text)