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
    choose = input("nhap tu 1->6: ")
    match choose:
        case "1":
            if len(product_list) == 0:
                print(" danh sasch rong ")
            else:
                print("danh sach san pham hien tai: ")
                for index,value in enumerate(product_list,start=1):
                    if value["quantity"] ==0:
                        status ="het hang"
                    elif value["quantity"]<=5:
                        status ="het hang"
                    else:
                        status= "con hang"
                    print(f"{index}. MA SP {value["product_id"]} | TEN {value["product_name"]} |"
                          f"gia {value["price"]} | TON KHO {value["quantity"]} | DA BAN {value["sold"]}"
                          f"DOI TRA {value["returned"]} | giam gia: {value["discount"]} | TRANG THAI{status} " )
        case "2":
            ma_new=input("nhap ma san phaM: ")
            flag=None
            for item in product_list:
                if item["product_id"] ==ma_new:
                    flag=item
                    break
            if flag is None:
                print("k tim thay san pham")
            slg_new=input("nhap slg san pham")

            if not slg_new.isdigit() or int(slg_new)<0 :
                print("slg mua k hop le")
            if int(slg_new)>flag.get("quantity"):
                print("so lg lon hon ton kho")
            flag["quantity"]-=int(slg_new)
            flag["sold"] += int(slg_new)
            gia_sau_giam=flag["price"] *(100-flag["discount"])/100
            print(f"tong tien{gia_sau_giam* int(slg_new)}")

        case "3":
            ma_new=input("nhap ma sp").strip().upper()
            flag_1 =None
            for item in product_list:
                if item["product_id"] == ma_new:
                    flag_1=item
                    break
            if flag_1 is None:
                print("ko tim thay ma san pham")
            new_slg= input("nhap slg doi tra: ")

            if not new_slg.isdigit() :
                print("slg nhap ko hop le")
            if int(new_slg)>flag_1["sold"]:
                print("slg k dc qua slg da ban")

            flag_1["sold"]-=int(new_slg)
            flag_1["quantity"] +=int(new_slg)
            flag_1["returned"] +=int(new_slg)

            price_new= flag_1.get("price")*(100-flag_1.get("discount"))/100
            print(f"SO TIEN SAU GIAM GIA {price_new * int(new_slg)}")

        case "4":
            ma_new = input("nhap ma san pham moi").strip().upper()
            flag=None
            for item in product_list:
                if ma_new==item["product_id"]:
                    flag=item
                    break
            if flag is None:
                name_new =input("nhap ten san pham moi")
                price_new= int(input("nhap gia tien moi"))
                slg_new = int(input("nhap slg moi"))
                sold_new= int(input("nhap so lg da ban"))
                return_new= int(input("nhap so lg tra ve"))
                discount_new=int(input("nhap % giam gia"))
                product_list.append({

                    "product_id": ma_new,
                    "product_name": name_new,
                    "price": price_new,
                    "quantity": slg_new,
                    "sold": sold_new,
                    "returned": return_new,
                    "discount": discount_new
                })
            else:
                slg_moi= input("nhap so luong san pham them")
                if not slg_moi.isdigit():
                    print("so k dc nho hon 0")
                flag["quantity"]+=int(slg_moi)
