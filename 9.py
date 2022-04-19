# ตอนที่ 11 - Class & Instance Variable

class Employee: #การสร้างคลาส
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    __companyName = "บริษัทxyzจำกัด"
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
    
class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self): #default constructor
        pass
        

class Programmer(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "โปรเเกรมเมอร์"
    def __init__ (self): #default constructor
        pass

class Sale(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานขาย"
    def __init__ (self): #default constructor
        pass


#การสร้างวัตถุ
account = Accounting()
print(account._Employee__companyName) #เข้าถึงตัวเเบบ Private

programmer = Programmer()
print(programmer._minSalary)  #เข้าถึงตัวเเบบ Protected
sale = Sale()



'''
obj1 = Employee("tao",5000,"mhee")


print("เ��ิ��เดือ��ต��ำสุด��อ������ั����า�� = "+str(Employee._maxSalary))
print(obj1._companyName)'''
