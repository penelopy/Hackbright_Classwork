# Things you should be able to do.
#10/3/14 completed in 28 minutes with champange party happening simulataneously

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for num in number_list: 
        if num % 2 != 0: 
            new_list.append(num)

    return new_list
# all_odd(number_list)


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for num in number_list: 
        if num % 2 == 0: 
            new_list.append(num)

    print new_list
# all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list: 
        if len(word) >= 4: 
            new_list.append(word)
    return new_list
# long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    lowest_num = 0
    for num in number_list: 
        if lowest_num > num: 
            lowest_num = num

    return lowest_num
# smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest_num = 0
    for num in number_list: 
        if largest_num < num: 
            largest_num = num

    return largest_num
# largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    half_list = []
    for num in number_list: 
        half_num = num /2.0
        half_list.append(half_num)
    return half_list
# halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list: 
        word_length = len(word)
        new_list.append(word_length)

    return new_list
word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    the_sum = 0
    for num in number_list: 
        the_sum += num 
    return the_sum
# sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = 1
    for num in number_list: 
        total *= num 
    return total
# mult_numbers(number_list)    

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ""
    for word in word_list: 
        new_string += word 
    return new_string
# join_strings(word_list)    

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    the_average = 0.0
    the_sum = 0.0
    for num in number_list: 
        the_sum += num 
    the_average = the_sum / len(number_list)

    # return the_average
    print the_average

average(number_list)    