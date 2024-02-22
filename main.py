from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

from userFunctions import create_user, get_user_data_by_name, get_user_data_by_id, delete_user
from loginFunctions import login, is_session_cookie_valid

app = FastAPI()

# Define Pydantic models for data validation
class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class GetUser(BaseModel):
    username: Optional[str] = None
    id: Optional[int] = None

class DeleteUser(BaseModel):
    id: int

class Login(BaseModel):
    username: str
    password: str


# Hello World Call
@app.get("/")
async def hello_world():
    return {"about": "Hello World!"}


# User Calls
@app.post("/create_user") # Creating a new user
async def create_new_user(user: UserCreate):
    create_user(user.username, user.password, user.email)
    return {"message": "User created successfully."}

@app.get("/user") # Getting user by ID or username
async def get_user(get_user: GetUser):
    if get_user.username:
        user_data = get_user_data_by_name(get_user.username)
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    elif get_user.id:
        user_data = get_user_data_by_id(get_user.id)
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    else:
        raise HTTPException(status_code=400, detail="Invalid request.")
    
    
@app.post("/delete_user") # Deleting a user by ID
async def delete_user(delete_user: DeleteUser):
    user_id = delete_user.id
    
    if user_id:
        user_data = get_user_data_by_id(user_id)
        if user_data:
            delete_user(user_id)
            return {"message": "User deleted successfully."}
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    else:
        raise HTTPException(status_code=400, detail="Invalid request.")


# Login Calls
@app.post("/login") # Login function
async def user_login(login_data: Login):
    session_cookie, timestamp = login(login_data.username, login_data.password)
    if session_cookie:
        return {"session_cookie": session_cookie, "timestamp": timestamp}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials.")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
