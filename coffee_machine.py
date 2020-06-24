class CoffeeMachine:
    READY_COFFEE = "I have enough resources, making you a coffee!"
    WATER_ERROR = "Sorry, not enough water!"
    MILK_ERROR = "Sorry, not enough milk!"
    BEAN_ERROR = "Sorry, not enough Coffee beans!"
    CUPS_ERROR = "Sorry, not enough disposable cups!"
 
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
 
    def remaining(self):
        print('The coffee machine has: ')
        print(self.water, 'of water')
        print(self.milk , 'of milk')
        print(self.coffee_beans, 'of coffee beans')
        print(self.disposable_cups, 'of disposable cups')
        print(self.money, ' of money')
 
    def buy(self,option):
        if option == '1':
            print()
            if self.water < 250:
                print(CoffeeMachine.WATER_ERROR)
            elif self.coffee_beans < 16:\
                print(CoffeeMachine.BEAN_ERROR)
            elif self.disposable_cups < 1:\
                print(CoffeeMachine.CUPS_ERROR)
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
        elif option == '2':
            print()
            if self.water < 350:
                print(CoffeeMachine.WATER_ERROR)
            elif self.milk < 75:
                print(CoffeeMachine.MILK_ERROR)
            elif self.coffee_beans < 20:
                print(CoffeeMachine.BEAN_ERROR)
            elif self.disposable_cups < 1:
                print(CoffeeMachine.CUPS_ERROR)
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
        elif option == '3':
            print()
            if self.water < 350:
                print(CoffeeMachine.WATER_ERROR)
            elif self.milk < 75:
                print(CoffeeMachine.MILK_ERROR)
            elif self.coffee_beans < 20:
                print(CoffeeMachine.BEAN_ERROR)
            elif self.disposable_cups < 1:
                print(CoffeeMachine.CUPS_ERROR)
            else:
                print(CoffeeMachine.READY_COFFEE)
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
 
    def fill(self, add_water_quantity, add_milk_quantity, add_coffee_beans_quantity, add_cups_quantity):
        self.water += add_water_quantity
        self.milk += add_milk_quantity
        self.coffee_beans += add_coffee_beans_quantity
        self.disposable_cups += add_cups_quantity
 
    def take_money(self):
        print('I gave you', '$' + str(self.money),'\n')
        self.money -= self.money
 
 
coffee = CoffeeMachine(400, 540, 120, 9, 550)
 
 
def action(user_action):
    if user_action == "buy":
        buy_option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:')
        if buy_option != 'back':
            coffee.buy(buy_option)
    elif user_action == "fill":
        add_water = abs(int(input('Write how many ml of water do you want to add:')))
        add_milk = abs(int(input('Write how many ml of milk do you want to add:')))
        add_beans = abs(int(input('Write how many grams of coffee beans do you want to add:')))
        add_cups = abs(int(input('Write how many disposable cups of coffee do you want to add:')))
        coffee.fill(add_water, add_milk, add_beans, add_cups)
    elif user_action == "take":
        coffee.take_money()
    elif user_action == "remaining":
        coffee.remaining()
 
 
while True:
    user_action = input('Write action (buy, fill, take, remaining, exit):')
    if user_action != 'exit':
        action(user_action)
    else:
        break
