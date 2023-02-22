#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
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
        return (f"Audition: \n actor: {self.actor}: \n location: {self.location} \n phone: {self.phone} \n hired: {self.hired}")

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
    auditions = relationship('Audition', backref='role')

    def __repr__(self):
        return (f"Role: \n character_name: {self.character_name} \n auditions: {[[*self.auditions]]}")

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def actors(self):
        return [audition.location for audition in self.auditions]

    # def sort_auditions(self):
    #     session = create_session()
    #     session.query()

    def lead(self):
        if not self.auditions: return "no actor has been hired for this role"
        audIdx = 0

        for idx, a in enumerate(self.auditions):
            newestActor = self.auditions[audIdx].id
            auditionIdx = idx if a.id < newestActor else audIdx

        return self.auditions[audIdx]

    def understudy(self):
        pass
        print(self.auditions.sort(key=id))
