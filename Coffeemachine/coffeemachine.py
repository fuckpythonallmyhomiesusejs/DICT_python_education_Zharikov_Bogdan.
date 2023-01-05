class CoffeeMachine:
    running = False

    def __init__(self, water, milk, coffee_beans, cups, money):
        """resources in coffee machine"""
        self.water = water
        self.milk = milk
        self.beans = coffee_beans
        self.cups = cups
        self.money = money

        if not CoffeeMachine.running:
            """ if the machine isn't running then start running"""
            self.buy_menu()

    def buy_menu(self):
        """not to run start() in a method use self.running & action selection"""
        self.running = True
        self.action = input("\n(buy, fill, take, remaining, exit)\nВыберите: ")
        print()
        action_choices = {"buy": self.buy, "fill": self.fill_menu, "take": self.take, "exit": exit, "remaining": self.remaining}
        if self.action in action_choices:
            action_choices[self.action]()
        else:
            exit()

    def return_to_menu(self):
        """returns to the menu after an action"""
        print()
        self.buy_menu()

    def available_check(self):
        """checks if he can afford to prepare such coffee at the moment & checks if the resources goes down to 0"""
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.beans - self.reduced[2] < 0:
            self.not_available = "beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "cups"

        if self.not_available != "":
            print(f"Извините, не хватает {self.not_available}!")
            return False
        else:
            print("У меня достаточно ресурсов, чтобы сделать кофе!")
            return True

    def get_ing_count(self):
        """performs an operation"""
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.beans -= self.reduced[2]
        self.cups -= self.reduced[3]
        self.money += self.reduced[4]

    def buy(self):
        """menu & checking for consumables """
        self.choice = input("Что вы хотите купить? \n1 - espresso \n2 - latte \n3 - cappuccino \nback - выйти в меню\n")
        if self.choice == '1':
            self.reduced = [250, 0, 16, 1, 4]
            if self.available_check():
                self.get_ing_count()

        elif self.choice == '2':
            self.reduced = [350, 75, 20, 1, 7]
            if self.available_check():
                self.get_ing_count()

        elif self.choice == "3":
            self.reduced = [200, 100, 12, 1, 6]
            if self.available_check():
                self.get_ing_count()

        elif self.choice == "back":
            self.return_to_menu()

        self.return_to_menu()

    def fill_menu(self):
        """adding consumables"""
        self.water += int(input("Напишите, сколько мл. воды вы хотите добавить:\n"))
        self.milk += int(input("Напишите, сколько мл. молока вы хотите добавить::\n"))
        self.beans += int(input("Напишите, сколько граммов зерен вы хотите добавить\n"))
        self.cups += int(input("Напишите, сколько одноразовых кофейных стаканчиков вы хотите добавить:\n"))
        self.return_to_menu()

    def take(self):
        """cash withdrawal"""
        print(f"I gave you ${self.money}")
        self.money -= self.money
        self.return_to_menu()

    def remaining(self):
        """displaying the amount of consumables"""
        print(f"В кофемашине есть:")
        print(f"{self.water} воды")
        print(f"{self.milk} молока")
        print(f"{self.beans} зерен")
        print(f"{self.cups} одноразовых стаканчиков")
        print(f"${self.money} денег")
        self.return_to_menu()


CoffeeMachine(400, 540, 120, 9, 550)
"""launch based on resources in parentheses"""