# ตอนที่ 14 - รู้จักกับ Super

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
        self._department = department #กำหนด Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("เเผนก = {}".format(self.__department))  '''

    
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) 
    
#ใช้งานเเบบท่ี่ 1
#----------------------------------------------------------------
'''class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์ของคลาสเเม่
        
class Programmer(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "โปรเเกรมเมอร์"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่

class Sale(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานขาย"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่ '''

#ใช้งานเเบบที่ 2
#----------------------------------------------------------------
class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์ของคลาสเเม่
        super()._showData()  #เรียกใช้งานจากคลาสเเม่ 
        
class Programmer(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "โปรเเกรมเมอร์"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #
        super()._showData() #เรียกใช้งานจากคลาสเเม่ 

class Sale(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานขาย"
    def __init__ (self,name,salary): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่
        super()._showData() #เรียกใช้งานจากคลาสเเม่ 
#----------------------------------------------------------------



#เรียกใช้งานของเเบบ 1
#----------------------------------------------------------------
'''
account = Accounting("kong",1202)
account._showData()
print()
programmer = Programmer("kem",123)
programmer._showData()
print()
sale = Sale("tom",923)
sale._showData()
'''
#----------------------------------------------------------------


#เรียกใช้งานของเเบบ 2
#----------------------------------------------------------------
account = Accounting("kong",1202)
print()
programmer = Programmer("kem",123)
print()
sale = Sale("tom",923)
#----------------------------------------------------------------



