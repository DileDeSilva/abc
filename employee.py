from status import Status

class Employee:
    def __init__(self, name, id, dep, designation):
        self.name = name
        self.id = id
        self.dep = dep
        self.designation = designation
        self.status = Status.Active

    def __str__(self):
            return "employee name: " + self.name + "employee id: " + self.id +"department: " + self.dep + "designation: " + self.designation + "status: " + self.status