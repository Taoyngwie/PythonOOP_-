from employee import Employee

class Programmer(Employee): #สืบทอดคลาสมาจาก Employee
    __departmentName = "โปรเเกรมเมอร์"
    def __init__ (self,name,salary,experience,skills): # รับพารามีเตอร์จากตัว Instance 
        super().__init__(name,salary,self.__departmentName) #เรียกใช้งานคอนสตรัทเตอร์คลาสเเม่
        self._exp = experience
        self._skills = skills

    #Method ที่ได้ทำการ Overwrite 
    def _showData(self):

        super()._showData() #ทำการปิดจากตัวที่เรา OverWrite เเล้วทำการเรียกคอนสตรัทเตอร์จากคลาสเเม่
        print("ประสบการณ์ = "+str(self._exp)) 
        print("ทักษะ = "+self._skills) 
        print("##########################################")

    def __str__(self):
            return (super().__str__()+"ประสบการณ์ = {},ทักษะ = {}".format(self._exp,self._skills))