from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(id, name, price, picture_link, description):
	declarative_base = Product(
		id=id,
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(product_object)
	session.commit()

add_product()

def update_prodacut(id, name, price, picture_link, description):
	declarative_base = session.query(
		base).filter_by(
		id=id).first()
	declarative_base.name = name
	declarative_base.price = price
	declarative_base.picture_link = picture_link
	declarative_base.description = description