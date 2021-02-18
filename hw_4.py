import unittest

## Name : Jake Domagalski
## Student ID: 2465 7437
## Your Email: jdomagal@umich.edu
## People you worked with : Ambra 
## Github URL :

### Customer Class
class Customer:

	# Constructor
	def __init__(self, name, wallet = 100):
		self.name = name
		self.wallet = wallet

    # Withdraws fast_cash from the atm into the customer's wallet.
	def withdraw_money(self, fast_cash):
		self.wallet += fast_cash


	# Pays the server
	def make_order(self, server, amount):
		self.wallet -= amount
		server.money += amount
		pass

	# Orders food from the truck to be brought to the table by the server,
	# assuming certain conditions are met.
	def order_food(self, server, truck, food_name, quantity):
		if not(server.serve_truck(truck)):
			print("Sorry, I don't serve that food truck. Please try a different one.")
		elif self.wallet < server.estimated_cost(truck, quantity):
			print("Don't have enough money for that :( Please withdraw more money!")
		elif not(truck.has_food(food_name, quantity)):
			print("Our food truck has run out of " + food_name + " :( Please try a different truck!")
		else:
			bill = server.place_order(truck, food_name, quantity)
			self.make_order(server, bill)
			self.eat_food()

	# Eats the ordered food and prints out message indicating this .
	def eat_food(self):
		print("Wow that was really tasty")

	def __str__(self):
		return "Hello! My name is " + self.name + ". I have $" + str(self.wallet) + " and I want to order some food."

### Food Truck Server Class
class Server:

	# Constructor
	def __init__(self, name, money = 200, food_trucks = [], service_fee = 5):
		self.name = name
		self.money = money
		self.food_trucks = food_trucks[:] # makes a copy of the list
		self.service_fee = service_fee

	# Adds a food truck to the known list of trucks at the festival.
	def add_truck(self, new_truck):
		self.food_trucks.append(new_truck)

	# Receives payment from customer, and adds the money to the server's fanny pack.
	def receive_payment(self, money):
		self.money += money


	# Returns the estimated cost of an order, namely the cost of the foods ( quantity times cost)
	# plus the server's own service fee.
	def estimated_cost(self, truck, quantity):
		return ((truck.cost * quantity) + self.service_fee)


	# Places an order at the food truck.
	# The server pays the food truck the cost.
	# The food truck processes the order
	# Function returns cost of the food + service fee.
	def place_order(self, truck, food_item, quantity):
		self.money = self.money - (truck.cost * quantity)
		truck.process_order(food_item, quantity)
		return self.estimated_cost(truck, quantity)

	# Returns boolean value letting customer know if this server can order from that food truck or not.
	def serve_truck(self, truck):
		return truck in self.food_trucks


	# string function.
	def __str__(self):
		return "Hello, my name is " + self.name + " I will be your server today, I have this much $" + str(self.money) + "in change. We take cash only. I charge $" + str(self.service_fee) + " and I can order from " + str(len(self.food_trucks)) + " food trucks."

### Create Truck class here

class Truck:

	def __init__(self, name, inventory, cost = 7, money = 700):
		self.name = name
		self.inventory = inventory
		self.cost = cost
		self.money = money 


	def process_order(self, food_item, quantity):
		if food_item in self.inventory:
			self.inventory[food_item] -= quantity
			self.money += (self.cost * quantity)


	def has_food(self, food_name, quantity):
		if food_name in self.inventory:
			if self.inventory[food_name] >= quantity:
				return True

	
	def stock_up(self, food_name, quantity):
		if food_name in self.inventory:
			self.inventory[food_name] += quantity
		else:
			self.inventory[food_name] = quantity

	
	def __str__(self):
		return "Hello, we are " + self.name + "." + "This is the current menu" + self.inventory.keys() + ". We charge " + str(self.cost) + " per item. We have " + str(self.money) + " in total."




