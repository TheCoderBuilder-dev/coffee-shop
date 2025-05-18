# Coffee Shop Domain Model

Welcome to the Coffee Shop, where caffeine meets code.  
This mini Python system models real-world customer-coffee-order

---

##  What’s the Vibe?

We’ve got 3 main players:
Customer – orders their fave drink
Coffee – the magical beverage types
Order – the actual transaction between the two

Think of it like this:  
Customers pull up, pick their coffee, and the order is logged. You can track who's ordering what, how often, and for how much.

---

##  How They Relate:

- A customer can place many Orders.
- A Coffee can be included in *many Orders.
- An Order links one Customer and one Coffee.
- So it's a many-to-many relationship... all through Orders.


---

##  How to Run This Project

### 1. Clone it:
git clone <the-repo-url>
cd coffee-shop
2. Set up your virtual environment:
pipenv install
pipenv shell
3. Run the debug:
python debug.py
Boom. You’re in. Now start testing those class methods
