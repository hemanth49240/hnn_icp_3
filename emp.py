class Employee:
  def __init__(self):  #constructor for name,family,salary and Department.
        self.name ="Hemanth "
        self.family =4
        self.salary=7777
        self.department="CSE"
  def __init__(self,name,family,salary,department):
        self.name =name
        self.family =family
        self.salary=salary
        self.department=department

  def count_emp(self,emp1,fullemp1):
        print("The total Number of Employees(employee+Fulltime employee):",len(emp1+fullemp1)) #counting number of employees.

  def avg_salary(self,emp1,fullemp1):  #function for calculating the average salaryof all employees.
       su=0
       for i in emp1:
           su=su+i.salary
       for i in fullemp1:
            su=su+i.salary
       print("the average salary of the all the Employees(employee+Fulltime employee):",su/2)

class Fulltime_Employee(Employee):
    pass
n=int(input("enter number of employees"))
pe=[]
for i in range(0,n):  #using for() loop,take the input dynamically.
    na=input("enter name")
    f=int(input("enter how many family members"))
    s=int(input("enter salary"))
    d=input("enter department")
    obj=Employee(na,f,s,d)
    pe.append(obj)
full=int(input("enter Full time employees"))
fe=[]
for i in range(0,full):
    na=input("enter name")
    f=int(input("enter how many family members"))
    s=int(input("enter salary"))
    d=input("enter department")
    obj=Fulltime_Employee(na,f,s,d)
    fe.append(obj)

result=Fulltime_Employee(na,f,s,d)
result.count_emp(pe,fe) #function call
result.avg_salary(pe,fe) #function call