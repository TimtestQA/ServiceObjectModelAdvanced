import requests

insult = requests.get("https://petstore.swagger.io/v2/pet/123",)

print(insult.json())