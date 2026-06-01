"""
Mã sản phẩm
Tên sản phẩm
Giá bán
Số lượng tồn kho
Số lượng đã bán


"""


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("""
    ===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
    1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
    2. Bán sản phẩm cho khách hàng
    3. Nhập thêm hàng vào kho
    4. Xem báo cáo doanh thu
    5. Thoát chương trình
    
    """)

    choose= input("Moi ban chon cac chuc nang tu 1->5")
    match choose:
        case "1":
            ton_kho=""
            if len(product_list) ==0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại: ")
                for index, item in enumerate(product_list):
                    if item.get("quantity")==0:
                        ton_kho="het hang"
                    elif item.get("quantity")<=5:
                        ton_kho="sap het hang"
                    else:
                        ton_kho="con hang"
                    print(
                        f"{index}. MA SP:{item.get('product_id')} | Ten: {item.get("product_name")} | GIA: {item.get('price')} | "
                        f"TON KHO: {item.get('quantity')} | DA BAN: {item.get('sold')} | TRANG THAI{ton_kho}")

        case "2":
            id_sp= input("NHAP MA SAN PHAM MUON MUA: ").strip().upper()
            flag= None

            for i in product_list:
                if id_sp==i["product_id"]:
                    flag=i
                    break
            if flag  is None:
                print("KHONG TIM THAY SAN PHAM")
                continue
            quantity_buy= input("NHAP SO LUONG CAN MUA")
            if int(quantity_buy)<=0:
                print("YEU CAU NHAP SO NGUYEN DUONG")
                continue
            if int(quantity_buy)>flag.get("quantity"):
                print(" SL MUA VUOT QUA TON KHO")
                continue
            flag["quantity"]-=int(quantity_buy)
            flag["sold"]+=int(quantity_buy)
            print(f"SO TIEN KHACH CAN THANH TOAN LA: {flag.get("price") * int(quantity_buy) }")

        case "3":
            ma_add= input("NHAP MA SAN PHAM MUON THEM: ").strip().upper()
            flag_1= None
            for i in product_list:
                if ma_add==i["product_id"]:
                    flag_1=i
                    break
            if flag_1 is None:
                print("MA K TON TAI")
                continue
            sl_them=input("MOI BAN NHAP SO LUONG MUON THEM:")
            if int(sl_them)<=0:
                print("VUI LONG NHAP 1 SO NGUYEN DUONG")
                continue
            flag_1["quantity"]+=int(sl_them)

        case "4":
            print("BAO CAO DOANH THU CUA HANG YODY")
            sum_0=0
            sum_1=0
            max=0
            flag=None
            for index,item in enumerate(product_list,start=1):
                sum_0=item.get("price")*item.get("sold")
                print(f"{index}. {item.get('product_name')} |  DA BAN: {item.get('sold')} | DOANH THU {sum_0}")
                sum_1+=sum_0
                if sum_0>max:
                    max=sum_0
                    flag=item.get("product_name")
            print(f"TONG DOANH THU {sum_1}")
            print(f"SAN PHAM BAN CHAY NHAT {flag}")







        case "5":
            print("CAM ON BAN DA SD CHUONG TRINH")
            break
        case _:
            print("VUI LONG NHAP CAC LUA CHON TU 1->5")

