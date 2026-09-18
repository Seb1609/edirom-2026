# Write a program that prints the words "Hello Edirom" to the console.
# Run it with `python exercises/ex1.py` in the terminal, or with the "|>" button in the top-right.
# Your solution must contain at least one function.

def hello(name: str):
    if name == "Mike":
        print("Oh no, not Mike again!")
    elif name == "Santa Claus":
        print("Wow, it is Santa Claus!")
    else:
        print(f"Hello {name}")

if __name__ == "__main__":
    # Hint: Once you have defined a function, remove the pass statement and call the function here.
    hello("Sebastian")