from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    address: str
    mobile: str

app = FastAPI()

created_users = {}
created_bookings = set ()

@app.get ("/")
def database():
    return "Gangadhar"

@app.post("/user/{user_id}")
def created_user(user_id: str, user:User):
    if user_id in created_users:
        raise HTTPException(status_code=400, detail="User already exists")
    created_users[user_id] = user
    return{"message": "created successfully"}


@app.get("/user/{user_id}")
def get_user(user_id:str):
    if user_id in created_users:
        return{"message": "Found user", "user": created_users[user_id]}
    else:
        raise HTTPException(status_code=404, detail="User already exists")

@app.post("/bookings/{new_bookings}")
def create_bookings(new_bookings: str):
    created_bookings.add(new_bookings)
    return{"message": "confirmed"}

@app.get("/bookings/{bookings_id}")
def get_new_bookings(bookings_id: str):
    if bookings_id in created_bookings:
        return{"message": "already booking confirmed"}
    else:
        raise HTTPException(status_code=404, detail="booking not found")

@app.delete("/delete/{delete_bookings}")
def delete_booking(bookings_id: str):
    if bookings_id in created_bookings:
        created_bookings.remove(bookings_id)
        return{"message": "Deleted your bookings Successfully"}
    else:
        raise HTTPException(status_code=404, detail="booking not found")

