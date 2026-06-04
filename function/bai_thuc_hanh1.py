inventory_stock = 100
total_revenue = 0.0

def check(num):
    if not num.isdigit():
        return False
    if int(num)<=0:
        return False
    return True


def add_stock():
    print("NHAP HANG")
    amount =input("vui long nhap so hang muon them: ")
    if check(amount) == False:
        print("YEU CAU NHAP SO DUONG VA PHAI LA CHU SO")
    global inventory_stock
    inventory_stock+=int(amount)
    print(f"DA NHAP THANH CONG {amount} SAN PHAM ")
    print(f"TON KHO HIEN TAI {inventory_stock}")

def  process_sale(quantity):
    if int(quantity)>inventory_stock:
        print("KO DU TON KHO")
        return False
    return True

def print_report():
    print(" ---BAO CAO KINH DOANH----")
    global inventory_stock
    global total_revenue
    print(f" TON KHO HIEN TAI: {inventory_stock}")
    print(f"Tổng doanh thu: ${total_revenue}")

def calculate_final_price(quantity, price):
    sum_tam_tinh= quantity * price
    if sum_tam_tinh>= 1000:

        print(f"GIAM GIA : 10% : {sum_tam_tinh*0.1}")
        print(f"THUE VAT 8%: {(sum_tam_tinh-(sum_tam_tinh*0.1)) *0.08} ")
        sum_tam_tinh= ((sum_tam_tinh-(sum_tam_tinh*0.1))) *1.08
    return sum_tam_tinh

def sell_product():
    while True:
        global inventory_stock
        global total_revenue
        quantity= input("NHAP SO LUONG CUA SAN PHAM MUON MUA: ")
        price= input("NHAP DON GIA SAN PHAM $ : ")

        if process_sale(quantity ) == False:
            print(f"KO DU DON HANG TRONG KHO. TON KHAI CHI CON{inventory_stock}")
            break
        else:
            print("HOA DON CHI TIET: ")
            print(f"so luong {quantity} | DON GIA {price}")
            print(f'TAM TINH: ${int(quantity) * int(price)} ')
            tong = calculate_final_price(int(quantity),int(price))
            inventory_stock -= int(quantity)
            total_revenue += tong
            print(f"Tổng thanh toán:{tong}")
            print("DA BAN THANH CONG")
            break



if __name__ == "__main__":
    while True:
        print("""
        ========== TECHSTORE MANAGEMENT SYSTEM ==========
        1. Nhập thêm hàng vào kho
        2. Bán hàng (Tính toán hóa đơn)
        3. Xem báo cáo tổng quan
        4. Thoát chương trình
        =================================================
        """)

        choose =input("Chọn chức năng (1-4): ")
        match choose:
            case "1":
                add_stock()
            case "2":
                sell_product()
            case "3":
                print_report()
            case "4":
                print(" cam on ban da sd chuong trinh ")
                break
            case _:
                print("vui long nhap lua chon tu 1->4")