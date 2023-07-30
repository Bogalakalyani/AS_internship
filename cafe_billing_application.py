class Items:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def update_item(self):
        question = input("Which attribute would you like to update? 1) name, 2) price, 3) type: ")
        if question.lower() == "name":
            old_name = input("Enter the current name of the item: ")
            new_name = input("Enter the new name for the item: ")
            self.update_name(old_name, new_name)
        elif question.lower() == "price":
            item_name = input("Enter the name of the item: ")
            new_price = float(input("Enter the new price for the item: "))
            self.update_price(item_name, new_price)
        elif question.lower() == "type":
            item_name = input("Enter the name of the item: ")
            new_type = input("Enter the new type for the item: ")
            self.update_type(item_name, new_type)
        else:
            print("Please choose one of the above three options.")
    
    def update_name(self, old_name, new_name):
        for item in self.items:
            if item.name == old_name:
                item.name = new_name
                break
    
    def update_price(self, name, new_price):
        for item in self.items:
            if item.name == name:
                item.price = new_price
                break
    
    def update_type(self, name, new_type):
        for item in self.items:
            if item.name == name:
                item.type = new_type
                break
    
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                break

class OrderItem:
    def __init__(self, menu_item, quantity, customization):
        self.menu_item = menu_item
        self.quantity = quantity
        self.customization = customization

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity, customization):
        item = OrderItem(menu_item, quantity, customization)
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.menu_item.name == name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for order_item in self.items:
            total += order_item.menu_item.price * order_item.quantity
        return total

class BillPayment:

    def apply_discount(self, discount_percentage,total):
        discount_amount = total * (discount_percentage / 100)
        discounted_total = total - discount_amount
        return discounted_total

    def apply_tax(self, tax_rate,total):
        tax_amount = total * (tax_rate / 100)
        total_with_tax = total + tax_amount
        return total_with_tax

    def apply_service_charge(self, service_charge_rate,total):
        service_charge_amount = total * (service_charge_rate / 100)
        total_with_service_charge = total + service_charge_amount
        return total_with_service_charge


item1 = Items("coffee", 100)
item2 = Items("bread", 150)
item3 = Items("tea", 30)
item4 = Items("pan cakes",50)

menu = Menu()
menu.add_item(item1)
menu.add_item(item2)
menu.add_item(item3)
menu.add_item(item4)
menu.remove_item("coffee")

print("<--------Today menu items are--------->")
m = []
for item in menu.items:
    m.append(item.name)
    print(item.name)
print()

order = Order()
while True:
    user_order = input(f"Can you please tell me your order from the above menu: ").lower()
    if user_order in m:
        quantity = int(input("can you please tell me quantity: "))
        customization =input("can you tell me your customization: ")
        for item in menu.items:
            if item.name == user_order:
                order.add_item(item, quantity, customization)
        q = input("Do you want to order more: ")
        if q.lower() == "no":
            break
    else:
        print("please order the items that are in the menu")

print('These are the items you ordered:')
for order_item in order.items:
    print(f"You ordered {order_item.quantity} {order_item.menu_item.name}")

total_bill = order.calculate_total()

bill_payment = BillPayment()


ammount = bill_payment.apply_discount(0,total_bill)

tax =input('Sir,Do you want me to add tax to your bill: ')
if tax.lower() == "yes":
    ammount = bill_payment.apply_tax(10,ammount)

service_charge=input('Sir,Do you want me to add service charges to your bill: ')
if service_charge.lower() == "yes":
    ammount = bill_payment.apply_service_charge(0.5,ammount)


print(f"Your total bill is {ammount}")




