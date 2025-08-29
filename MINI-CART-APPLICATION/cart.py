def cartApplication(cart):
    if not cart:
        print("The cart is already empty!")
    else:
        print("Shopping cart:")
    total=0
    for item in cart:
        print(f"{item['name']} : ${item['price']}")
        total+=item['price']
    print(f"Total : ${total:.2f}")
def main():
    cart=[]
    while True:
        print("\n Shopping Application :")
        print("1.Add to cart item")
        print("2.View cart")
        print("3.Remove item from cart")
        print("4.Exit")
        choose=input("Enter your choice to perform :")
        if choose=='1':
            item_name=input("Enter your item name :")
            item_price=float(input("Enter the price :"))
            item={'name':item_name,'price':item_price}
            cart.append(item)
            print("Item added to the cart")
        elif choose=='2':
            cartApplication(cart)
        elif choose=='3':
            if not cart:
                print("The cart is already empty")
            else:
                cartApplication(cart)
                item_index=int(input("Enter the item number for removing:")) -1
                if 0<=item_index<len(cart):
                    remove=cart.pop(item_index)
                    print(f"Removed item:{remove['name']}")
                else:
                    print("Invalid input number.")
        elif choose=='4':
            print("Exit from the cart application")
            break
        else:
            print("Invalid number, please try again.")
if __name__=="__main__":
    main()