import random

def main():

    print(f"numbers {append_random_numbers(4)}")





def append_random_numbers(quantity):
    numbers = []

    for random_num in range(quantity):
        
        random_num = round(random.uniform(0, 100), 1)
        numbers.append(random_num)

    return numbers

main()