def print_daily_totals(day, csv_file): 
    print day
    my_file = open(csv_file) 

    for line in my_file:
        print line
        line = line.rstrip()
        words = line.split(',')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)

    my_file.close()
    print "\n",



def main():

    print_daily_totals("Day 1", "um-deliveries-20140519.csv")
    print_daily_totals("Day 2", "um-deliveries-20140520.csv")
    print_daily_totals("Day 3", "um-deliveries-20140521.csv")

if __name__ == "__main__":
    main()