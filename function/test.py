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
def display_students(student_list):
    if len(student_list) == 0 :
        print("DANH SASCH RONG")
    else:
        for index,value in enumerate(student_list,start=1):
            print(f"{index} | MA {value["student_id"]} | NAME {value["name"]} | TOAN: {value["math_score"]} | Tieng anh {value["english_score"]}")

def  find_student_by_id(student_list,id):
    for i in student_list:
        if i["student_id"] == id:
            return i
    return False




def validate_score(score_input):
    if not 0<=float(score_input)<=10:
        return False
    if not score_input.replace(".","").isdigit():
        return False

def add_student(student_list):
    while True:
        ma=input("nhap ma can them: ").strip().upper()
        if find_student_by_id(student_list,ma)==  True:
            print("TRUNG MA HOC SINH")
        else:

                name=input("nhap ten hoc vien moi").strip().title()
                while True:
                    new_math=input("nhap diem toan: ")
                    if validate_score(new_math) == False:
                        print("nhap lai: ")
                        continue
                    new_eng=input("nhap diem tieng anh:")
                    if validate_score(new_eng)==False:
                        print("nhap lai diem anh: ")
                        continue
                    student_list.append({
                        "student_id": ma,
                        "name": name,
                        "math_score": float(new_math),
                        "english_score": float(new_eng)
                    })
                    break
                break

def update_score(student_list):
    while True:
        ma=input("nhap ma hoc vien: ")
        if find_student_by_id(student_list,ma) == False:
            print("yeu cau nhap lai")
            continue
        while True:
            i=find_student_by_id(student_list,ma)
            new_math=input("yeu cau nhap diem toan")
            if validate_score(new_math) == False:
                print("yeu cau nhap lai: ")
                continue
            new_eng=input("yeu cau nhap lai iem tieng anh: ")
            if validate_score(new_eng) == False:
                print("yeu cau nhap lai: ")
                continue
            i["math_score"]= float(new_math)
            i["english_score"] =float(new_eng)













while True:
    print("""
    ===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
    1. Hiển thị danh sách học viên
    2. Thêm học viên mới
    3. Cập nhật điểm thi theo mã học viên
    4. Đánh giá học lực của toàn bộ học viên
    5. Thoát chương trình
    """)

    choose= input("nhap lua chon")
    match choose:
        case "1":
            display_students(students)
        case "2":
            add_student(students)