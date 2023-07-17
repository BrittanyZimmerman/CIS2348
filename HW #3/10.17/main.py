class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')

    def get_item_total(self):
        return self.item_quantity * self.item_price


if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print(f'Item 1')
    inp1_name = str(input('Enter the item name:\n'))
    inp1_price = int(input('Enter the item price:\n'))
    inp1_quantity = int(input('Enter the item quantity:\n'))
    print()

    item1.item_name = inp1_name
    item1.item_price = inp1_price
    item1.item_quantity = inp1_quantity

    print(f'Item 2')
    inp2_name = str(input('Enter the item name:\n'))
    inp2_price = int(input('Enter the item price:\n'))
    inp2_quantity = int(input('Enter the item quantity:\n'))
    print()

    item2.item_name = inp2_name
    item2.item_price = inp2_price
    item2.item_quantity = inp2_quantity

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    total1 = item1.get_item_total()
    total2 = item2.get_item_total()
    print(f'Total: ${total1 + total2}')
