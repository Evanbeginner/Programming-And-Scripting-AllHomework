class Employee:
    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp +=1
        fullname = self.first + self.last
    

    def Display(self):
        print("First name {} {} Pay {}".format(self.first,self.last, self.pay))

    @classmethod
    def from_string(cls,emp_str):
         first,last,pay = emp_str.split('-')
         return cls(first,last,pay)
         

    def applyraise(self):

        self.pay = int(self.pay* self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
         cls.raise_amount = amount
      
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
         return False
        return True
    
     


class Developer(Employee):
 raise_amount=1.11
 def __init__(self,first,last,pay,prog_lang):
  super().__init__(first,last,pay)
  self.pro_lang = prog_lang



class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None :
            self.employees = []
        else: 
            self.employees = employees

    def addemployee(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)
        
    def printemployees(self):
        for emp in self.employees:
            print('--',emp.fullname())

    def removeemp(self,emp):
     if emp in self.employees:
       self.employees.remove(emp)

dev1 = Developer('Evan','Kelly',45000,'Python')

mng_1 = Manager('Sue','Smith',90000, [dev1])
mng_1.printemployees()


            









