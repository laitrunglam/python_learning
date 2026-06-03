

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def find_student_by_id (id,list_student):
    for i in list_student:
        if id ==i["student_id"]:
            return True
    return False

def validate_score(score_input):
    if not score_input.isdigit():
        return False
    if float(score_input)<0 or float(score_input)>10:
        return False
    return True

def  find_student_by_id_1(student_list, student_id):

    for i in student_list:
        if student_id == i["student_id"]:
            return i



def update_score(student_list):
    while True:
        ma=input("nhap ma hoc vien: ")
        flag=find_student_by_id_1(student_list,ma)
        if flag is None:
            print("ma hoc sinh ko ton tai yeu cau nhap lai:")
            continue
        else:
            while True:
                new_math=input("nhap diem toan: ")
                if validate_score(new_math)==False:
                    print("yeu cau nhap lai")
                    continue
                new_eng=input("nhap diem tieng anh: ")
                if validate_score(new_eng)==False:
                    print("yeu cau nhap lai")
                    continue
                flag["math_score" ] = float(new_math)
                flag["english_score"] =float(new_eng)
                print("DA CAP NHAT THANH CONG")
                break
            break




def add_student(student_list):
    while True:
        ma=input("nhap ma hs: ").strip().upper()
        flag=0
        for i in students:
            if find_student_by_id(ma,student_list) == True:
                flag=1
                break
        if flag==1:
            print("yeu cau nhap lai")
            continue
        else:
            name_new= input("NHAP TEN NV MOI: ").title()
            while True:
                math_new= input("nhap diem toan: ")
                if validate_score(math_new) == False:
                    continue
                new_eng=input("nhap diem tieng anh: ")
                if validate_score(new_eng)==False:
                    continue

                student_list.append({
                    "student_id": ma,
                    "name": name_new,
                    "math_score": float(math_new),
                    "english_score": float(new_eng)
                })
                print("DA THEM THANH CONG")
                break
            break



def display_students(student_list):
    if len(student_list):
        for i,value in enumerate(student_list,start=1):
            print(f"{i}. MA: {value["student_id"]} | TEN { value["name"]}  | TOAN: {value["math_score"]} | VAN {value["english_score"]}")


if __name__ == '__main__':
    while True:
        print("""
        ===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
        1. Hiển thị danh sách học viên
        2. Thêm học viên mới
        3. Cập nhật điểm thi theo mã học viên
        4. Đánh giá học lực của toàn bộ học viên
        5. Thoát chương trình
        """)
        choose= input("NHAP LUA CHON TU 1-?5")
        match choose:
            case "1":
                display_students(students)
            case "2":
                add_student(students)
            case "3":
                update_score(students)
            case "4":
                evaluate_students(students)