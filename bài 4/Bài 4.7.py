print("TRAN VAN CUONG")
print("MSSV: 235752021610043") 
print("#############################")
######################################​
chuoi = input("Nhập chuỗi đi thằng tê: ")
chuoi_moi = ""

for ky_tu in chuoi:
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu

print("Chuỗi mới: ", chuoi_moi)
