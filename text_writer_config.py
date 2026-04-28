class TextWriter:
    def write_lines(self):
        lines = open("mylife.txt", "w")

        while True:
            my_life = input("Enter your line:")
            lines.write(my_life + "\n")

            response = int(input("Are there more lines? y/n"))

            if response.lower() == "n":
                break
        lines.close()
        print("Saved to a file! Check mylife.txt")