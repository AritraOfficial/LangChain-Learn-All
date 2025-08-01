from typing import TypedDict

class Person(TypedDict):  #person inherit from TypedDict
    name: str
    age: int
    city: str

#make a new dict called new_person - this is basically a new person object like a man or woman
new_person: Person = {"name": "John", "age": 30, "city": "New York"}  #(new_person: Person) means -  is a type of Person dict

print(new_person)







