grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]



def display_grades(book) :
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print("Mã SV | Tên Học Sinh        | Điểm Toán | Điểm Anh | ĐTB ")
    for i in book:
        print(f" id: {i["id"]} | TEN HOC SINH: {i["name"]} | DIEM TOAN {i["info"][0]} | DIEM TIENG ANH {i["info"][1]} |"
              f"DIEM TRUNG BINH {(i["info"][0] + i["info"][1])/2 }")
def  add_student(book):
    while True:
        ma=input("nhap ma hoc sinh: ")
        flag=1

        for i in book:
            if i["id"] ==ma:
                print("MA HS DA TON TAI VUI LONG NHAP MA KHAC ")
                flag=0
                break
        if flag ==1 :
            name=input("nhap ten hoc sinh")
            new_math=float(input("nhap diem toan: "))
            new_eng= float(input("nhap diem tieng anh: "))
            book.append(
                {"id": ma, "name": name, "info": (new_math,new_eng)}
            )
            print(f"IN RA THANH CONG{ma}")
            break

def update_scores(book):
    while True:
        ma=input("nhap ma hoc sinh: ")
        flag=None
        for i in book:
            if i["id"] ==ma:
                flag=i
                break
        if flag is None:
            print("yeu cau nhap lai ma: ")
            continue
        else:
            math_new=float(input("Nhap diem toan moi: "))
            eng_new=float((input("Nhap diem tieng anh moi: ")))
            flag["info"] = (math_new,eng_new)
            print(f"DA CAP NHAT THANH CONG SV {ma }")
            break

def delete_student(book):
    ma=input("nhap ma can xoa: ")
    flag=1
    for i in book:
        if i["id"] ==ma:
            flag=0
            book.remove(i)
            print("thong bao thanh cong")
            break
    if flag==1:
        print("ma k ton tai")


if __name__ =="__main__":
    while True:
        print("""
        === HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
    1. Xem bảng điểm học sinh
    2. Thêm hồ sơ học sinh mới
    3. Cập nhật điểm số
    4. Xóa hồ sơ học sinh
    5. Thoát chương trình
    ================================
        """)
        choose =input("NHAP LUA CHON TU 1->5: ")
        match choose:
            case "1":
                display_grades(grade_book)
            case "2":
                add_student(grade_book)
            case "3":
                update_scores(grade_book)
