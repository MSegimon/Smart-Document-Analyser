from pydantic import BaseModel
from typing import Optional

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

class SessionCookie(BaseModel):
    session_cookie: str

class FileUpload(BaseModel):
    url: str
    session_cookie: str

class FileDelete(BaseModel):
    id: int
    session_cookie: str

class FileGet(BaseModel):
    id: int
    session_cookie: str

class AnalyseText(BaseModel):
    id: int
    session_cookie: str
