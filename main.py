from employee import Employee
from salary import Salary

def display_menu():
    print("*********************************")
    print("*************WELCOME*************")
    print("Main Menu")
    print("1. Create Employee")
    print("2. Create Salary")
    print("3. Exit")
    print("*********************************")
    option=0
    while True:
        option=input("Enter the option")
        if option.isdigit() and option in ["1","2","3"]:
            option=int(option)
            break
        else:
            print("Invalid input")
    return option

def createEmp():
    name=input("enter emp name")
    id=input("enter emp id")
    dep=input("enter dep")
    designation=input("enter designation")

    emp=Employee(name, id, dep, designation)
    print(emp)

def createSal():
    while True:
        basic_salary = input("Enter Basic Salary: ")
        if basic_salary.replace(".","").isdigit():
            basic_salary=float(basic_salary)
            break
        else:
            print("enter valid basic salary")

    while True:
        allowance = input("Enter Allowance: ")
        if allowance.replace(".","").isdigit():
            allowance=float(allowance)
            break
        else:
            print("enter valid basic allowance")
        sal = Salary(basic_salary, allowance)
        print(sal.basicSalary, sal.allowance)
        print("salary 1 ",sal.cal_netSalary())

        sal2 = Salary(32000.00, 2000.00)
        print(sal2.basicSalary, sal2.allowance)
        print("salary 2", sal2.cal_netSalary())

def main():
    option = display_menu()
    if option ==1:
        createEmp()
    elif option ==2:
        createSal()
    else:
        exit()

if __name__ == "__main__":
    main()