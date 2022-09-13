from typing import Optional
from pydantic import BaseModel



class Base(BaseModel):
    name         : str
    email        : str
    mobile_no    : str
    

class Profile(BaseModel):
    
    sex  : str
    dob  : str