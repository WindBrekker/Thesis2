import os
import time

def draw_tree(levels):
    for i in range(1, levels + 1):
        spaces = " " * (levels - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    time.sleep(0.5)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def blinking_tree(levels, iterations):
    for _ in range(iterations):
        draw_tree(levels)
        clear_screen()

if __name__ == "__main__":
    try:
        levels = int(input("Podaj ilość poziomów choinki: "))
        iterations = int(input("Podaj ilość migotania: "))
        blinking_tree(levels, iterations)
    except ValueError:
        print("Podano nieprawidłowe dane. Wprowadź liczbę całkowitą.")
