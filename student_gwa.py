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
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    name, gwa = line.split(",")
                    student = StudentGwa(name, float(gwa))
                    self.students.append(student)

        except FileNotFoundError:
            print("File not found")

    def top_student(self):
        top_student = self.students[0]
        for student in self.students:
            if student.gwa < top_student.gwa:  #The lower number of GWA (i.e 1.10, 1.20, etc), the higher the rank
                top_student = student

        return top_student
