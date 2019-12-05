from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
'''

def fed():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_product(Id, name, price, picture_link, description, session):
	declarative_base = Product(
		Id=Id,
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(declarative_base)
	session.commit()

"""
add_product(1, "Jordan x Off White", '$420.69', 'offwhitejordan.jpg', "This shoes are rare you can buy them once in 420 days. Harry up before somone will buy them before you....", fed())
add_product(2, "Jordan x Gucci", '$696.9', 'guccijordan.jpg', "Designer shoes made out of snake's poop smells better then it sounds.", fed())
add_product(3, "Nike Blazer x Sacai", '$222.22', 'sacainikeblazer.jpg', "Cool shoes for teenagers!", fed())
add_product(4, "Marvel x Vans", '$666', 'deadpoolvans.jpg', "The best shoes for the best paople, only a few can buy those shoes! A.K.A Deadpool", fed())
add_product(5, "Nike Air x Supreme", '$999', 'nikeairsupreme.jpg', "Those shoes made out of a lot of air and some red dye", fed())
add_product(6, "Adidas Yeezy x Unicorn", '$333', 'unicornyeezy.jpg', "Hey, I'm not judging", fed())
"""


def update_product(Id, name, price, picture_link, description, session):
	declarative_base = session.query(
		base).filter_by(
		Id=Id).first()
	declarative_base.name = name
	declarative_base.price = price
	declarative_base.picture_link = picture_link
	declarative_base.description = description

def query_all(session):
   products = session.query(
      Product).all()
   return products

def add_to_cart(Id, name, price, picture_link, description, session):
	declarative_base = Product(
		Id=Id,
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(declarative_base)
	session.commit()

print(query_all(fed()))

