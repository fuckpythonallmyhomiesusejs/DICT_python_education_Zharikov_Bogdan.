import random

words = ("dict", "python", "java", "godamn")
word = random.choice(words)
turns = 8
guesses = ''
uselatter = []
def menu():
    while True:
        choice = input("1. Играть" "\n2. Выйти" "\n" )
        if choice == '1':
            print("Добро пожаловать!\n")
            game(turns,guesses)
        if choice == '2':
            print("Довстречи!")
            return

def game(turns, guesses):
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                print(end="")
                failed += 1
        if failed == 0:
            print("Ты победил!")
            print("Угаданное слово: ", word)
            break
        print()
        guess = input("Ввод:")
        guesses += guess
        if guess.upper():
            print("Вводите буквы с маленького регистра!")
        if len(guess) > 1:
            print("Много символов введите 1 букву!")
        elif guess in uselatter:
            print("Такая буква уже была!")
        else:
            uselatter.append(guess)
        if guess not in word:
            turns -= 1
            print("Неправильно")
            print("У тебя осталось", + turns, 'попыток!')
            if turns == 0:
                print("Ты проиграл!")

menu()
