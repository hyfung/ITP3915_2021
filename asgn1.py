#!/usr/bin/python3
import sys

COFFEE_NAME_AND_PRICES = (("Cappuccino", 25), ("Espresso", 20), ("Latte", 15), ("Mocha", 30))
INDEX_COFFEE_NAME = 0
INDEX_COFFEE_PRICE = 1
LARGE_CUP_PRICE = 5
COLD_PRICE = 3

INDEX_COFFEE_NO = 0
INDEX_QUANTITY = 1
INDEX_LARGE_CUP = 2
INDEX_COLD = 3

def compute_sales(coffee_no: int, quantity: int, large_cup: str, cold: str) -> int:
    coffee_price = COFFEE_NAME_AND_PRICES[coffee_no][INDEX_COFFEE_PRICE]

    if large_cup == 'Y':
        coffee_price += LARGE_CUP_PRICE

    if cold == 'Y':
        coffee_price += COLD_PRICE

    return coffee_price * quantity

def main():
    global_sales_list = [] #List of current_sales_list
    current_sales_list = []
    cups_of_coffee_sold = {
        "Cappuccino": 0,
        "Espresso": 0,
        "Latte": 0,
        "Mocha": 0,
    }

    total_number_sales = 0
    highest_sales_amount = 0
    lowest_sales_amount = sys.maxsize
    total_sales_amount = 0

    print("Welcome to coffe shop")

    while True:
        print("Coffee Shop Menu:")
        print("No. | Coffee Type | Price")
        print("0   | Cappuccino  | $25")
        print("1   | Espresso    | $20")
        print("2   | Latte       | $15")
        print("3   | Mocha       | $30")

        total_amt = 0
        choice = input("Please input your choice. Press \"Enter\" to confirm order (0 – 3): ")
        if choice != '':
            #Adding orders to current sale
            choice = int(choice)
            quantity = int(input("Please input quantity: "))
            large = input("Large Cup required? +$5.00 (Y / N): ")
            cold = input("Cold required? +$3.00 (Y / N): ")
            print("")

            current_sales_list.append((choice, quantity, large, cold))

        print("Current Order Summary:")
        for item in current_sales_list:
            if item[INDEX_LARGE_CUP] == 'Y' and item[INDEX_COLD] == 'Y':
                #Large and cold
                print(str(COFFEE_NAME_AND_PRICES[item[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]) + " (Cold,Large): " + str(quantity), end = "")
            elif item[INDEX_LARGE_CUP] == 'Y':
                #Large
                print(str(COFFEE_NAME_AND_PRICES[item[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]) + " (Large): " + str(quantity), end = "")
            elif item[INDEX_COLD] == 'Y':
                #Cold
                print(str(COFFEE_NAME_AND_PRICES[item[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]) + " (Cold): " + str(quantity), end = "")
            else:
                print(str(COFFEE_NAME_AND_PRICES[item[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]) + ": " + str(quantity), end = "")

            print(": $%d" % compute_sales(item[0], item[1], item[2], item[3]))
            total_amt += compute_sales(item[0], item[1], item[2], item[3])

        print("Total: $%d" % total_amt)

        if choice == '':
            #Finishing current order and calculate stats
            for item in current_sales_list:
                cups_of_coffee_sold[COFFEE_NAME_AND_PRICES[item[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]] += item[1]

            global_sales_list.append(current_sales_list)
            current_sales_list = []

            sale_avg = 0
            for sale in global_sales_list:
                sale_total = 0
                for item in sale:
                    sale_total += compute_sales(item[0], item[1], item[2], item[3])
                highest_sales_amount = max(sale_total, highest_sales_amount)
                lowest_sales_amount = min(sale_total, lowest_sales_amount)
                sale_avg += sale_total

            sale_avg /= len(global_sales_list)                


            print("Statistics of Coffee Shop:")
            print("Total number sales = %d" % len(global_sales_list))
            print("Lowest Sales Amount = $%d" % lowest_sales_amount)
            print("Highest Sales Amount = $%d" % highest_sales_amount)
            print("Average Sales Amount = $%.1f" % sale_avg)

            print("List of number of cups coffee sold:")
            if cups_of_coffee_sold['Cappuccino'] > 0:
                print("\tCappuccino: %d" % cups_of_coffee_sold['Cappuccino'])
            if cups_of_coffee_sold['Espresso'] > 0:
                print("\tEspresso: %d" % cups_of_coffee_sold['Espresso'])
            if cups_of_coffee_sold['Latte'] > 0:
                print("\tLatte: %d" % cups_of_coffee_sold['Latte'])
            if cups_of_coffee_sold['Mocha'] > 0:
                print("\tMocha: %d" % cups_of_coffee_sold['Mocha'])
            print("")

if __name__ == '__main__':
    main()
