# ตอนที่ 17 - Overloading Method

from traceback import print_tb


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
#-----------------------------------------------------------------------------------
class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self,name,salary,age): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์ของคลาสเเม่
        #ทำการเพิ่ม Attribute ภายในคลาส
        self._age = age
    
    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):
        '''print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) '''
        
        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("อายุ = ",format(self._age)) 
        print("##########################################")

        def __str__(self):
            return (super().__str__()+"อายุ = {}".format(self._age))

#-----------------------------------------------------------------------------------
class Programmer(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "โปรเเกรมเมอร์"
    def __init__ (self,name,salary,experience,skills): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่
        self._exp = experience
        self._skills = skills

    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):

        '''print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) '''

        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("ประสบการณ์ = "+str(self._exp)) 
        print("ทักษะ = "+self._skills) 
        print("##########################################")

    def __str__(self):
            return (super().__str__()+"ประสบการณ์ = {},ทักษะ = {}".format(self._exp,self._skills))

#-----------------------------------------------------------------------------------
class Sale(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานขาย"
    def __init__ (self,name,salary,area): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่ 
        self._area = area
    
    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):
        '''print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) '''

        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("เขต = "+self._area) 
        print("##########################################")

    def __str__(self):
            return (super().__str__()+"เขต = {}".format(self._area))
#-----------------------------------------------------------------------------------


#เรียกใช้งาน เเบบผ่านคอนสทรัตเตอร์โดยตรง

account = Accounting("kong",1202,15)
print(account.__str__())

programmer = Programmer("kem",123,3,"c++")
print(programmer.__str__())

sale = Sale("tom",923,"surin")
print(sale.__str__())
