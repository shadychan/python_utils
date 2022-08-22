import requests as re
import json

url = "https://xxx/xxx/xxx/register"
headers = {
    "content-type": "application/json"
}
body = {
    "name": "Shady",
    "age": 25,
    "hobby": ["code", "basketball"],
    "married": False
}

if __name__ == '__main__':
    resp = re.post(url, headers=headers, data=json.dumps(body))
    if resp.status_code != 200:
        print("response code:", resp.status_code)
        print("response text:", resp.text)
        exit()
    print(resp.text)
    rj = json.loads(resp.text)
    # read data from rj...
