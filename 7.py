class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return self.name, self.id
class Manager(Employee):
    def __init__(self, name, id, departament):
        Employee.__init__(self, name, id)
        self.departament = departament
    def manage_project(self):
        return self.name,'Управляет проектом в отделе', self.departament
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
    def perform_maintenance(self):
        return self.name,'Выполняет обслуживание по специальности', self.specialization
class TechManager(Manager, Technician):
    def __init__(self, name, id, departament, specialization):
        Manager.__init__(self, name, id, departament)
        Technician.__init__(self, name, id, specialization)
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        return [employee.get_info() for employee in self.team]
employee1 = Employee('Igor', 1)
employee2 = Employee('Gera', 2)
employee3 = Employee('Misha', 3)
for i in [employee1, employee2, employee3]:
    print(i.get_info())
manager1 = Manager('Vlada', 4, 'IT')
technician1 = Technician('Alex', 5, 'programmer')
tech_manager1 = TechManager('Jack', 6, 'IT', 'programmer')
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(employee2)
tech_manager1.add_employee(employee3)
print(tech_manager1.get_team_info())
