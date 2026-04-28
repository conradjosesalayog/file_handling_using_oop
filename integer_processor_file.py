class IntegerProcessor:
    def __init__(self):
        self.integer_file = "integers.txt"

    def process(self):
        with open(self.integer_file, "r") as number_file, \
             open("double.txt", "w") as even_square_file, \
             open("triple.txt", "w") as odd_cube_file:



