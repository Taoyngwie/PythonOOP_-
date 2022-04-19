# à¸•à¸­à¸ÿà¸—à¸µà¹ÿ 11 - Class & Instance Variable

class Employee: #à¸ÿà¸²à¸£à¸ªà¸£à¹ÿà¸²à¸ÿà¸ÿà¸¥à¸²à¸ª
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "à¸ÿà¸£à¸´à¸©à¸±à¸—xyzà¸ÿà¸³à¸ÿà¸±à¸”"
#----------------------------------------------------------------
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #à¸ÿà¸³à¸«à¸ÿà¸” Attribute 
        self.__salary = salary #à¸ÿà¸³à¸«à¸ÿà¸” Attribute 
        self._department = department #à¸ÿà¸³à¸«à¸ÿà¸” Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("à¸ÿà¸·à¹ÿà¸­à¸ÿà¸ÿà¸±à¸ÿà¸ÿà¸²à¸ÿ = {}".format(self.__name))
        print("à¹€à¸ÿà¸´à¸ÿà¹€à¸”à¸·à¸­à¸ÿ = {}".format(self.__salary))
        print("à¹€à¹€à¸ÿà¸ÿà¸ÿ = {}".format(self.__department))  '''

    
    def _showData(self):
        print("à¸ÿà¸·à¹ÿà¸­à¸ÿà¸ÿà¸±à¸ÿà¸ÿà¸²à¸ÿ = "+self.__name)
        print("à¹€à¸ÿà¸´à¸ÿà¹€à¸”à¸·à¸­à¸ÿ = ",format(self.__salary))
        print("à¹€à¹€à¸ÿà¸ÿà¸ÿ = "+self._department) 
    
'''
#----------------------------------------------------------------
    #à¸ÿà¸£à¸±à¸ÿà¸ÿà¹ÿà¸²à¸•à¸±à¸§à¹€à¹€à¸ÿà¸£à¹ÿà¸ÿà¹€à¸¡à¸ÿà¸­à¸”(setter)
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
#-----------------------------------------------------------------
    #à¸£à¸±à¸ÿà¸ÿà¹ÿà¸²à¸ÿà¸²à¸ÿà¸•à¸±à¸§à¹€à¹€à¸ÿà¸£à¹ÿà¸ÿà¹€à¸¡à¸ÿà¸­à¸”(getter)
    
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

#------------------------------------------------------------------
'''


#à¸ÿà¸²à¸£à¸ªà¸£à¹ÿà¸²à¸ÿà¸§à¸±à¸•à¸–à¸¸
obj1 = Employee("tao",5000,"mhee")


print("à¹€à¸ÿà¸´à¸ÿà¹€à¸”à¸·à¸­à¸ÿà¸•à¹ÿà¸³à¸ªà¸¸à¸”à¸ÿà¸­à¸ÿà¸ÿà¸ÿà¸±à¸ÿà¸ÿà¸²à¸ÿ = "+str(Employee._maxSalary))
print(obj1._companyName)