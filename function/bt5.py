student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def display_statements(records):
    print("HIEN THI SAO KE DIEM SO: ")

    for index,i in enumerate( records,start=1):
        if i["current_points"]< 500:
            status="can tich luy them"
        elif 500<=i["current_points"]<=1500:
            status="thanh vien tiem nang"
        elif i["current_points"]>1500:
            status="thanh vien uu tu"
        print(f"{index}. MA {i["student_id"]} | TEN {i["name"]}  | HIEN CO{i["current_points"]} |  DA TIEU {i["spent_points"]}|"
              f"HOAN TRA {i["refunded_points"]} | HE SO {i["multiplier"]} | {status}")

def redeem_rewards(records) :
    ma=input("MOI BAN  NHAP MA HOC VIEN DOI QUA: ").strip().upper()
    flag=None
    for i in records:
        if i["student_id"] == ma:
            flag=i
            break
    if flag is None:
        print("MA K TON TAI")
    diem=int(input("NHAP SO DIEM CAN TIEU "))
    if diem<=0 or diem>flag["current_points"]:
        print("DIEM SO PHAI LON HON 0 VA KO DC VUOT QUA CURRENT POINT")
    else:
        flag["current_points"]-=diem
        flag["spent_points"]+=diem
        print(f"GIAO DICH THANH CONG {flag["name"]} da tieu {diem} . SO DU CON LAI: {flag["current_points"]}")

def grade_assignment(records):
    while True:
        ma=input("nhap ma hv: ")
        flag=None
        for i in records:
            if i["student_id"]==ma:
                flag=i
                break
        if flag is None:
            print("nhap ma sai")
        else:
            nhap_diem=int(input("NHAP DIEM GOC DAT DUOC: "))
            diem_thuc=nhap_diem*flag["multiplier"]
            flag["current_points"] +=diem_thuc
            print(f"HE SO HIEN TAI CUA {flag["name"]} la : {flag["multiplier"]} .DIEM THUC NHAN {diem_thuc}")
            print(f"DA CONG {diem_thuc} vao tk")
            break



if __name__ == "__main__":
    while True:
        print("""
        ===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
        1. Hiển thị sao kê điểm số
        2. Đổi điểm lấy phần thưởng
        3. Phúc khảo bài thi (Hoàn điểm)
        4. Kích hoạt (Hệ số nhân điểm)
        5. Chấm bài (thêm điểm)
        6. Thoát chương trình
        =====================================================
        """)
        choose=input("NHAP LUA CHON TU 1->6: ")
        match choose:
            case "1":
                display_statements(student_records)
            case "2":
                redeem_rewards(student_records)
            case "3":
                grade_assignment(student_records)