class TestAllMethods(unittest.TestCase):

	def setUp(self):
		inventory = {"Burger":40, "Taco":50}
		self.f1 = Customer("Ted")
		self.f2 = Customer("Morgan", 150)
		self.t1 = Truck("The Grill Queen", inventory, cost = 10)
		self.t2 = Truck("Tamale Train", inventory, cost = 9)
		self.t3 = Truck("The Streatery", inventory)
		self.s1 = Server("Greg")
		self.s2 = Server("Tina", service_fee = 8, food_trucks = [self.t1, self.t2])

	## Check to see whether constructors work
	def test_customer_constructor(self):
		self.assertEqual(self.f1.name, "Ted")
		self.assertEqual(self.f2.name, "Morgan")
		self.assertEqual(self.f1.wallet, 100)
		self.assertEqual(self.f2.wallet, 150)

	## Check to see whether constructors work
	def test_server_constructor(self):
		self.assertEqual(self.s1.name, "Greg")
		self.assertEqual(self.s1.service_fee, 5)
		self.assertEqual(self.s2.service_fee, 8)
		self.assertEqual(self.s1.food_trucks, [])
		self.assertEqual(len(self.s2.food_trucks), 2)

	## Check to see whether constructors work
	def test_truck_constructor(self):
		self.assertEqual(self.t1.name, "The Grill Queen")
		self.assertEqual(self.t1.inventory, {"Burger":40, "Taco":50})
		self.assertEqual(self.t1.money, 700)
		self.assertEqual(self.t2.cost, 9)

	# Check that the food truck can stock up properly.
	def test_stocking_medicine(self):
		inventory = {"Burger":10}
		t4 = Truck("Misc Truck", inventory)

		# Testing whether food truck can stock up on items
		self.assertEqual(t4.inventory,{"Burger":10} )
		t4.stock_up("Burger", 30)
		self.assertEqual(t4.inventory, {"Burger": 40})

	def test_make_payment(self):
		# Check to see how much money there is prior to a payment
		previous_wallet_customer = self.f2.wallet
		previous_money_server = self.s2.money

		# Make the payment
		self.f2.make_order(self.s2, 30)

		# See if money has changed hands
		self.assertEqual(self.f2.wallet, previous_wallet_customer - 30)
		self.assertEqual(self.s2.money, previous_money_server + 30)


	# Check to see that the server can serve from the different trucks
	def test_adding_and_serving_truck(self):
		s3 = Server("Felix", service_fee = 7, food_trucks = [self.t1, self.t2])
		self.assertTrue(s3.serve_truck(self.t1))
		self.assertFalse(s3.serve_truck(self.t3))
		s3.add_truck(self.t3)
		self.assertTrue(s3.serve_truck(self.t3))
		self.assertEqual(len(s3.food_trucks), 3)


	# Test that estimated cost works properly.
	def test_estimated_cost(self):
		self.assertEqual(self.s1.estimated_cost(self.t1, 5), 45)
		self.assertEqual(self.s2.estimated_cost(self.t2, 6), 61)

	# Check that the food truck can properly see when it is empty
	def test_has_food(self):

		# Test to see if has_food returns True when a food truck has food left


		# Test to see if has_food returns True when a food truck has
		# just a little bit of food left (i.e., food_left == 1)


		# Test to see if has_food returns False when a food truck has no food left
		pass

	# Test order food
	def test_order_food(self):
		# test if a customer doesn't have enough money in their wallet to order

		# test if the food truck doesn't have any food left in stock

		# check if the server can order food from that truck
		pass


	#Write Test Case
    #test if a customer can add money to their wallet
	def test_withdraw_money(self):
		pass




def main():
	inventory_1 = {'Burgers': 15, "Fries" : 20, "Soda" : 25}
	inventory_2 = {'Turkey Sandwich' : 20, "Ham Sandwich" : 20, "Chips" : 30}

	customer1 = Customer('Johnny', 500)
	customer2 = Customer('Bob', 250)

	truck1 = Truck('Burgers', inventory_1, cost = 5, money = 1000)
	truck2 = Truck('Sandwiches', inventory_2, cost = 6, money = 750)

	server1 = Server('Anna', 100, [inventory_1], 2)
	server2 = Server('Kirsten', 250, [inventory_1, inventory_2], 6)

	customer1.order_food(server1, truck1, 'Burgers', 2)
	customer2.order_food(server2, truck2, 'soda', 1)
	pass


if __name__ == "__main__":
	main()
	print("\n")
	unittest.main(verbosity = 2)