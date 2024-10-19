class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(f"Roll No: {student.student_id}, Name: {student.name}, Major: {student.major}, Section: {student.section}")

    def show_teachers(self):
        print(f"Teachers in {self.name}:")
        for teacher in self.teachers:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}, Class Section: {teacher.section}")
            teacher.show_timetable()

class Human:
    def __init__(self, name):
        self.name = name

class Student(Human):
    def __init__(self, university, student_id, name, major, section):
        super().__init__(name)
        self.student_id = student_id
        self.major = major
        self.section = section
        university.add_student(self)

class Teacher(Human):
    def __init__(self, name, subject, section, timetable):
        super().__init__(name)
        self.subject = subject
        self.section = section
        self.timetable = timetable

    def show_timetable(self):
        print(f"Timetable for {self.name} ({self.subject}, {self.section} section):")
        for day, time in self.timetable.items():
            print(f"{day}: {time}")

# Initialize University
ntu = University("National Textile University (NTU)")

# Add Students
student1 = Student(ntu, 101, "Hassan", "Computer Science", "Morning")
student2 = Student(ntu, 102, "Ali", "Botany", "Evening")
student3 = Student(ntu, 103, "Ahmed", "MBBS", "Morning")

# Add Teachers
teacher1 = Teacher("Dr. Ashfaq", "Mathematics", "Morning", {
    "Monday": "9 AM - 11 AM",
    "Wednesday": "10 AM - 12 PM",
    "Friday": "2 PM - 4 PM"
})
teacher2 = Teacher("Prof. Ammar", "Computer Science", "Evening", {
    "Tuesday": "11 AM - 1 PM",
    "Thursday": "1 PM - 3 PM"
})

# Register Teachers in University
ntu.add_teacher(teacher1)
ntu.add_teacher(teacher2)

# Display University Data
ntu.show_students()
ntu.show_teachers()
