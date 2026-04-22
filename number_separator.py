class NumberSeparator:
    def __init__(self, numbers_file):
        self.numbers_file = numbers_file

    def separate_odd_even(self):
        even_numbers = []
        odd_numbers = []

        try:
            with open(self.numbers_file, "r") as file:
                numbers = file.read().split()






