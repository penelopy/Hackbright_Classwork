# Things you should be able to do.
#10/11/14 tried using map, filter, reduce

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd():
    return list(filter ((lambda(x): x % 2 != 0), number_list))
# print all_odd()

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    return list(filter ( (lambda(x): x % 2 == 0), some_list) )
# print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return list(filter (lambda(x): len(x) >= 4, word_list)) 
# print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return reduce (lambda x, y: x if (x < y) else y, some_list)
# print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return reduce (lambda x, y: x if (x > y) else y, some_list)
# print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return list( map (lambda(x): x / 2.0, some_list))
# print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    return map(lambda(x): len(x), word_list)
# print word_lenths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return reduce (lambda x, y: x + y, numbers)
# print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return reduce( lambda x, y: x * y, numbers)
# print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return reduce (lambda x, y: x + "" + y, word_list)
# print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return sum_numbers(number_list)/float(len(numbers))
print average(number_list)
