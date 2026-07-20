# this is sample program for Class and objects in Python

class Check:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def primarytest(self):
        print(f'{self.name} is saying whoo whoo!')
        return

test1 = Check('Harry', 6)
print(test1.name)
test1.primarytest()

class Car:
    made = 'India'
    def __init__(self, color, model):
        self.color = color
        self.model = model
print(Car.made)

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)

# program to understand the built in methods

class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __str__(self):
        return self.title
    
    def __eq__(self, value):
        return (self.title == value.title)
    
book1 = Book('My book', 421)
book2 = Book('Your book', 232)

print(len(book1))
print(len(book2))
print(book1 == book2)
print(str(book1))
print(str(book2))

# Code for dynamic attributed
# This is required when we don't know the attribute name 

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age  = age


person1 = Person('Rohan', 23)

any_attribute = input('Enter the attribute to check: ')
print(getattr(person1, any_attribute, "Attribute not found"))