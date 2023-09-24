total_price = 0

while True:
    try:
        quantity = int(input("Number of items: "))
        if quantity == 0:
            break
        price = float(input("Price of item: "))

        subtotal = quantity * price

        # Add the subtotal to the total price
        total_price += subtotal
        if total_price > 100:
           total_price *= 0.9

        print("Total price: ${:.2f}".format(total_price))
    except ValueError:
        print("Please enter a valid quantity and price.")