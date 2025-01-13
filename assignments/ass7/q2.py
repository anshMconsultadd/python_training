

class Employee:
   
   def __init__(self, name, id, salary):
       self.name = name
       self.id = id
       self.salary = salary



class fulltime(Employee):
    def __init_(self,name,id,salary):
        super().__init__(name, id, salary)
    def calculate_salary(self):
        salary = self.salary
        tax = 0.1 * salary
        pf = 0.12 *salary
        salary = salary - tax - pf
        return salary
    
class parttime(Employee):    
   def __init_(self,name,id,salary):
        super().__init__(name, id, salary)
        def calculate_salary(self):
            salary = self.salary
            tax = 0.1 * salary
            pf = 0.12 *salary
            salary = salary - tax - pf
            return salary
    
class contractor(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)
    def calculate_salary(self): 
        salary = self.salary
        tax = 0.1 * salary
        salary = salary - tax
        return salary


ansh=fulltime("Ansh", 1, 1000)
ayush=parttime("Ayush", 2, 1000)
gautam=contractor("Gautam", 3, 1000)

print(ansh.calculate_salary())
print(gautam.calculate_salary())

