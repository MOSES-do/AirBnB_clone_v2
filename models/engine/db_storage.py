#!/usr/bin/python3
"""DBStorage for application"""
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
import os

HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
HBNB_TYPE_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')
HBNB_ENV = os.environ.get('HBNB_ENV')


engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                    HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                    HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True
            )


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = engine
        self.__session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
            )
        self.__session = scoped_session(self.__session_factory)

        self.drop_tables(HBNB_ENV)

    def drop_tables(self, env_test):
        if env_test != 'test':
            return
        try:
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)

            for table_name in metadata.tables.keys():
                table = Table(
                    table_name, metadata, autoload_with=self.__engine
                )
                table.drop(self.__engine)
                print(f"Dropped table: {table_name}")
        except Excetion as e:
            print(f"An error occured while dropping tables: {str(e)}")

    def all(self, cls=None):
        """query current database session (self_session
            for objects with the class_name in cls
            Return a dictionary of objects
        """
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                """returns the object"""
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for obj in query:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj
        else:
            for cls in Base.__subclasses__():
                """query all subclasses of base
                    to return instances of all classes
                     from database in for a list
                """
                query = self.__session.query(cls).all()
                for obj in query:
                    """construct each object into a dictionary"""
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        session = self.__session()
        session.add(obj)
        session.commit()

    def save(self):
        session = self.__session()
        session.commit()

    def delete(self, obj=None):
        if obj:
            session = self.__session()
            session.delete(obj)
            session.commit()

    def close(self):
        """
        call remove() on the private session attr
        """
        self.__session.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session.remove()
