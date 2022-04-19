# เธ•เธญเธ�เธ—เธตเน� 11 - Class & Instance Variable

class Employee: #เธ�เธฒเธฃเธชเธฃเน�เธฒเธ�เธ�เธฅเธฒเธช
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    __companyName = "เธ�เธฃเธดเธฉเธฑเธ—xyzเธ�เธณเธ�เธฑเธ”"
#----------------------------------------------------------------
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #เธ�เธณเธซเธ�เธ” Attribute 
        self.__salary = salary #เธ�เธณเธซเธ�เธ” Attribute 
        self.__department = department #เธ�เธณเธซเธ�เธ” Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("เธ�เธทเน�เธญเธ�เธ�เธฑเธ�เธ�เธฒเธ� = {}".format(self.__name))
        print("เน€เธ�เธดเธ�เน€เธ”เธทเธญเธ� = {}".format(self.__salary))
        print("เน€เน€เธ�เธ�เธ� = {}".format(self.__department))  '''

    
    def _showData(self):
        print("เธ�เธทเน�เธญเธ�เธ�เธฑเธ�เธ�เธฒเธ� = "+self.__name)
        print("เน€เธ�เธดเธ�เน€เธ”เธทเธญเธ� = ",format(self.__salary))
        print("เน€เน€เธ�เธ�เธ� = "+self._department) 
    
class Accounting(Employee): #เธชเธทเธ�เธ—เธญเธ”เธ�เธฅเธฒเธชเธกเธฒเธ�เธฒเธ� Employee
    __departmentName = "เธ�เธ�เธฑเธ�เธ�เธฒเธ�เธ�เธฑเธ�เธ�เธต"
    def __init__ (self): #default constructor
        pass
        

class Programmer(Employee): #เธชเธทเธ�เธ—เธญเธ”เธ�เธฅเธฒเธชเธกเธฒเธ�เธฒเธ� Employee
    __departmentName = "เน�เธ�เธฃเน€เน€เธ�เธฃเธกเน€เธกเธญเธฃเน�"
    def __init__ (self): #default constructor
        pass

class Sale(Employee): #เธชเธทเธ�เธ—เธญเธ”เธ�เธฅเธฒเธชเธกเธฒเธ�เธฒเธ� Employee
    __departmentName = "เธ�เธ�เธฑเธ�เธ�เธฒเธ�เธ�เธฒเธข"
    def __init__ (self): #default constructor
        pass


#เธ�เธฒเธฃเธชเธฃเน�เธฒเธ�เธงเธฑเธ•เธ–เธธ
account = Accounting()
print(account._Employee__companyName) #เน€เธ�เน�เธฒเธ–เธถเธ�เธ•เธฑเธงเน€เน€เธ�เธ� Private

programmer = Programmer()
print(programmer._minSalary)  #เน€เธ�เน�เธฒเธ–เธถเธ�เธ•เธฑเธงเน€เน€เธ�เธ� Protected
sale = Sale()



'''
obj1 = Employee("tao",5000,"mhee")


print(str(Employee._maxSalary))
print(obj1._companyName)'''
