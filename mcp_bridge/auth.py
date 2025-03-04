from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from mcp_bridge.config import config

security = HTTPBearer(auto_error=False)

async def get_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Validate the API key provided in the Authorization header.
    
    If no API key is configured in the server settings, authentication is skipped.
    If an API key is configured, the request must include a matching API key.
    
    The API key should be provided in the Authorization header as:
    Authorization: Bearer your-api-key-here
    """
    # If no API key is configured, skip authentication
    if not config.api_key:
        return True
    
    # If API key is configured but not provided in the request
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is required in Authorization header (Bearer token)",
        )
    
    # If API key is provided but doesn't match
    if credentials.credentials != config.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    
    return True 