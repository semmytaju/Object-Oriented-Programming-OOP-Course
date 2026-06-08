# class 1
class Restaurant:
    # constructor without parameters
    def __init__(self):
        self.menu = {
            "Nasi Goreng": 15000,
            "Mie Goreng": 12000,
            "Nasi Padang": 25000,
            "Ayam Goreng": 18000,
            "Soto Ayam": 20000
        }
        self.order_list = []
        self.total_price = 0
    
    # fungsi menampilkan menu restoran
    def show_menu(self):
        print("Menu:")
        for item in self.menu:
            print("(Rp. {0}) {1}".format(self.menu[item], item))
    
    # fungsi order menu restoran
    def order(self, item, qty):
        if item in self.menu:
            price = self.menu[item] * qty
            self.order_list.append((item, qty, price))
            self.total_price += price
            print(qty, item, "added to order.")
        else:
            print(item, "not found in menu.")
    
    # fungsi menghadle proses pembayaran
    def buy(self):
        if len(self.order_list) > 0:
            print("Order Summary:")
            for order in self.order_list:
                print(order[1], order[0], "[ Rp.", order[2], "]")
            print("Total Price:", "Rp. ", self.total_price)
            self.order_list = []
            self.total_price = 0
        else:
            print("No order placed.")

# class 2
class McDonaldRestaurant(Restaurant):
    # constructor with parameters
    def __init__(self):
        super().__init__() # call parrent class constructor
        self.menu.update({
            "Burger": 20000,
            "Hotdog": 15000,
            "French Fries": 10000,
            "Fried Chicken": 25000,
            "Pizza": 30000
        })

# create object
restaurant = McDonaldRestaurant()

# loop while untuk menampilkan menu
while True:
    print("\nWelcome to Semmy Restaurant:")
    print("1. Show Menu")
    print("2. Order")
    print("3. Buy")
    print("4. Exit")
    
    # switch case (if-elif-else statement)
    choice = int(input("Enter menu number: "))
    # menu 1
    if choice == 1:
        restaurant.show_menu()
    # menu 2
    elif choice == 2:
        selected_item = input("Enter item name (mau pesan apa): ")
        num_item = int(input("Enter quantity (berapa banyak): "))
        restaurant.order(selected_item, num_item)
    # menu 3
    elif choice == 3:
        restaurant.buy()
    # menu 4
    elif choice == 4:
        break
    else:
        print("Sorry, the number is not in the menu.")
        
        