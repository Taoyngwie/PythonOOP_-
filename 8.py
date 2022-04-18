# ตอนที่ 11 - Class & Instance Variable

class Employee: #การสร้างคลาส
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "บริษัทxyzจำกัด"
#----------------------------------------------------------------
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #กำหนด Attribute 
        self.__salary = salary #กำหนด Attribute 
        self.__department = department #กำหนด Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("เเผนก = {}".format(self.__department))  '''

    
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) 
    
'''
#----------------------------------------------------------------
    #ปรับค่าตัวเเปรในเมธอด(setter)
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
#-----------------------------------------------------------------
    #รับค่าจากตัวเเปรในเมธอด(getter)
    
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

#------------------------------------------------------------------
'''


#การสร้างวัตถุ
obj1 = Employee("tao",5000,"mhee")


print("เงินเดือนต่ำสุดของพนักงาน = "+str(Employee._maxSalary))
print(obj1._companyName)