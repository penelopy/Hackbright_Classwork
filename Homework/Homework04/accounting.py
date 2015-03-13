# def customer_data():

    # for item in customer_list: 
    

    # customer1_name = "Joe"
    # customer1_melons = 5
    # customer1_paid = 5.00

    # customer2_name = "Frank"
    # customer2_melons = 6
    # customer2_paid = 6.00

    # customer3_name = "Sally"
    # customer3_melons = 3
    # customer3_paid = 3.00

    # customer4_name = "Sean"
    # customer4_melons = 9
    # customer4_paid = 9.50

    # customer5_name = "David"
    # customer5_melons = 4
    # customer5_paid = 4.00

    # customer6_name = "Ashley"
    # customer6_melons = 3
    # customer6_paid = 2.00

   
def check_for_underpayment():

    melon_cost = 1.00


    customer_file = open("customer_orders.csv")
    for line in customer_file:
        line = line.rstrip()
        words = line.split(',')

        customer_num = words[0]
        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])

        customer_expected = customer_melons * melon_cost
        if customer_expected != customer_paid:
            print customer_name, "paid %.2f, expected %.2f"%(customer_paid, customer_expected)
            print "********************"

def main():


 check_for_underpayment()



if __name__ == "__main__":
    main()