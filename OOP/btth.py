    
from tabulate import tabulate

class Drink:
    def __init__(self,code,name,price):
        self.code=code
        self.name=name
        self.__price=price
        self.is_available=True

    def toggle_available(self):
        self.is_available=not self.is_available

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value<=0:
            raise ValueError("GIA BAN K HOP LE")
        self.__price=value

def display_ds(lst):
    tablet=[]
    for Drink in lst:
        if Drink.is_available== True:
            status='DANG BAN'
        else:
            status="NGUNG BAN"
        tablet.append([Drink.code,Drink.name,Drink.price,status])

    print(tabulate(tablet,headers=["Mã món","Tên món","Giá bán","Trạng thái"],tablefmt="grid"))

def add_drink(lst):
    new_code=input("nhap ma moi: ")
    for i in lst:
        if i.code==new_code:
            print("MA DA BI TRUNG")
            return
    new_name =input("NHAP TEN MOI: ")
    try:
        new_price=input("NHAP GIA MOI: ")
        if float(new_price)<0:
            print("k duoc nhap so am")
            return
        new_drink=Drink(new_code,new_name,new_price)
        lst.append(new_drink)
        print(f"DA THEM THANH CONG MON DO UONG CO MA {new_code}")
    except ValueError:
        print("GIA BAN KHONG HOP LE")


def update_status(lst):
    new_id=input("NHAP MA CAN UPDATE: ")
    for i in lst:
        if i.code==new_id:
            i.toggle_available()
            if i.is_available:
                status="DANG BAN"
            else:
                status="NGUNG BAN"
            print(f"DA CAP NHAT TRANG THAI CHO MON {new_id}")
            print(f"Trạng thái hiện tại: {status}")
            return
    print("K CO MA TRUNG")










menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

while True:
    choose=input("""
    === HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===
    1. Xem danh sách đồ uống
    2. Thêm đồ uống mới
    3. Cập nhật trạng thái kinh doanh
    4. Thoát chương trình
    ==============================================
    Chọn chức năng (1-4):
    """)
    match choose:
        case "1":
            display_ds(menu)
        case "2":
            add_drink(menu)
        case "3":
            update_status(menu)

