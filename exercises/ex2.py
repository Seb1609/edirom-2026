# Write a function that prints your name 10 times.
# Your solution must contain only one print() statement
# Run it with `python exercises/ex2.py` in the terminal.

def my_name(name: str, times: int):
    for _ in range(times):
        print(name)

my_name("Sebastian", 5)


if __name__ == "__main__":
    pass
