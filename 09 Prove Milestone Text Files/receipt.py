import csv
from datetime import datetime

current_date_and_time = datetime.now()

INDEX_FOR_PRODUCTS = 0

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}            

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            products_dict[key] = row_list

    return products_dict

            


def main():

    #file = input("What is the file you want to open? ")

    products_dict = read_dict("products.csv", INDEX_FOR_PRODUCTS)

    #print("All Products")
    #print(products_dict)
    print("Inkom Emporium")
    print()
    print("Requested Items")

    try:
        filename = "request.csv"
        with open(filename, "rt") as request_file:
            reader = csv.reader(request_file)

            next(reader)

            subtotal = 0
            num_items = 0


            for row_list in reader:
                if row_list[0] in products_dict:
                    product = products_dict[row_list[0]][1]
                    quantity = row_list[1]
                    price = products_dict[row_list[0]][2]

                    subtotal = subtotal + (float(quantity) * float(price))

                    print(f"{product}: {quantity} @ {price}")

                    num_items = num_items + int(quantity)

                else:
                    print(f"Error: unknown product ID in the request.csv file '{row_list[0]}'")

    except FileNotFoundError as Error:
        print()
        print()
        print(f"ERROR: No such file or directory: '{filename}'")
        print()
        print()

    salestax = subtotal * 0.06
    total = subtotal + salestax
    print()
    print(f"Number of Items: {num_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {salestax:.2f}")
    print(f"Total: {total:.2f}")

    #If it is Tuesday or Wednesday -10%
    if (datetime.today().weekday() == 1) or (datetime.today().weekday() == 2):
        print()
        print("Discount:")
        print(f"Total: {(total - total * 0.10):.2f}")
    

    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%a %b  %d %H:%M:%S %Y}")



if __name__ == "__main__":
    main()