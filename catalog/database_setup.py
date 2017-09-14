# 1- Configuration code begining
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# 3- Class code
class MainCategory(Base):
    # 3- Table code
    __tablename__ = 'main_category'

    # 4- Mapper code
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
    
class SubCategory(Base):
    # 3- Table code
    __tablename__ = 'sub_category'

    # 4- Mapper code
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    mainCategory_id = Column(Integer, ForeignKey('main_category.id'))
    category = relationship(MainCategory)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
    
# 2- Configuration code ending
engine = create_engine('sqlite:///foodCatalog.db')
Base.metadata.create_all(engine)