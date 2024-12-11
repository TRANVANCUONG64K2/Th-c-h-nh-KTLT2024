print("TRAN VAN CUONG")
print("MSSV: 235752021610043") 
print("#############################")
######################################​
S = input("Nhập chuỗi S: ")

# Duyệt qua từng ký tự trong chuỗi
for char in S:
    # Kiểm tra nếu ký tự không phải là dấu cách hoặc dấu tab
    if char != " " and char != "\t":
        print(char)
