from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from security.token_verification import Auth0TokenVerifier

token_auth_scheme = HTTPBearer()


def authenticated(credentials: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    result = Auth0TokenVerifier(credentials.credentials).verify()
    status = result.get("status")
    if status:
        raise HTTPException(status_code=403, detail=f"You are not allowed to access this endpoint.")
    return credentials.credentials
