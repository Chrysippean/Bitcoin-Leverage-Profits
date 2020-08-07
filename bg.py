import requests

url = "https://bungeetech.com/api/v1/crawl"

payload = "url=https%3A%2F%2Fwww.amazon.com&location=all&method=GET"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'x-api-key': API KEY,
    'x-clientid': CLIENT ID,
    }

response = requests.request("POST", url, data=payload, headers=headers)