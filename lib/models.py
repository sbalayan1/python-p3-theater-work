#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship, sessionmaker, backref

# engine = create_engine("sqlite:///theater.db")
Base = declarative_base()

def create_session():
    engine = create_engine('sqlite:///theater.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean()) 
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return (f"\nAudition: \nactor: {self.actor}: \nlocation: {self.location} \nphone: {self.phone} \nhired: {self.hired}")

    def call_back(self):
        session = create_session()
        session.query(Audition).filter(Audition.id == self.id).update({Audition.hired: True})
        session.commit()
        session.close()
        return self
    

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())
    auditions = relationship('Audition', backref='role', order_by="Audition.id", collection_class=ordering_list('id'))

    def __repr__(self):
        return (f"Role: \n character_name: {self.character_name} \n auditions: {[[*self.auditions]]}")

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def top_5_auditions(self):
        output = []
        for a in self.auditions:
            if (a.hired == True): output.append(a)

        return output

    def lead(self):
        topAud = self.top_5_auditions()
        if not topAud: return "no actor has been hired for this role"
        return topAud[0]

    def understudy(self):
        topAuds = self.top_5_auditions()
        if not topAuds or len(topAuds) <= 1: return "no actor has been hired for understudy for this role"
        return topAuds[1]
