
class Employee(object):
    def __init__(self,name,age,salary,employment_year):
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year
        emp1=[]
    def get_working_years(self):
        return 2020-self.employment_year


class Manager(Employee):

    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage=bonus_percentage
    def get_working_years(self):
        return 2020-self.employment_year

    def get_bonus(self):

        return self.bonus_percentage * self.salary



def main():
    emp=[]
    man=[]
    options=["Show Employees","Show Managers","Add An Employee","Add A Manager","Exit"]
    print("Welcome to HR Pro 2019")
    print("Options: ")
    for index,variable in enumerate(options,1):
        print(f"{index}. {variable}")
    while True:
        choice=int(input("What would you like to do? "))
        if(choice==1):
            if not emp:
                print("Employees")
                print()
            else:
                for num in emp:
                    print(f"Name: {num.name} Age:  {num.age} Salary:  {num.salary} Working Years:  {num.get_working_years()}")
        elif(choice==2):
            if not man:
                print("Managers")
                print()
            else:
                for num in man:
                    print(f"Name: {num.name} Age:  {num.age} Salary:  {num.salary} Working Years:  {num.get_working_years()} Bonus: {num.get_bonus()}")
        elif(choice==3):
            name=input("Name: ")
            age=int(input("Age: "))
            salary=int(input("Salary: "))
            emp_year=int(input("Employment Year: "))
            emp1=Employee(name,age,salary,emp_year)
            emp.append(emp1)

            print("Employee added successfully")
        elif(choice==4):
                name=input("Name: ")
                age=int(input("Age: "))
                salary=int(input("Salary: "))
                emp_year=int(input("Employment Year: "))
                bonus_percentage=float(input("Bonus Percentage: "))
                man1=Manager(name,age,salary,emp_year,bonus_percentage)
                man1.get_bonus()
                man.append(man1)

                print("Manager added successfully")
        elif(choice==5):
            break
        else:
            print("you have entered a wrong number")


if __name__ == '__main__':
    main()
