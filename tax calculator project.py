class Students: # a object or an inatance of a class.
#class is a blueprint that defines a set of values and actions.  
#The instance of the class made the __init__ method constructor.
#Constructor a function associated with a class.

    def __init__ (self,first_name, last_name):#Constructor

#self is a variable.
#self refers to an instance of a class.
#self.first_name is attributes.
#Attribute is a variable associated with a class.
   
        self.first_name = first_name #Attribute.
        self.last_name = last_name #Attribute.


    def full_name(self): #A class function.
        return f"student full name: {self.first_name} {self.last_name}"

#student_one = Variable.
#Students = an instance of class.
student_one = Students("Hady", "Al Masri") 
print(student_one.full_name())
print(student_one.first_name)
print(student_one.last_name)




