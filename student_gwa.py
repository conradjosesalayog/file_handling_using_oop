class StudentGwa:
    '''Initial class for students and their GWAs'''
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = gwa

class StudentConfig:
    '''Main class for the configuration of the students and their GWAs'''
    def __init__(self):
        self.file_name = "students.txt"
        self.students = []

    def read_students(self):
        with open(self.file_name, "r") as file:
            for line in file:
                name, gwa = line.split(",")
