
from programmer import Programmer
from sale import Sale
from acount import Accounting

acount = Accounting("kong",1202,15)
print("พนักงานบัญชี รายได้ต่อปี = "+str(acount._getIncome()))

programmer = Programmer("kem",123,3,"c++")
print("โปรเเกรมเมอร์ รายได้ต่อปี = "+str(programmer._getIncome(10000))) #Overload parameter ใน Method

sale = Sale("tom",923,"surin")
print("พนักงานขาย รายได้ต่อปี = "+str(sale._getIncome(500,450))) #Overload parameter ใน Method
