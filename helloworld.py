from typing import Dict

number = 10
text = "Hello, World!"

print (f"Number: {number} | Text: {text}")

class Employee:
    def __init__(self, name : str, role : str) -> None :
        self.name = name
        self.role = role
    
    def __del__(self):
        className : str = self.__class__.__name__
        print (f"destructor calls : {className}")
    
    def display_info(self) -> None :
        print (f"Name : {self.name} | Role: {self.role}")
    
    def to_dict(self) -> Dict[str, str] :
        return {"name": self.name, "role": self.role}

employee1 = Employee("Alice", "Developer")
employee1.display_info()
empDict : Dict[str, str] = employee1.to_dict()
employeeName : str = empDict["name"]

print ("----------")
employee1.role = "Engineer"
employee1.name = "David"
employee1.display_info()

print (f"Employee Name from dic : {employeeName}")