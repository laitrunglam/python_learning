blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]
def display_inventory(inventory):
    if len(inventory)==0:
        print("k co mau nao")
    else:
        print("""
        --- DANH SÁCH KHO MÁU ---
        Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn    
        """ )
        tong=0
        for i in inventory:
            x=i.split("-")
            if len(x) == 5:
                ma,ten,nhom_mau,the_tich,ngay=x
            else:
                ma=x[0]
                ten=x[1]
                nhom_mau=x[2]+"-"
                the_tich=x[4]
                ngay=x[5]
            tong+=int(the_tich)
            print(f"{ma} | {ten} | {nhom_mau} | {the_tich}ml | {ngay}")
        print(f"TONG THE TICH MAU TRONG KHO {tong}ml")


def add_blood_bag(inventory):
    while True:
        ma=input("yeu cau nguoi dung nhap ma: ").upper().strip()
        if ma == "":
            print("vui long k de trong ma tui mau: ")
            continue
        flag=0
        for i in inventory:
            x=i.split("-")
            if ma==x[0]:
                flag=1
                break
        if flag==1:
            print("ma da trung vui long nhap lai ")
            continue


        while True:
            name = input("yeu cau nhap ten moi : ").title()
            if name == "":
                print("vui long k de trong ten nguoi nhap: ")
                continue
            break
        nhom_mau = input("yeu cau nhap nhom mau: ").strip().upper()
        while True:
            the_tich = input("yeu cau nhap the tich: ")
            if not the_tich.isdigit() or int(the_tich) <= 0:
                print("the tich phai la so")
                continue
            break

        date_hh = input("yeu cau nhap ngay het han: ")
        inventory.append("-".join([ma, name, nhom_mau, the_tich, date_hh]))
        print(f"THANH CONG DA NHAP TUI MAU {ma} VAO KHO")
        print(f"SAU KHI CHUAN HOA DU LIEU DC DUA VAO list LA :"
              f"{inventory[3]}")
        break




def update_expiry(inventory):
    while True:
        ma= input("nhap ma tui can sua?").strip().upper()
        if ma=="":
            print("ma rong yeu cau nhap lai")
            continue
        flag=None
        for i in inventory:
            x=i.split("-")
            if x[0]==ma:
                flag=i
                break
        if flag is None:
            print(" k ton tai ma tui yeu cau nhap lai ")
            continue
        date_new=input("nhap ngay moi: ")
        new_lst=flag.split("-")
        new_lst[-1]=date_new
        index=inventory.index(flag)
        inventory[index]="-".join(new_lst)
        print("da thanh cong cap nhat het han cho tui mau !!!")
        break

def remove_blood_bag(inventory):
    while True:
        ma=input("nhap ma : ").strip().upper()
        if ma == "":
            print("k dc de ma rong")
            continue
        flag=None
        for i in inventory:
            x=i.split("-")
            if x[0]==ma:
                inventory.remove(i)
                flag=1
                print(f"da xoa {ma} ra khoi ds")
                break
        if flag is None:
            print("ma k ton tai vui long nhap lai ")
            continue
        break






def main():
    while True:
        print("""
        === HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===
        1. Xem danh sách túi máu trong kho
        2. Nhập túi máu mới
        3. Gia hạn / Sửa ngày hết hạn
        4. Xuất / Hủy túi máu
        5. Thoát chương trình 
        """)
        choose=input("NHAP CAC SO TU 1->5: ")
        match choose:
            case "1":
                display_inventory(blood_inventory)
            case "2":
                add_blood_bag(blood_inventory)
            case "3":
                update_expiry(blood_inventory)
            case "4":
                remove_blood_bag(blood_inventory)

main()
