#!/usr/bin/env python3
from models import create_session, Audition, Role

if __name__ == "__main__":
    session = create_session()
    audition = session.query(Audition).first()
    role = session.query(Role).first()

    audition.call_back()
    session.commit()

    print(audition)

    role.lead()

    import ipdb; ipdb.set_trace()