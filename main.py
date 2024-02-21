from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

from userFunctions import create_user, get_user_data_by_name, get_user_data_by_id, delete_user

app = FastAPI()

# Define Pydantic models for data validation
class UserCreate(BaseModel):
    username: str
    password: str
    email: str


# Hello World Call
@app.get("/")
async def hello_world():
    return {"about": "Hello World!"}


# User Calls
@app.post("/user") # Creating a new user
async def create_new_user(user: UserCreate):
    create_user(user.username, user.password, user.email)
    return {"message": "User created successfully."}

@app.get("/user") # Getting user by ID or username
async def get_user(request: Request):
    query_params = request.query_params
    username = query_params.get('username')
    user_id = query_params.get('id')
    
    if username:
        user_data = get_user_data_by_name(username)
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    elif user_id:
        user_data = get_user_data_by_id(user_id)
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    else:
        raise HTTPException(status_code=400, detail="Invalid request.")
    

@app.post("/delete_user") # Deleting a user by ID
async def delete_user_by_id(request: Request):
    query_params = request.query_params
    user_id = query_params.get('id')
    
    if user_id:
        user_data = get_user_data_by_id(user_id)
        if user_data:
            delete_user(user_id)
            return {"message": "User deleted successfully."}
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    else:
        raise HTTPException(status_code=400, detail="Invalid request.")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
