def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mời Nhập Chuỗi cần Đảo Ngược:")
print("Chuỗi Đảo Ngược là :", dao_nguoc_chuoi(input_string))