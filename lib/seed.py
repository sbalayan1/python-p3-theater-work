#!/usr/bin/env python3

from models import create_session, Audition, Role
from faker import Faker
import random

if __name__ == "__main__":
    faker = Faker()
    session = create_session()

    print("Deleting old seed data")
    session.query(Role).delete()
    session.query(Audition).delete()

    print("Seeding database")
    for i in range(0, 50):
        role = Role(character_name=faker.name())

        session.add(role)
        session.commit()

        #actor, location, phone, hired, role_id
        audition = Audition(actor=faker.name(), location=faker.address(), phone=faker.phone_number() , hired=faker.boolean(), role_id=role.id)
        session.add(audition)
        session.commit()
    #creates role
    #creates auditions

    for i in range(0, 100):
        #actor, location, phone, hired, role_id
        audition = Audition(actor=faker.name(), location=faker.address(), phone=faker.phone_number() , hired=faker.boolean(), role_id=random.randint(1,50))

        session.add(audition)
        session.commit()

    session.close()
    print("Done seeding! \n Session closed!")