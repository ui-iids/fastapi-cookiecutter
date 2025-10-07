from pydantic import BaseModel


# --- Models ---


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
