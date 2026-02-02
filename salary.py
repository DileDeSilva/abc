class Salary:
    def __init__(self,basicSalary, allowance):
        self.basicSalary = basicSalary
        self.allowance = allowance

    def cal_netSalary(self):
        self.netSalary = self.basicSalary + self.allowance
        return self.netSalary


basic_salary = input("Enter Basic Salary: ")
if basic_salary.replace(".","").isdigit():
    basic_salary=float(basic_salary)

allowance = input("Enter Allowance: ")
if allowance.replace(".","").isdigit():
    allowance=float(allowance)
sal = Salary(basic_salary, allowance)
print(sal.basicSalary, sal.allowance)
print("salary 1 ",sal.cal_netSalary())

sal2 = Salary(32000.00, 2000.00)
print(sal2.basicSalary, sal2.allowance)
print("salary 2", sal2.cal_netSalary())
