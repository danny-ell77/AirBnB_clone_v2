import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        config = {
            "drivername": "mysql+mysqldb",
            "localhost": os.getenv("HBNB_MYSQL_HOST"),
            "port": 3306,
            "database": os.getenv("HBNB_MYSQL_DB"),
            "username": os.getenv("HBNB_MYSQL_USER"),
            "password": os.getenv("HBNB_MYSQL_PWD"),
        }
        self.__engine = create_engine(URL(**config), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            query = self.__session.query(cls).order_by(cls.id.asc())
        else:
            query = self.__session.query(
                User, State, City, Amenity, Place, Review
            ).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in query}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            obj.delete(synchronize_session=False)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )()
