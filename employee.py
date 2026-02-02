from status import Status

class Employee:
    def __init__(self, name, id, dep, designation):
        self.name = name
        self.id = id
        self.dep = dep
        self.designation = designation
        self.status = Status.Active

name="dile"
id="123"
dep="IT"
designation="manager"
Status=""

Employee(name, id, dep, designation, Status)