#a class is a templete without any necessary of memory and defines the structure and behaviour
#properties:
#1.attribute-a variable that is defined to store value
#2.method(function)-the behaviour and that perform action on the defined variables
#a class is a blue print for creating objects that share similar attributes and behaviours
#---object---
#an object is a specific instance created from a class it has its own set of attributes values and can perform actions to the methods 
#defined in the class
#synatx-----
'''class Class_Name:
      statements
      def method_name(self,parameters):
            statements_block'''
#attributes and methods are called as members of class
#a method is similar to function you can define function anywhere if we define the function inside the class then it is method
#if it is a method the first argument should point to the address minimum one argument is required for method 
#a function can be with zero parameters
#you can can function directly anywhere if we want to call method then classname.method or create one object and call with object
#----OBJECT  CREATION SYNATAX
'''object_name=Class_Name()'''
#the object can access class variables and methods using the dot operator
'''object_name.class_member_name'''
class Test:
    id=1449
t=Test()
print(t.id)
#firstly it will not create any memory for class but it will create for the class members when object is created it will allocate 
# memory to classthat is t variable 
#c is famous for dynamic memory allocation
class Emp:
    def st_dtls(self,n,i):
        self.name=n
        self.id=i
    def dsply(self):
        print(self.name,self.id)
e1=Emp()
e1.st_dtls("harika",1449)
e1.dsply()   #when we call e1 then it will create memory 10k then it will project 10k to self w
print(e1.name,e1.id) #accessing outside
e2=Emp()
e2.st_dtls('xy',123)
e2.dsply()
#name and id belongs to object
#when we are creating object at that time only  we can initialise the variables by maintaining the method mname as __init__
class Emp1:
    def __init__(self,n,i):
        self.name=n
        self.id=i
    def dsply(self):
        print(self.name,self.id)
e3=Emp1('abc',123)
e3.dsply()
e4=Emp1('meghana',987)
e4.dsply()
#init method is called automatically when object is created
