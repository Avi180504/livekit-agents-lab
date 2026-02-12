import jwt
import time

api_key = "APIi6op6WaS8Lao"
api_secret = "VZkeL1J4xJqUYiXOrz8b9WehQ4je82lHFLiks3kAQ9VB"

payload = {
    "iss": api_key,
    "sub": "test-user",
    "nbf": int(time.time()),
    "exp": int(time.time()) + 3600,
    "video": {
        "room": "test-room",
        "roomJoin": True,
        "canPublish": True,
        "canSubscribe": True
    },
    "agent": {
        "name": "echo-agent"
    }
}

token = jwt.encode(payload, api_secret, algorithm="HS256")
print("\nYOUR TOKEN:\n")
print(token)

