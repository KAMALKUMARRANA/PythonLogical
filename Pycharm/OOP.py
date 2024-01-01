# Class--> blueprint
# object ----->real life entity
class Employee:
    inc=1.5
    no_of_emp=0
    def __init__(self,fn,ln,sal): # instance
        self.fn=fn
        self.ln=ln
        self.sal=sal
        self.inc=1.4
        Employee.no_of_emp+=1
    def increment(self):
        self.sal=int(self.sal * Employee.inc) # 1.5 and self.inc -->1.5
    @classmethod # decorator
    def change_increment(cls,amount):
        cls.inc=amount
    @classmethod
    def from_str(cls,emp_str):
        fn,ln,sal=emp_str.split("-")
        return cls(fn,ln,sal)
    @staticmethod  #independent
    def is_open(day):
        if day =="Sunday":
            return False
        else:
            return True


kamal=Employee("Kamal","Rana",50000) #---->object
#print(Employee.no_of_emp)

print(Employee.no_of_emp)
print(kamal.__dict__)
print(Employee.__dict__)
#kamal.increment()

# print(kamal.fn,kamal.sal)
#
#
# print(kamal.sal)
# Employee.change_increment(3)
# kamal.increment()
# print(kamal.sal)
#
# harry=Employee.from_str("harry-Das-40000")
# print(harry.fn,harry.sal)

# subham=Employee("Subham","Das",25000)
# print(Employee.is_open("Monday"))


# inheritance---------------------------->
class Programmer(Employee):
    def __init__(self,fn,ln,sal,proglang,exp):
        super().__init__(fn,ln,sal)
        self.proglang=proglang
        self.exp=exp

    def increment(self):
        self.sal = int(self.sal * Employee.inc+0.2)



kamal=Programmer("Kamal","Rana",150000,"Python",5)
print(kamal.fn,kamal.ln,kamal.sal,kamal.proglang,kamal.exp)
help(Programmer)







