class CoffeeMachine():
    # machine's starting stock
    def __init__(self, money, water, milk, beans, dis_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.dis_cups = dis_cups

    # 'remaining' action
    def stock_state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.dis_cups) + " of disposable cups")
        print(str(self.money) + " of money")

    # 'buy' action
    def buy(self):
        # make a coffee function within 'buy'
        def make(drink):
            def not_enough(ingredient):
                print("Sorry, not enough {}!".format(ingredient))
            if self.water < drink.water_req:
                not_enough("water")
            elif self.milk < drink.milk_req:
                not_enough("milk")
            elif self.beans < drink.beans_req:
                not_enough("coffee beans")
            elif self.dis_cups < drink.cups_req:
                not_enough("disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.money += drink.cost
                self.water -= drink.water_req
                self.milk -= drink.milk_req
                self.beans -= drink.beans_req
                self.dis_cups -= drink.cups_req

        # user input menu of 'buy' function
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if order == "1":
            make(espresso)
        elif order == "2":
            make(latte)
        elif order == "3":
            make(cappuccino)
        elif order == "back":
            self.input_req()
        else:
            print("Input not valid")

    # 'fill' action
    def fill(self):
        def how_many(unit, stock_item):
            return int(input("Write how many {} of {} you want to add: ".format(unit, stock_item)))
        self.water += how_many("ml", "water")
        self.milk += how_many("ml", "milk")
        self.beans += how_many("grams", "coffee beans")
        self.dis_cups += how_many("disposable cups", "coffee")

    # 'take' action
    def take(self):
        print("I gave you all the money, totalling ${}".format(self.money))
        self.money = 0

    # user input menu loop
    def input_req(self):
        import sys
        while True:
            user_query = input("Write action (buy, fill, take, remaining, exit): ")
            if user_query == "buy":
                self.buy()
            elif user_query == "fill":
                self.fill()
            elif user_query == "take":
                self.take()
            elif user_query == "remaining":
                self.stock_state()
            elif user_query == "exit":
                sys.exit()
            else:
                print("Input not valid")

class Drink:
    cups_req = 1
    # drink recipe intialiser
    def __init__(self, cost, water_req, milk_req, beans_req):
        self.cost = cost
        self.water_req = water_req
        self.milk_req = milk_req
        self.beans_req = beans_req

# menu of drinks and their ingredients
espresso = Drink(4, 250, 0, 16)
latte = Drink(7, 350, 75, 20)
cappuccino = Drink(6, 200, 100, 12)

machine_1 = CoffeeMachine(550, 400, 540, 120, 9)
machine_1.input_req()









