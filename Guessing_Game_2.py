import random

start = input("Welcome to the guessing game 2! Now think of a "
              "\nnumber from 1-100. Write higher if the number is to low."
              "\nWrite lower if the number is to high. And write"
              "\nyes if it is correct. When you got the number write "
              "\n'ready'")


while True:
    value = random.randint(1, 100)
    CPU = input(f"Is your number {value}").capitalize()
    if CPU == "Higher":
       higher = input(f"Is your number {random.randint(value, 100)}").capitalize()
    if CPU == "Lower":
        lower = input(f"Is your number {random.randint(1, value)}").capitalize()
    if higher == "Higher":
        input(f"Is your number {random.randint(value, higher)}").capitalize()
    if lower == "Lower":
        input(f"Is your number {random.randint(lower, value)}").capitalize()
