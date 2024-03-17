from dataclasses import dataclass


@dataclass
class UserCreateDTO:
    public_id: str
    name: str
    role: str
    email: str
