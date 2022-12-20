water = 400
milk = 540
beans = 120
cups = 9
money = 550


def start():
    menu = "Выберите: \n(buy, fill, take, remaining, exit)\n"
    choice = None

    while choice != "exit":
        choice = input(menu).strip()

        if choice == "buy":
            buy_menu()

        elif choice == "fill":
            fill_menu()

        elif choice == "take":
            take()

        elif choice == "remaining":
            rem()


def buy_menu():
    back = False

    while not back:
        select = "Что вы хотите купить? \n1 - espresso \n2 - latte \n3 - cappuccino \nback - выйти в меню\n"
        choice = input(select).strip()

        if choice == "back":
            back = True

        elif choice.isdigit():
            int_choice =int(choice)

            if 0 < int_choice <= 3:
                get_coffee(int_choice)
                back = True


def get_coffee(choice: int):
    global water, milk, beans, money, cups
    ing_list = get_ing_count(choice)
    drink_names = ["espresso", "latte", "cappuccino"]

    if check_ing(ing_list):
        water -= ing_list[0]
        milk -= ing_list[1]
        beans  -= ing_list[2]
        money += ing_list[3]
        cups -= 1
        print("У меня достаточно ресурсов, чтобы сделать {0}!".format(drink_names[choice-1]))



def check_ing(ing_list: list):
    global water, milk, beans, cups

    if water < ing_list[0]:
        print("Извините, мало воды")
        return False

    elif milk < ing_list[1]:
        print("Извините, мало молока")
        return False

    elif beans  < ing_list[2]:
        print("Извините, не хватает кофейных зерен")
        return False

    elif cups < 1:
        print("Извините, не хватает чашек")
        return False

    return True


def get_ing_count(choice: int):
    list_ing = [0, 0, 0, 0]

    if choice == 1:
        list_ing[0] = 250
        list_ing[2] = 16
        list_ing[3] = 4

    elif choice == 2:
        list_ing[0] = 350
        list_ing[1] = 75
        list_ing[2] = 20
        list_ing[3] = 7

    else:
        list_ing[0] = 200
        list_ing[1] = 100
        list_ing[2] = 12
        list_ing[3] = 6

    return list_ing


def fill_menu():
    global water, milk, beans, cups

    ing = int(input("Напишите, сколько мл. воды вы хотите добавить: "))
    water += ing

    ing = int(input("Напишите, сколько мл. молока вы хотите добавить: "))
    milk += ing

    ing = int(input("Напишите, сколько граммов зерен вы хотите добавить: "))
    beans  += ing

    ing = int(input("Напишите, сколько одноразовых кофейных стаканчиков вы хотите добавить: "))
    cups += ing



def take():
    global money

    print(f"Сдача {money}")
    money = 0
    remaining()
    ...


def remaining():
    global water, milk, beans , cups, money

    print("В кофемашине есть: \n{0} воды \n{1} Молока"
          "\n{2} зерен \n{3} одноразовых стаканчиков \n{4} денег\n"
          .format(water, milk, beans, cups, money))



start()
