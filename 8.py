# ตอ��ที�� 11 - Class & Instance Variable

class Employee: #��ารสร��า����ลาส
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "��ริษัทxyz��ำ��ัด"
#----------------------------------------------------------------
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #��ำห��ด Attribute 
        self.__salary = salary #��ำห��ด Attribute 
        self._department = department #��ำห��ด Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("��ื��อ����ั����า�� = {}".format(self.__name))
        print("เ��ิ��เดือ�� = {}".format(self.__salary))
        print("เเ������ = {}".format(self.__department))  '''

    
    def _showData(self):
        print("��ื��อ����ั����า�� = "+self.__name)
        print("เ��ิ��เดือ�� = ",format(self.__salary))
        print("เเ������ = "+self._department) 
    
'''
#----------------------------------------------------------------
    #��รั������าตัวเเ��ร����เม��อด(setter)
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
#-----------------------------------------------------------------
    #รั������า��า��ตัวเเ��ร����เม��อด(getter)
    
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

#------------------------------------------------------------------
'''


#��ารสร��า��วัตถุ
obj1 = Employee("tao",5000,"mhee")


print("เ��ิ��เดือ��ต��ำสุด��อ������ั����า�� = "+str(Employee._maxSalary))
print(obj1._companyName)