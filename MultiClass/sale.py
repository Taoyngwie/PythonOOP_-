from employee import Employee


class Sale(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "พนักงานขาย"
    def __init__ (self,name,salary,area): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่ 
        self._area = area
    
    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):

        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("เขต = "+self._area) 
        print("##########################################")

    def __str__(self):
            return (super().__str__()+"เขต = {}".format(self._area))