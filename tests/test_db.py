from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='stefani', email='stef1@ani.com', password='senha')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'stef1@ani.com'))

    assert result.username == 'stefani'
