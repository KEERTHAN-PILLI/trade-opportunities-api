from fastapi import Security, HTTPException, status, Request
from fastapi.security.api_key import APIKeyHeader
from slowapi import Limiter
from slowapi.util import get_remote_address
import os
from dotenv import load_dotenv

load_dotenv()

# Simple API Key Authentication
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    expected_key = os.getenv("API_KEY", "default_secret_key")
    if api_key == expected_key:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials",
    )

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)

# Session tracking (In-memory)
class SessionTracker:
    def __init__(self):
        self.sessions = {}

    def track_request(self, client_id: str):
        self.sessions[client_id] = self.sessions.get(client_id, 0) + 1
        return self.sessions[client_id]

session_tracker = SessionTracker()
