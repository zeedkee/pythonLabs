# example.py
from pydantic import BaseModel, EmailStr, ValidationError, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    # custom validator (Pydantic v2)
    @field_validator("account_id")
    def account_id_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

def main():
    # valid creation
    user = User(name="Salah", email="salah@gmail.com", account_id=12345)
    print("User created:", user)
    print("name:", user.name)
    print("as dict:", user.model_dump())           # python dict
    print("as json:", user.model_dump_json())      # JSON string

    print("\n-- Trying invalid email / account_id --")
    try:
        bad = User(name="Ali", email="ali", account_id=-5)
    except ValidationError as e:
        print("ValidationError:")
        print(e)

    print("\n-- parse_raw example --")
    json_str = user.model_dump_json()
    user2 = User.model_validate_json(json_str)   # Pydantic v2: classmethod to parse JSON
    print("parsed user2:", user2)

if __name__ == "__main__":
    main() 