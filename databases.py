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
	session.close()

def add_product(name, price, picture_link, description, session):
	declarative_base = Product(
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(declarative_base)
	session.commit()
	session.close()


# add_product( "Jordan x Off White", '$420.69', 'offwhitejordan.jpg', "This shoes are rare you can buy them once in 420 days. Harry up before somone will buy them before you....", fed())
# add_product( "Jordan x Gucci", '$696.9', 'guccijordan.jpg', "Designer shoes made out of snake's poop smells better then it sounds.", fed())
# add_product( "Nike Blazer x Sacai", '$222.22', 'sacainikeblazer.jpg', "Cool shoes for teenagers!", fed())
# add_product( "Marvel x Vans", '$666', 'deadpoolvans.jpg', "The best shoes for the best paople, only a few can buy those shoes! A.K.A Deadpool", fed())
# add_product( "Nike Air x Supreme", '$999', 'nikeairsupreme.jpg', "Those shoes made out of a lot of air and some red dye", fed())
# add_product( "Adidas Yeezy x Unicorn", '$333', 'unicornyeezy.jpg', "Hey, I'm not judging", fed())
# add_product( "Jordan Not For Resale", '$150','Jordan_Notforresale.png', "It's good", fed())
# add_product( "Jordan X Travis Scott", '$365', 'JordanTravis.jpg', "The rapper Travis Scott is a legend also in the fashion culture", fed())
# add_product( "Nike SB X Off White",'$1000', 'nikesboffwhite.jpg', "It does look good and smells good", fed())
# add_product( "Red October Yeezy", '$1500', 'redoctober.jpg', "Old school shoes for the best ones", fed())

def update_product(Id, name, price, picture_link, description, session):
	declarative_base = session.query(
		base).filter_by(
		Id=Id).first()
	declarative_base.name = name
	declarative_base.price = price
	declarative_base.picture_link = picture_link
	declarative_base.description = description
	session.close()

def query_all(session):
	products = session.query(
		Product).all()
	return products
	session.close()

def add_to_cart(session,id):
	declarative_base = Cart(
		product_id=id)
	session.add(declarative_base)
	session.commit()
	session.close()

print(len(query_all(fed())))

