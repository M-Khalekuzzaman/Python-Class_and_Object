#Class is a templete
'''
class Student :
    roll = " "
    gpa = " "

rahim = Student()
rahim.roll = 101
rahim.gpa = 3.50
print(f"Roll : {rahim.roll}, gpa : {rahim.gpa}")

karim = Student()
karim.roll = 102
karim.gpa = 3.60
print(f"Roll : {karim.roll}, gpa : {karim.gpa}")
'''
class StudentInfo :
    name = " "
    roll = " "
    cgpa = " "
    session = " "

rahim = StudentInfo()
#print(isinstance(rahim,StudentInfo))
rahim.name = "Khalekuzzaman"
rahim.roll = 101
rahim.cgpa = 3.92
rahim.session ='2018-19'
print(f" Name : {rahim.name}, Roll : {rahim.roll}, Cgpa : {rahim.cgpa}, Session : {rahim.session}")

karim = StudentInfo()
#print(isinstance(rahim,StudentInfo))
karim.name = "Kaochar"
karim.roll = 102
karim.cgpa = 3.72
karim.session ='2018-20'
print(f" Name : {karim.name}, Roll : {karim.roll}, Cgpa : {karim.cgpa}, Session : {karim.session}")