# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    newlist = []
    for num in number_list:
        if num % 2 != 0:
            newlist.append(num)
    return newlist

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    newlist = []
    for num in number_list:
        if num % 2 == 0:
            newlist.append(num)
    return newlist

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    newlist = []
    for word in word_list:
        if len(word) >= 4:
            newlist.append(word)
    return newlist

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    min = number_list[0]
    for num in number_list:
        if num < min:
            min = num
    return min

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    max = number_list[0]
    for num in number_list:
        if num > max:
            max = num
    return max

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    newlist = []
    for num in number_list:
        newlist.append(num/2.0)
    return newlist

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    newlist = []
    for word in word_list:
        newlist.append(len(word))
    return newlist

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum = 0
    for num in number_list:
        sum += num
    return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    product = 1
    for num in number_list:
        product *= num
    return product

# Write a function that joins all the strings in a list together (without using the join method) and 
# returns a single string.
def join_strings(word_list):
    newstring = ""
    for word in word_list:
        newstring += word
    return newstring

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list) / float(len(number_list))