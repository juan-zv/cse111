from datetime import datetime

# print(f"{datetime.now()}")

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

subtotal = round(float(input("Please enter the subtotal: ")), 2)

total = 0

if day_of_week == 1:
    if subtotal >= 50:
        total = round((subtotal - subtotal * 0.10 + subtotal * 0.06), 2)
        discount_amount = subtotal * 0.10
        total_sales_amount = subtotal * 0.06

        print(f"Discount amount: {round((subtotal * 0.10), 2)}")
        print(f"Total sales amount: {round(total_sales_amount, 2)}")
        print(f"Total: {total}")
    else:
        total = subtotal + subtotal * 0.06
        print(f"Total sales amount: {subtotal * 0.06}")
        print(f"Total: {total}")
elif day_of_week == 2:
    if subtotal >= 50:
        total = subtotal - subtotal * 0.10 + subtotal * 0.06
        print(f"Discount amount: {subtotal * 0.10}")
        print(f"Total sales amount: {subtotal * 0.06}")
        print(f"Total: {total}")
    else:
        total = subtotal + subtotal * 0.06
        print(f"Total sales amount: {subtotal * 0.06}")
        print(f"Total: {total}")