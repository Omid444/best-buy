import products
import store
import sys


product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    """Printing menu"""
    menu =   "  Store Menu\n"\
             "  ----------\n"\
             "1. List all products in store\n"\
             "2. Show total amount in store\n"\
             "3. Make an order\n"\
             "4. Quit"
    print(menu)


def show_all_list_store(active_products):
    """Print all products and their quantities"""
    count = 1
    for product in active_products:
        print(f"{count}.{product.name},Price: {product.price}, Quantity: {product.quantity} ")
        count += 1

def show_all_amount_store(active_products):
    """Print how many item exist in store overally"""
    total_items = 0
    for product in active_products:
        total_items += product.price
    print(f"Total of {total_items} items in store")


def make_order(active_product):
    """Taking order from customer and calculate and print total payment"""
    shopping_list = []
    total_payment = 0
    while True:
        print("When you want to finish order, enter empty text.")
        customer_order = input("Which product # do you want? (number of product in list)")
        amount = input("What amount do you want?")

        if not (customer_order and amount):
            if shopping_list:
                total_payment += best_buy.order(shopping_list)
                print(f"Order made! Total payment: {total_payment}")
                break
            else:
                break
        if customer_order.isdigit() and int(customer_order) <= len(active_product)-1:
            try:
                shopping_list.append((active_product[int(customer_order)-1], int(amount)))
            except ValueError as e:
                print(e)
        else:
            print("Both list number and amount number must be entered correctly")


def exit_program(active_product):
    print("program closed")
    sys.exit()


def control_menu(active_product):
    menu_numb = input("Please select a number:")
    menu_dict = {1:show_all_list_store, 2:show_all_amount_store, 3:make_order, 4:exit_program}

    try:
        menu_numb = int(menu_numb)
        if 0 < menu_numb <= len(menu_dict):
            menu_dict[menu_numb](active_product)
        else:
            print("please enter valid number form 1 to 4")
    except ValueError:
        print("string is not allowed please enter number from 1 to 4")


def main():
    while True:
        start()
        active_product = best_buy.get_all_products()
        control_menu(active_product)


if __name__ == "__main__":
    main()