import requests

response = requests.post(
    "http://127.0.0.1:5000/chat",
    json={"message": "who am i to you bro?"}
)

print("Status Code:", response.status_code)
print("Raw Text:", response.text)