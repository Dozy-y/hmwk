class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return self.make, self.model, self.fuel_type
Car1=Car('Toyota', 'Supra', '95')
print(Car1.get_info())
