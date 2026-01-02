from fastapi import Header, HTTPException

API_KEY = "my_secret_key_123"

def get_current_user(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return "authorized_user"