import itertools
from random import randint


def kill(player_choice: str, choice_other_player: str, arr: list) -> bool:
    # Reversing the array for better performance when slicing.
    arr = arr[::-1]
    double_arr = arr + arr
    # Calculating half of the array for performance.
    half_len_arr = int((len(arr) / 2)) - 1
    i = 0
    for killer, victim in itertools.combinations(double_arr, 2):
        if killer == player_choice and i <= half_len_arr:
            i += 1
            if victim == choice_other_player:
                return True
    return False


def check_commands(selected_user: str, count_player: int) -> bool:
    if selected_user == "!exit":
        print("Bye!")
        exit(0)
    elif selected_user == "!rating":
        print(f"Your rating: {count_player}")
        return True
    return False


def check_input_user(selected_user: str, items_array: list) -> bool:
    if selected_user in items_array:
        return True
    return False


def read_file(key: str) -> int:
    try:
        with open("rating.txt") as f:
            for line in f:
                name, score = line.split()
                if name == key:
                    return int(score)
    except (FileNotFoundError, ValueError):
        print("Rating file not found or is corrupt. Starting with default rating of 0.")
        return 0


def game(user: str, items_array: list) -> None:
    count_player = read_file(user)
    while True:
        selected_user = input(">")
        if check_commands(selected_user, count_player):
            continue
        if not check_input_user(selected_user, items_array):
            print("Invalid input")
            continue

        computer_choice = items_array[randint(0, len(items_array) - 1)]
        if kill(computer_choice, selected_user, items_array):
            print(f"Sorry, but the computer chose <{computer_choice}>")
        elif kill(selected_user, computer_choice, items_array):
            print(f"Well done. The computer chose <{computer_choice}> and failed")
            count_player += 100
        else:
            print(f"There is a draw ({computer_choice})")
            count_player += 50


def main():
    user = input('Enter your name: ')
    print(f"Hello, {user}")
    role = input("Enter your values separated by commas: ").split(",") or ["paper", "scissors", "rock"]
    count_victim = int((len(role) / 2))
    print(*role, sep=f' {"<"*count_victim} ')
    print("Okay, let's start.")
    game(user, role)


if __name__ == '__main__':
    main()
