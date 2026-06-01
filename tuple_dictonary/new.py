from xml.dom.xmlbuilder import DOMInputSource

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
    choose= input("nhap vao lua chon cua ban: ")
    match choose:
        case "1":
            if len(product_list)==0:
                print(" danh sach san pham dang trong")
                continue
            print("danh sach san pham hien tai: ")
            for index,product in enumerate(product_list,start=1):
                if product["quantity"] ==0:
                    status="het hang"
                elif product["quantity"]<=5:
                    status="sap het hang"
                else:
                    status="con hang"

                print(f"{index} | MA SP {product.get("product_id")} | TEN {product["product_name"]} | GIA { product["price"]} |"
                 f"TON KHO {product["quantity"]:,} | DA BAN {product["sold"]} | DOI TRA {product["returned"]} | GIAM GIA{product["discount"]} | TRANG THAI{status}")
        case "2":
            product_id_new= input("nhap ma san pham: ").strip().upper()
            flag = False
            for i in product_list:
                if i["product_id"] == product_id_new:
                    flag =True
                    while True:
                        slg_new= int(input("nhap sl san pham muon them: "))

                        if slg_new<=0:
                            print("slg k hop le")
                            continue
                        if slg_new> i["quantity"]:
                            print("k dc vuot qua slg ton kho")
                            continue
                        break

                    i["quantity"]-=slg_new
                    i["sold"]+=slg_new
                    slg_giam= i["price"]*(100-i["discount"])/100
                    total= slg_giam*slg_new
                    print(f"TONG TIEN KHASCH CAN THANH TOAN{total}")
        case "3":
            product_id_return= input("nhap ma san pham: ").strip().upper()
            flag= False
            for product in product_list:
                if product["product_id"] == product_id_return:
                    flag =True
                    quantity_return = input("nhap so luong doi tra: ")
                    if not quantity_return.isdigit() or int(quantity_return)<=0:
                        print("slg tra ve k hop le")
                        break
                    if int(quantity_return)> product["sold"] :
                        print("slg tra ve k dc lon hon slg ban")
                        break

                    price_new= product["price"]*(100-product["discount"])/100
                    price_return = price_new *int(quantity_return)
                    product["sold"] -= int(quantity_return)
                    product["quantity"] += int(quantity_return)
                    product["returned"]+=int(quantity_return)
                    print(f"so tien can tra{price_return}")
        case "5":
            ma_sp_new= input("nhap ma san pham moi: ")
            if ma_sp_new.strip()=="":
                print("k dc nhap rong")
            for i in product_list:
                if i["product_id"] == ma_sp_new:
                    slg_the=int(input("nhap slg can them: "))
                    if slg_the<=0:
                        print("phai nhap >0")
                    else:
                        i["quantity"] +=slg_the
            else:
                name_new =input("nhap ten: ")
                slg_new=int(input("nhap slg: "))
                gia_new=int(input("nhao gia:"))
                sold_new=int(input("nhap gia ban: "))
                return_new=int(input("nhap gia tri tra ve"))
                discount_new=int(input("nhap giam gia"))

                product_list.append(
                    {
                        "product_id": ma_sp_new,
                        "product_name": name_new,
                        "price": gia_new,
                        "quantity": slg_new,
                        "sold": sold_new,
                        "returned": return_new,
                        "discount": discount_new
                    }
                )





