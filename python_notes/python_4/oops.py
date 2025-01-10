class Car:
    year=2024
    count=0
    def __init__(self,brand, model):
        self.__brand=brand
        self.__model=model
    
    def getter(self):
        return self.__brand
    
    def setter(self,brand):
        self.__brand=brand
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod
    def static_method():
         Car.count+=1
         print(Car.count)
    
    @property
    def get_model(self):
        return self.__model

    
class Electric_Car(Car):
    def __init__(self,brand,model,range):
        super().__init__(brand,model)
        self.range=range 

tesla =Electric_Car('audi','a4',350000)
print(tesla.full_name())
tesla.setter('bmw')
print(tesla.get_model)

# Electric_Car.static_method()








        


