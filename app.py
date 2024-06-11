import requests
import sys

original_stdout = sys.stdout

with open("output.json", "w") as f:
    sys.stdout = f
    rastreio = [
        "OY399286596BR"
    ]
    url = "https://api.17track.net/track/v2.2/register"
    payload =  [
  {
    "number": f"{rastreio[0]}",
    "lang": "en",
    "email":"",
    "param": "",
    "order_no": "",
    "order_time": "",
    "carrier": "",
    "final_carrier": "",
    "auto_detection": True,
    "tag": "",
    "remark": ""
  }
    ]
    headers = {
        "content-type": "application/json",
        "17token": ""
    }
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

