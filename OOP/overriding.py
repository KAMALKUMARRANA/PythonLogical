class Emp:
    def fun(self,x,y):
        return(x+y)
    def sum(self,a,b,c=0):
        return (a+b+c)
class St(Emp):
    def fun(self,x,y):
        print(super().fun(x, y))
        return(x*y)




emp=St()
print(emp.fun(10,12))
print(emp.sum(10,15,20)) # overloading
print(emp.sum(10,15))

