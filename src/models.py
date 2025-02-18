import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    
    user_from_id = Column(Integer, nullable=False, primary_key=True)
    user_to_id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    
    
class Post(Base):
    __tablename__='post'

    id = Column(Integer, primary_key=True)
    user_id = (Integer, ForeignKey('user.id'))
    User = relationship(User)

class Media(Base):
    __tablename__='media'

    id= Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')