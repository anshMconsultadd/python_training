# Create a class hierarchy for employees, with a base class and
# subclasses for full-time, part-time, and contractor employees.
# Include shared attributes like name, ID, and salary calculation in
# the base class. Each subclass should calculate the salary based
# on its type (full-time, part-time, contractor). Apply tax deductions
# (e.g., 10%) and Provident Fund (PF) deductions (e.g., 12%) for
# full-time and part-time employees. For contractors, apply only the
# tax deduction and no PF. The final salary after deductions should
# be returned for each employee type.

class Employee:
   name=""
   id=0
   salary=0
    
   def __init__(self, name, id, salary):
       self.name = name
       self.id = id
       self.salary = salary

    def calculate_salary(self):
        return self.salary
