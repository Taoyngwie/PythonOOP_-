class Employee: #การสร้างคลาส
    # class vatiable 
    _minSalary = 12000
    _maxSalary = 50000
    companyName = "บริษัทxyzจำกัด"
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

    #คำนวนโบนัส
    #โดยที่เราจะกำหนดโบนัสเป็นค่าเริ่มต้น = 0
    def _getIncome(self,bonus=0):
        return (self.__salary * 12) + bonus

    #คำนวนโบนัส + ล่วงเวลา
    #โดยที่เราจะกำหนดโบนัสเป็นค่าเริ่มต้น = 0
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary * 12) + bonus + overtime

    #เเปลงจาก obj เป็น str (ซึ่งจะส่งค่าออกไปเป็น str)
    def __str__(self):
        return ("ชื่อพนักงาน = {},เเผนก = {},เงินเดือน = {},รายได้ต่อปี = {} "
        .format(self.__name,self._department,self.__salary,self._getIncome()))