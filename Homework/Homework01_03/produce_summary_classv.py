def print_daily_report(filename, day):
    my_day = "Day %d" % day
    actual_print(my_day,False)

    my_file = open(filename)
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0]
        count = words[1]
        amount = words[2]
        
        statement = "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
        actual_print(statement,False)
    my_file.close()
    print "\n",

def actual_print(statement,upper):
    if upper == True:
        print statement.upper()
    else:
        print statement

def main():

    # Day 1
    print_daily_report("um-deliveries-20140519.csv", 1)

    # Day 2
    print_daily_report("um-deliveries-20140520.csv", 2)

    # Day 3
    print_daily_report("um-deliveries-20140521.csv", 3)

if __name__ == "__main__":
    main()