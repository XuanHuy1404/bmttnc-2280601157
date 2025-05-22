print("Nhap các dòng văn bản(Nhập'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    print("\nCac Dòng Đã Nhập Sau Khi Chuyển Thành Chữ In Hoa:")
    for line in lines:
        print(line.upper())
        
        