from fastapi import FastAPI, Depends, HTTPException
from db import engine, sessionLocal
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Users, Category, Orders, Shablones
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

app = FastAPI(
	title='My API',
	description='My new API',
	version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/users')
def show_all_users(session: Session = Depends(get_db)):
   r = session.query(Users).all()
   return [
		{
			'id': i.id,
			'tg_id': i.tg_id,
			'username': i.username,
			'is_admin': i.is_admin
		}
		for i in r
	]



from typing import Optional

@app.post("/users")
def create_user(
    tg_id: Optional[int] = None,
    username: str = None,
    session: Session = Depends(get_db)
):
    user = Users(
        tg_id=tg_id,
        username=username,
    )
    session.add(user)
    session.commit()
    session.refresh(user)  # чтобы вернуть обновлённый объект с id
    return user

@app.put('/users')
def do_admin_user(user_id: int, session: Session = Depends(get_db)):
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_admin = True
    session.commit()
    session.refresh(user)
    return user