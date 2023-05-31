# Dating App 
This is a backend service for a dating app that helps users find potential matches based on hobbies. The service is built using Python and the FastAPI framework.
# Prerequisites
Python 3.7 or above
FastAPI
Pydantic
uvicorn server 
redis server 
# Installation
Clone the repository:
git clone https://github.com/kiranwatson/Datingapp.git
# Install the dependencies:
pip install -r requirements.txt
# Usage
1 Start the FastAPI server:
uvicorn main:app --reload
2 API Endpoint
GET /match/{user_id}: Returns potential matches for a given user ID.
Example Request:
GET http://localhost:8000/match/1
Example Response:
[
  {
    "id": 2,
    "name": "Pari Singh",
    "hobbies": ["Music", "Cooking", "Reading"]
  },
  {
    "id": 3,
    "name": "Naina Patel",
    "hobbies": ["Music", "Chess", "Dance"]
  }
]
# Data Model
The service uses the following data model:
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    hobbies: List[str]
# How it Works
The service stores user data in a list of User objects.
When a GET request is made to /match/{user_id}, the service retrieves the user with the specified ID.
The service compares the hobbies of the given user with the hobbies of all other users.
It calculates a compatibility score based on the number of common hobbies.
The service filters out users with no common hobbies and returns the potential matches in descending order of their IDs.
