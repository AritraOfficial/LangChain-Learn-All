from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name : str = 'Aritra'
    age:  Optional[int] = None
    email : EmailStr 
    cgpa: float = Field(gt=0,lt=10)
    
    
# new_stu = {'name':'Aritra'}
new_stu = {'age':22, 'email':'abc@co.in', 'cgpa':1}

student = Student(**new_stu)

print(student)

#you can also convert the model to a dictionary and json 
stu_dict = dict(student)
stu_json = student.model_dump_json()
print(stu_dict['age'])
print(stu_json)