from db import Base
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column, BigInteger, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Users(Base):
   __tablename__ = 'users'
   
   id = Column(Integer, primary_key=True)
   tg_id = Column(BigInteger)
   is_admin = Column(Boolean, default=False)
   username = Column(String)
   
   orders = relationship('Orders', back_populates='user')



class Category(Base):
   __tablename__ = 'categories'
   
   id = Column(Integer, primary_key=True)
   title = Column(String)
   
   shablones = relationship('Shablones', back_populates='category')


class Shablones(Base):
   __tablename__ = 'shablones'
   
   id = Column(Integer, primary_key=True)
   category_id = Column(Integer, ForeignKey('categories.id'))
   title = Column(String)
   description = Column(Text)
   img_url = Column(Text)
   
   orders = relationship('Orders', back_populates='shablone')
   category = relationship('Category', back_populates='shablones')


class Orders(Base):
   __tablename__ = 'orders'
   
   id = Column(Integer, primary_key=True)
   shablone_id = Column(Integer, ForeignKey('shablones.id'))
   user_id = Column(Integer, ForeignKey('users.id'))
   create_at = Column(DateTime, default=datetime.utcnow)
   source = Column(String)  
	# site / telegram
   status = Column(String, default="new")
	# new / paid / done / canceled

   
   user = relationship('Users', back_populates='orders')
   shablone = relationship('Shablones', back_populates='orders')




