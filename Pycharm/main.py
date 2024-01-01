# String -----> Immutable
name="Kamal Kumar"
print(name.upper())
print(name)
print(name.find('m')) # return index
print(name.find("Kumar"))
print(name.replace("Kumar","Rana"))
print(name.replace("K","R"))
print("K" in name)

#operators------------------------------->
# Arithmetric +,-,/,//,*,**,%
print(5+1)
print(5//2)
print(5**2) #-------> power
i=5
i+=2
print(i)

# Comparision >,<,>=,<=,==,!=
#Logical or,and,not

#Control Structure---------------->
age=18
if age >18:
    print("you are an adult")
elif age==18:
    print("you are new adult")
else:
    print("You Can not adult")
num=range(5)
print(num) # 0,1,2,3,4
for i in range(1,6):
    print(i)

i=1
while i<=5:
    print(i*'*')
    i+=1
i=5
while i>=0:
    print(i*'*')
    i-=1



