class NumberSeparator:
    def __init__(self, numbers_file):
        self.numbers_file = numbers_file

    def separate_odd_even(self):
        even_numbers = []
        odd_numbers = []

        try:
            with open(self.numbers_file, "r") as file:
                numbers = file.read().split()

            for number in numbers:
                number = int(number)
                if number % 2 == 0:
                   even_numbers.append(number)
                else:
                   odd_numbers.append(number)
        except:
            print("Error")

        with open("/.even_numbers.txt", "w") as even_numbers_file:
            for number in even_numbers:
                even_numbers_file.write(str(number))

