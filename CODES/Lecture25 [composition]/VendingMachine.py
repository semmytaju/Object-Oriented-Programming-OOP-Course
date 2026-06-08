# class 1
class FoodDrinkVendingMachine:
    def __init__(self):
        self.menu = []
        self.payment = 0
    
    def add_menu(self, item, price):
        self.menu.append((item, price))
    
    def display_menu(self):
        print("Pilih menu yang kamu inginkan:")
        for i, (item, price) in enumerate(self.menu):
            print(f"{i+1}. {item} - Rp {price}")
    
    def select_menu(self, choice):
        item, price = self.menu[choice-1]
        print(f"Kamu memilih {item} dengan harga Rp {price}")
        return price
    
    def insert_coin(self, coin):
        self.payment += coin
    
    def checkout(self, price):
        if self.payment >= price:
            change = self.payment - price
            print(f"Pembayaran berhasil. Kembalian kamu adalah Rp {change}")
            self.payment = 0
        else:
            print("Pembayaran tidak cukup. Silahkan masukkan uang lebih.")
    
    def start(self):
        print("Selamat datang di vending machine!")
        self.display_menu()
        choice = int(input("Masukkan nomor menu: "))
        price = self.select_menu(choice)
        coin = int(input("Masukkan uang: "))
        self.insert_coin(coin)
        self.checkout(price)


# class 2
class MenuColdDrink(FoodDrinkVendingMachine):
    def __init__(self):
        super().__init__()
        self.add_menu("Coca Cola", 5000)
        self.add_menu("Fanta", 5000)
        self.add_menu("Sprite", 5000)
        self.add_menu("Aqua", 3000)

# class 3
class MenuHotDrink(FoodDrinkVendingMachine):
    def __init__(self):
        super().__init__()
        self.add_menu("Kopi Panas", 5000)
        self.add_menu("Teh Panas", 3000)
        self.add_menu("Coklat Panas", 7000)

# class 4
class MenuSnackFood(FoodDrinkVendingMachine):
    def __init__(self):
        super().__init__()
        self.add_menu("Chitato", 5000)
        self.add_menu("Oreo", 6000)
        self.add_menu("Kit Kat", 7000)
        self.add_menu("Tango Wafer", 4000)


# switch case with loop and if/else
while True:
    print("Pilih menu vending machine:")
    print("1. Menu minuman dingin")
    print("2. Menu minuman panas")
    print("3. Menu makanan ringan")
    print("0. Exit")
    choice = int(input("Masukkan nomor menu vending machine: "))

    if choice == 0:
        break
    
    if choice == 1:
        machine = MenuColdDrink()
    elif choice == 2:
        machine = MenuHotDrink()
    elif choice == 3:
        machine = MenuSnackFood()
    else:
        print("Pilihan tidak valid.")
        continue
    
    # start vending machine
    machine.start()
    
    
    