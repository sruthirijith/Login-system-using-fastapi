import db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
import schema
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

app = FastAPI(title="user registration")


@app.get('/get_user_profile')
def  get_user(id:str):
    #  receive_user = db.query(models.user_register,models.user_profile).filter(models.user_register.id==id,models.user_profile.id==id).first()
     receive_user = db.query(models.user_profile).filter(models.user_profile.owner_id==id).first()
     return receive_user

@app.get('/get_user_register')
def  get_user(id:str):
   
     receive_user = db.query(models.user_register).filter(models.user_register.id==id).first()
     return receive_user

@app.post('/user_register')
def user_register(data:schema.Base):
    receive_data = db.query(models.user_register).filter(models.user_register.mobile_no==data.mobile_no).first()
    

    if receive_data:

        return {'phone number already in db'}
    
    receive_data1 = db.query(models.user_register).filter(models.user_register.email==data.email).first()
    if receive_data1:
        return {' email already in db'}


        
    try:
        user_details = models.user_register(**data.dict())
        db.add( user_details)
        db.commit()
        receive_data2 = db.query(models.user_register.id).filter(models.user_register.mobile_no==data.mobile_no).first()
         
        
    except:
         return{'db error'}
    return data,receive_data2


@app.post('/user_profile')
def user_profile(data1:schema.Profile, id:str):
    profile_details= models.user_profile(**data1.dict(),owner_id=id)
    db.add(profile_details)
    db.commit()
    return data1


@app.put("/update user_register")
def update(id:str,name:str,email:str,mobile_no:str):
    data = db.query(models.user_register).filter(models.user_register.id==id).first()
    if not data:
        return 404
    data.name      = name
    data.email     = email
    data.mobile_no = mobile_no
    try:
        db.add(data)
        db.commit()
        db.refresh()
    except:
        pass
    return 200

@app.put("/update user_profile")
def update(owner_id:str,sex:str,dob:str):
    data1 = db.query(models.user_profile).filter(models.user_profile.owner_id==owner_id).first()
    if not data1:
        return 404
    data1.sex      = sex
    data1.dob     = dob
    
    try:
        db.add(data1)
        db.commit()
        db.refresh()
    except:
        pass
    return 200

@app.delete('/delete_user_register')
def delete(id:str):
    delete_data=db.query(models.user_register).filter(models.user_register.id==id).first()
    db.delete(delete_data)
    db.commit()
    return delete_data
    

@app.delete('/delete_user_profile')
def delete(owner_id:str):
    delete_data1=db.query(models.user_profile).filter(models.user_profile.id==owner_id).first()
    db.delete(delete_data1)
    db.commit()
    return delete_data1