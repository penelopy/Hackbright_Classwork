# melon_name = {
#     1: "Honeydew",
#     2: "Crenshaw",
#     3: "Crane",
#     4: "Casaba",
#     5: "Cantaloupe",
# }

# melon_price = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedless = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,
# }


melon_dict = {"Honeydew": [.99, True], "Crenshaw": [2.00, False], "Crane": [2.50, False], "Casaba": [2.50, False], "Cantaloupe": [.99, False]}

for k, v in melon_dict.iteritems(): 
    print v[1]