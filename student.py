"""""
class student():
    name = 'vignesh'
    age = '24'


print(getattr(student, 'name'))
print(getattr(student, 'age'))
print(getattr(student, 'gender' , 'no such attribute found'))

print(student.name)
print(student.age)


setattr(student, 'name', 'sachin Vicky')
print(student.name)



setattr(student,'gender' , 'male')


print(student.gender)





student.city='Tiruvannamalai'


print(student.city)

print(student.__dict__)

del student.city
print(student.__dict__)


"""

class student ():
    name='Vignesh'
    age= 24

    def printall():
        print("Name : " ,student.name)
        print("Age :",student.age)

student.printall()
print(student.__dict__)

