from employee import Employee


class Accounting(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self,name,salary,age): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์ของคลาสเเม่
        #ทำการเพิ่ม Attribute ภายในคลาส
        self._age = age
    
    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):
        
        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("อายุ = ",format(self._age)) 
        print("##########################################")

        def __str__(self):
            return (super().__str__()+"อายุ = {}".format(self._age))