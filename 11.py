# ตอนที่ 15 - แปลง Object เป็น String

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

    #เเสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) 

    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    #เเปลงจาก obj เป็น str (ซึ่งจะส่งค่าออกไปเป็น str)
    def __str__(self):
        return ("ชื่อพนักงาน = {},เเผนก = {},เงินเดือน = {},รายได้ต่อปี = {} "
        .format(self.__name,self._department,self.__salary,self._getIncome()))

class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
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
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่ 


#เรียกใช้งาน เเบบผ่านคอนสทรัตเตอร์โดยตรง
account = Accounting("kong",1202)
print(account.__str__())
programmer = Programmer("kem",123)
#print(programmer.__str__())
sale = Sale("tom",923)