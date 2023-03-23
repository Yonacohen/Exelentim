import datetime
from datetime import datetime
def func_difference(dat):
    if type(dat) is datetime :
         if (datetime.today()<dat):          #check if we recive future date
             dif = dat - datetime.today()
             #print (dat)
             return dif
    return("Only a future date")
d=datetime(2023,3,18)
dd= func_difference(d)
print (dd.days)
















