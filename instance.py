"""
class user():
    course='python'

o = user()
print(user.__dict__)
print(user.course)
print(o.__dict__)
print(o.course)
o.course= 'C++'
print(o.course) 
print(o.__dict__)

"""

class student:
    name = 'Vignesh'
    age  = '24'

    def printall(self,gender):
        print("Name  : ", student.name)
        print("Age   : ", student.age)
        print("Grnder: ", gender)


o=student()
o.printall( "male")      
student.printall(o,"Male")