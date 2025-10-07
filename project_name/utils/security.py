from typing import List, Any, Dict, Optional, Tuple, Callable, Union, Literal


def authenticate_user(username: str, password: str, db: Dict[str, Any]) -> bool:
    user = db.get(username)
    if not user or user["password"] != password:
        return False
    return True
