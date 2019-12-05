from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
from model import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home():
	return render_template("home.html")
@app.route("/store")
def store():
	return render_template("store.html", products = query_all(fed()))
@app.route("/about")
def about():
	return render_template("about.html")	
@app.route("/cart")
def cart():
	return render_template("cart.html")

#####################
#add_product(1, "Jordan x Off White", '$420.69', 'offwhitejordan.jpg', "This shoes are rare you can buy them once in 420 days. Harry up before somone will buy them before you....", fed())
#add_product(2, "Jordan x Gucci", '$696.9', 'guccijordan.jpg', "Designer shoes made out of snake's poop smells better then it sounds.", fed())
#add_product(3, "Nike Blazer x Sacai", '$222.22', 'sacainikeblazer.jpg', "Cool shoes for teenagers!", fed())
#add_product(4, "Marvel x Vans", '$666', 'deadpoolvans.jpg', "The best shoes for the best paople, only a few can buy those shoes! A.K.A Deadpool", fed())
#add_product(5, "Nike Air x Supreme", '$999', 'nikeairsupreme.jpg', "Those shoes made out of a lot of air and some red dye", fed())
#add_product(6, "Adidas Yeezy x Unicorn", '$333', 'unicornyeezy.jpg', "Hey, I'm not judging", fed())


if __name__ == '__main__':
    app.run(debug=True)