from number_separator import NumberSeparator

def main():
    separator = NumberSeparator("numbers.txt")
    separator.separate_odd_even()
if __name__ == "__main__":
    main()