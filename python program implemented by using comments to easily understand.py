x=100#Global Variables                       
y=200
class X:#Super class(X)
    """sample class to test basic concepts of python programs"""#Documentational string it is a optional statement
    a=300#Static Variables
    b=400
    def __init__(self):#Constructor To initialize the nonstatic variables
        print("in constructor of X")#When ever we create object constructor method will be executed automatically
        self.p=500
        self.q=600#Non static variables
    def m1(self):#Normal method
        i=700
        j=800#Local variables
        print(i)
        print(j)
        print("in m1 of X")
    def m2(self):#Methods
        print("in m2 of X")
        print(x)
        print(y)
    def __del__(self):#Destructor method whenever we delete the object this method will be executed
        print("in destructor of X")
class Y(X):#Sub class(Y)
    c=900#Static variables
    d=1000
    def __init__(self):#Magic or Constructor or Initiator Methods
        self.r=1100#Nonstatic variables
        self.s=1200
        super().__init__()#We call superclass properties into subclass we use this statement explicetely purpose of nonstatic variables calling purpose
    def m2(self):#Methods
        print("in m2 of Y")
    def m3(self):#Methods
        print("in m3 of Y")
    def modify(self):#Methods
        Y.c=Y.c+100
        self.r=self.r+100
    def display(self):#Methods
        print(Y.c)
        print(Y.d)
        print(self.r)
        print(self.s)
        self.m2()
        self.m3()
        print(Y.a)
        print(Y.b)
        print(self.p)
        print(self.q)
        self.m1()
        super().m2()#We call super class methods with in the subclass we use this statement by method overwrite concept
r1=Y()
print(r1)
r1.display()
r1.modify()
r1.display()
r2=Y()
print(r2)
r2.display()
del r1#When ever we delete object destructor method will be executed

        
        
        
        
    
