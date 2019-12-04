import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


# We will add classes here
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(250), nullable=False)
    apellidos = Column(String(250), nullable=False)
    dni = Column(Integer, nullable=False)
    cuota = Column(Integer)

    @property
    def serialize(self):
        return {
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'dni': self.dni,
            'id': self.id,
            'cuota': self.cuota
            
        }


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///proyecto.db')
Base.metadata.create_all(engine)
