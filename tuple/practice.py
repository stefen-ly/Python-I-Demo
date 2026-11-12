# Student registration
student = ("Dara", 20, "Computer Science", "Year 3")
print("=> 1 - Student Registration")
print("Student name:", student[0])
print("Major:", student[2])
print("Total items:", len(student))
print("Student year:", student[-1])
("--------------------------------------------------------------------------------------")

# Course enrollment
courses = ("Python", "Database", "Networking", "Python", "Web Development")
print("\n=> 2 - Course Enrollment")
print("Python count:", courses.count("Python"))
print("Networking index:", courses.index("Networking"))
for course in courses:
    print(course)
("--------------------------------------------------------------------------------------")

# Update student course
registered_courses = ("Python", "Database", "Networking")
course_list = list(registered_courses) 
course_list.append("Cloud Computing")
registered_courses = tuple(course_list)
print("\n=> 3 - Updated registration:", registered_courses)
