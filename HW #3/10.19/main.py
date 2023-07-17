class ShoppingCart:

    def __init__(self, name = 'none', date = 'January 1, 2016'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, cart_item):
        self.cart_items.append(cart_item)

    def remove_item(self, item):
        count = 0
        for i in range(len(self.cart_items)):
            if count < 1:
                if self.cart_items[i].item_name == item:
                    self.cart_items.pop(i)
                    count += 1
        if count == 0:
            print(f'Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase, new_quantity):
        count = 0
        for i in range(len(self.cart_items)):
            if count < 1:
                if self.cart_items[i].item_name == ItemToPurchase:
                    self.cart_items[i].item_quantity = new_quantity
                    count += 1
        if count == 0:
            print(f'Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total_count = 0
        for x in self.cart_items:
            total_count += int(x.item_quantity)
        return total_count

    def get_cost_of_cart(self):
        cart_total = 0
        for i in self.cart_items:
            cart_total += int(i.item_quantity) * int(i.item_price)
        return cart_total

    def print_total(self):
        if len(self.cart_items) == 0:
            print(f'SHOPPING CART IS EMPTY')
        else:
            print(self.get_cost_of_cart())

    def print_descriptions(self):
        for x in self.cart_items:
            print(f'{x.item_name}: {x.item_description}')


class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')

    def get_item_total(self):
        return int(self.item_quantity) * int(self.item_price)

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')

if __name__ == "__main__":

    cart1_name = str(input("Enter customer's name:\n"))
    cart1_date = input("Enter today's date:\n")
    print()
    cart1 = ShoppingCart(cart1_name, cart1_date)

    print(f"Customer name: {cart1.customer_name}\nToday's date: {cart1.current_date}\n")

    def print_menu(ShoppingCart):
        user_in = ''
        while user_in != 'q':
            print(f"MENU\na - Add item to cart\nr - Remove item from cart\n"
                  f"c - Change item quantity\ni - Output items' descriptions\n"
                  f"o - Output shopping cart\nq - Quit\n")
            print(f'Choose an option:')
            user_in = str(input())
            while (user_in != 'o') and (user_in != 'a') and (user_in != 'r') and (user_in != 'c') and (user_in != 'i') and (user_in != 'q'):
                print(f'Choose an option:')
                user_in = str(input())
            if user_in == 'o':
                print(f"OUTPUT SHOPPING CART\n{ShoppingCart.customer_name}'s Shopping Cart - {cart1.current_date}")
                print(f'Number of Items: {ShoppingCart.get_num_items_in_cart()}\n')
                if ShoppingCart.get_num_items_in_cart() == 0:
                    print('SHOPPING CART IS EMPTY\n')
                    print('Total: $0\n')
                else:
                    for x in ShoppingCart.cart_items:
                        print(f'{x.item_name} {x.item_quantity} @ ${x.item_price} = ${x.get_item_total()}')
                    print()
                    print(f'Total: ${ShoppingCart.get_cost_of_cart()}\n')
            if user_in == 'i':
                print(f"OUTPUT ITEMS' DESCRIPTIONS\n{ShoppingCart.customer_name}'s Shopping Cart - {cart1.current_date}")
                print()
                print(f'Item Descriptions')
                ShoppingCart.print_descriptions()
                print()
            if user_in == 'a':
                print('ADD ITEM TO CART')
                new_item_N = input('Enter the item name:\n')
                new_desc = input('Enter the item description:\n')
                new_price = input('Enter the item price:\n')
                new_quantity =input('Enter the item quantity:\n')
                print()
                new_item = ItemToPurchase()
                new_item.item_name = new_item_N
                new_item.item_description = new_desc
                new_item.item_price = new_price
                new_item.item_quantity = new_quantity
                ShoppingCart.add_item(new_item)
            if user_in == 'r':
                print('REMOVE ITEM FROM CART')
                rem_item = input('Enter name of item to remove:\n')
                ShoppingCart.remove_item(rem_item)
                print()
            if user_in == 'c':
                print('CHANGE ITEM QUANTITY')
                item_change = input('Enter the item name:\n')
                item_quantity = input ('Enter the new quantity:\n')
                ShoppingCart.modify_item(item_change, item_quantity)
                print()

    print_menu(cart1)