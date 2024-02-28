import datetime as dt
import sqlalchemy as sa
import sqlalchemy.orm as orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    created_data = sa.Column(sa.DateTime, default=dt.datetime.now)
    news = orm.relationship("News", back_populates='user')