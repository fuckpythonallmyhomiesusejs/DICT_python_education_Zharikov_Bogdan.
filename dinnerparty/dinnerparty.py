import random

list_person = {}
list_person_arr = []

def counting():
    print("Сколько людей будет на вечеринке?")
    in_person: int = int(input(": "))

    if in_person <= 1:
        print("Одни бухают только алкаши!")
        return

    print("Введите имя друзей которые будут на вечеринке с новой строчки")

    for i in range(in_person):
        input_person = input(": ")
        list_person.update({f"{input_person}" : 0})

    input_amount = int(input("Какая вышла сумма чека?" "\n: "))

    lucky_person = input("Будет счастливчик в вашей ПаТи?)))) y/n" "\n: ")
    choice_lucky = random.choice([key for key in list_person.keys()])

    if lucky_person.lower() == "y":
        in_person -= 1
        print(f"{choice_lucky} Счастливчик")
    else:
        print("Не хотите испытать уДаЧу!? ну ладно." "\n")

    amount_person = round((input_amount / in_person), 2)
    for key in list_person.keys():
        if key == choice_lucky and lucky_person.lower() == 'y':
            list_person[key] = 'Победитель по жизни'
        else:
            list_person[key] = amount_person

    print(list_person)


counting()
