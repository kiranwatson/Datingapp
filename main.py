from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    hobbies: List[str]

users = [
    User(id=1, name="Meet", hobbies=["Music", "Chess", "Drawing"]),
    User(id=2, name="Pari Singh", hobbies=["Music", "Cooking", "Reading"]),
    User(id=3, name="Naina Patel", hobbies=["Music", "Chess", "Dance"]),
    User(id=4, name="Amy Bhatt", hobbies=["Cooking"]),
]
from fastapi import FastAPI

app = FastAPI()

@app.get("/match/{user_id}")
def get_potential_matches(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        return {"message": "User not found"}

    matches = []
    for other_user in users:
        if other_user.id != user_id:
            common_hobbies = set(user.hobbies).intersection(other_user.hobbies)
            compatibility_score = len(common_hobbies)
            if compatibility_score > 0:
                matches.append({
                    "id": other_user.id,
                    "name": other_user.name,
                    "hobbies": other_user.hobbies,
            
                })

    matches = sorted(matches, key=lambda x: x["id"], reverse=True)
    return matches
 
