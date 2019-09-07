class Employee:
    employee_count=0
    emp_salary=0
    income=[]
    def __init__(self,name,family,salary,departement):
        self.name=name
        self.family=family
        self.salary=salary
        self.departement=departement
        Employee.employee_count+=1
        Employee.emp_salary = Employee.emp_salary+self.salary
    def avg_salary(self):
        avg=Employee.emp_salary/Employee.employee_count
        return(print(avg))
class FullEmployee(Employee):
    def __init__(self,name,family,salary,departement,age):
        Employee.__init__(self,name,family,salary,departement)
        self.age=age
    def sample(self):
        return(print("method is invoked"))

emp1= Employee('jhon','smith',60000,'developer')
emp2= Employee('kate','hjk',70000,'tester')
emp3=FullEmployee('x','y',90,'v',43)
emp3.sample()
emp1.avg_salary()
print(Employee.employee_count)



