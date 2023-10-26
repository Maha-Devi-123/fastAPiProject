# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base,db_engine 


Base.metadata.create_all(db_engine)


class CarInfo(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(String)
    modelName = Column(String)
    cc = Column(Integer)
    onRoadPrice = Column(Integer)
    seatingCapacity = Column(Integer)
    gearBox = Column(Integer) 