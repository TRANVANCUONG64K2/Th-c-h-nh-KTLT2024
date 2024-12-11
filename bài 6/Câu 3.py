print("TRAN VAN CUONG")
print("MSSV: 235752021610043") 
# Class cơ sở
class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu = Nu()
print(aNam.getGender())  
print(aNu.getGender())   
