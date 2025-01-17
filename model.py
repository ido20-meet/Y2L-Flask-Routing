from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product(Base):
	__tablename__ = 'products'
	Id = Column(Integer, primary_key=True)
	name = Column(String)
	price = Column(String)
	picture_link = Column(String)
	description = Column(String)

class Cart(object):
	__tablename__ = 'Product'
	Id= Column(String, primary_key=True)
	product_id= Column(Integer)