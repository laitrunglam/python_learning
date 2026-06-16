
class MemberCard:
    point_value_vnd = 1000
    def __init__(self,card_id,name,points):
        self.card_id=card_i
        self.name=name
        self.__points=points
        self.__tier="Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        if card_id.startswith("RC") and card_id[2:].isdigit() and len(card_id)==4:
            return True
        return False

    @points.setter
    def points(self,value):
        if value<0:
            raise ValueError("NHAP SO K DUOC AM")
        self.__points=value

    @tier.setter
    def tier(self,value):
        self.__tier=value

    def earn_points(self,bill_amount) :
        tinh=bill_amount//10000
        self.__points+=tinh
        if self.__points>=100:
            self.__tier="VIP"
        return tinh

    def redeem_points(self,points_to_use):
        if 0<points_to_use<=self.__points:
            discount_use=points_to_use * self.point_value_vnd
            self.__points-=points_to_use
            return discount_use
        return None





db_coffee=[
    MemberCard('RC01',"NGUYEN VAN A",150),
    MemberCard('RC02','TRAN THI B',20)
]

def change_point(lst):
    print("--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
    new_ma=input("Nhập mã thẻ: ")
    for i in lst:
        if i.card_id==new_ma:
            point_use=int(input("Nhập số điểm muốn sử dụng:"))
            discount=i.redeem_points(point_use)
            if not discount is None:
                print(f"Đã trừ {point_use} điểm.")
                print(f"Khách hàng được giảm giá {discount}VNĐ vào hóa đơn!")
                print(f"Số điểm còn lại: {i.points}")
                print(f"Hạng thẻ hiện tại: {i.tier}")
            else:
                print("Không thể đổi điểm!")
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
                print(f"Điểm hiện tại của khách: {i.points}")
                print("Điểm cũ được giữ nguyên:")
                print(f"Số điểm sau giao dịch: {i.points}")
            break
    else:
        print("ma the k ton tai")

def display_coffee(lst):
    for i,value in  enumerate(lst,start=1):
        print(f"{i}. MA {value.card_id} | TEN {value.name} | DIEM {value.points} | HANG: {value.tier} ")

def register_card(lst):
    new_ma=input("Nhập mã thẻ:").upper()
    if not MemberCard.is_valid_card_id(new_ma) :
        print("Mã thẻ phải bắt đầu bằng chữ 'RC' và theo sau là 2 chữ số (Ví dụ: RC01, RC99)")
        return
    for i in lst:
        if i.card_id==new_ma:
            print("Mã thẻ đã tồn tại trong hệ thống! Vui lòng kiểm tra lại.")
            return
    new_name=input("Nhập tên khách hàng: ")
    print("Đăng ký thẻ thành viên thành công!")
    print(f"Mã thẻ: {new_ma}")
    print(f"Tên khách hàng: {new_name}")
    print("Điểm ban đầu: 0")
    print("Hạng thẻ: Standard")
    lst.append(MemberCard(new_ma, new_name, 0))

def tich_diem(lst):
    print("--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
    new_ma=input("Nhập mã thẻ: ")

    for i in lst:
        if i.card_id==new_ma:
            total_bill=int(input("Nhập tổng tiền hóa đơn: "))
            status=i.tier
            earn_p=i.earn_points(total_bill)
            print(f"Khách hàng: {i.name}")
            print(f"Hóa đơn: {total_bill} VNĐ")
            print(f"Số điểm được tích: {earn_p}")
            print(f"Tổng điểm hiện tại: {i.points}")
            if i.tier!=status:
                print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
            print(f"Hạng thẻ hiện tại: {i.tier}")
            break
    else:
        print("MA THE K TON TAI")







while True:
    choose=input("""
    ===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====
    1. Xem danh sách thẻ thành viên
    2. Đăng ký thẻ mới
    3. Khách mua hàng (Tích điểm)
    4. Khách dùng điểm (Đổi ưu đãi)
    5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)
    6. Thoát chương trình
    ====================================================== 
    Chọn chức năng (1-6):
    """)

    match choose:
        case "1":
            display_coffee(db_coffee)
        case "2":
            register_card(db_coffee)
        case "3":
            tich_diem(db_coffee)
        case "4":
            change_point(db_coffee)


