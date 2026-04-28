from student_gwa import StudentConfig

manager = StudentConfig()
manager.read_students()

top_student = manager.top_student()
print(top_student.name, top_student.gwa)

