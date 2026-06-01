product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]
"""
Mỗi sản phẩm được lưu dưới dạng dictionary, bao gồm các thông tin:

        Mã sản phẩm
        Tên sản phẩm
        Giá bán
        Số lượng tồn kho
        Số lượng đã bán
        Số lượng đã đổi trả
        Phần trăm giảm giá hiện tại

"""

while True:
    print("""
    ===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
    1. Hiển thị danh sách sản phẩm
    2. Bán sản phẩm cho khách hàng
    3. Xử lý đổi trả sản phẩm
    4. Áp dụng giảm giá cho sản phẩm
    5. Nhập thêm hàng vào kho cửa hàng
    6. Thoát chương trình
    """)

    choose = input("MOI NHAP LUA CHON: ")
    match choose:
        case "1":
            if len(product_list) == 0:
                print("DANH SACH SAN PHAM DANG TRONG")
            else:

                print(" Danh sách sản phẩm hiện tại: ")
                tonkho=None
                for index,item in enumerate(product_list,start=1):
                    if item.get("quantity") ==0:
                        tonkho="HET HANG"
                    elif item.get("quantity") <=5:
                        tonkho="SAP HET HANG"
                    elif item.get("quantity") >=5:
                        tonkho="CON HANG"
                    print(f"{index}. MA SP: {item.get('product_id')}|"
                          f"TEN: {item.get('product_name')}|"
                          f"GIA: {item.get('price')}"
                          f"TON KHO: : {item.get('quantity')}|"
                          f"DA BAN: {item.get('sold')}|"
                          f"DOI TRA: {item.get('returned')}|"
                          f"GIAM GIA: {item.get('discount')}% |"
                          f"TRANG THAI: {tonkho}"
                          )
        case "2":
            ma_buy= input("NHAP MA SAN PHAM MUON MUA: ").strip().upper()
            flag= None
            for i in product_list:
                if i.get("product_id")==ma_buy:
                    flag=i
                    break
            if flag is None :
                print("SAN PHAM K TON TAI")
                continue
            sl_buy=input("NHAP SO LUONG SAN PHAM MUA: ")
            if int(sl_buy)<=0:
                print("SO LUONG MUA PHAI LA SO NGUYEN DUONG")
                continue
            if int(sl_buy)>flag.get("quantity"):
                print("SO LUONG MUA K DUOC LON HON SO TON KHO")
                continue
            flag["quantity"]-=int(sl_buy)
            flag["sold"]+=int(sl_buy)

            gia_sau_giam=0
            tong_tien=0
            if flag.get("discount")>0:
                gia_sau_giam=flag.get('price')*(100-flag.get('discount'))/100
                tong_tien=gia_sau_giam*int(sl_buy)
                print(f"TONG TIEN: {tong_tien}")
            else:
                print(f"TONG TIEN: {int(sl_buy)*flag.get('price')}")

        case "3":
            ma_tra= input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()
            flag_1=None
            for i in product_list:
                if i.get("product_id")==ma_tra:
                    flag_1=i
                    break
            if flag_1 is None:
                print("MA SAN PHAM K TON TAI")
                continue
            slg_doitra=input("NHAP SO LUONG DOI TRA: ")
            if int(slg_doitra)<=0:
                print("SO LG PHAI LA SO DUONG")
                continue
            if int(slg_doitra)>flag_1.get("sold"):
                print("SO LG DOI TRA K DUOC QUA SLG DA BAN")
                continue
            flag_1["sold"]-=int(slg_doitra)
            flag_1["quantity"]+=int(slg_doitra)
            flag_1["returned"]+=int(slg_doitra)
            gia_sau_giam= flag_1.get("price") *(100-flag_1.get("discount"))/100
            print(f"SO TIEN HOAN LAI SAU GIAM GIA: {gia_sau_giam*int(slg_doitra)}")

        case "4":
            ma_giam=input("Nhập mã sản phẩm cần áp dụng giảm giá:").strip().upper()
            flag_2=None
            for i in product_list:
                if i.get("product_id")==ma_giam:
                    flag_2=i
                    break
            if flag_2 is None:
                print("MA SAN PHAM K TON TAI")
                continue
            phantram_giam= input("NHAP % GIAM GIA")
            if not phantram_giam.isdigit() or int(phantram_giam)<0:
                print("khong dc la so am hoac chu so")
                continue
            if 0<=int(phantram_giam)<=70:
                flag_2["discount"]=int(phantram_giam)

        case "5":
            ma_add= input("Nhap ma sp can nhap them").strip().upper()
            flag_3=None
            for i in product_list:
                if i.get("product_id")==ma_add:
                    flag_3=i
                    break
            if flag_3 is None:
                print("MA SAN PHAM K TON TAI")
                continue
            slg_add=input("NHAP SO LUONG can them: ")
            if int(slg_add)<=0:
                print("YEU CAU NHAP SO NGUYEN DUONG")
                continue
            flag_3["quantity"]+=int(slg_add)
            print("DA CONG VAO TON KHO THANH CONG")

        case "6":
            print("CAM ON BAN DA SU DUNG CHUONG TRINH")
            break
        case _:
            print("VUI LONG NHAP LUA CHON TU 1->6")
            continue




