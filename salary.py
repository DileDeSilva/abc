class Salary:
    def __init__(self,basicSalary, allowance):
        self.basicSalary = basicSalary
        self.allowance = allowance

    def cal_netSalary(self):
        self.netSalary = self.basicSalary + self.allowance
        return self.netSalary

    def __str__(self):
        return "basic salary: " + self.basicSalary + "allowance : " + self.allowance + "net salary: " + str(self.cal_netSalary())
