from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from project_name.models.auth import Token
from datetime import datetime, timezone
from project_name.utils.security import authenticate_user


# set up router
router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


# --- Mock user store ---
fake_users_db = {
    "alice": {"username": "alice", "password": "wonderland"},
    "bob": {"username": "bob", "password": "builder"},
}


# --- Endpoints ---


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Basic username/password authentication.
    Returns a fake access token for demo purposes.
    """
    if not authenticate_user(
        username=form_data.username, password=form_data.password, db=fake_users_db
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Fake token generation for demo
    access_token = f"token-for-{form_data.username}"
    expires_in = 3600  # 1 hour

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": expires_in,
    }


@router.get("/verify-token")
async def verify_token(token: str):
    """
    Dummy token verification endpoint.
    """
    if not token.startswith("fake-token-for-"):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    username = token.removeprefix("fake-token-for-")
    return {
        "valid": True,
        "user": username,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
