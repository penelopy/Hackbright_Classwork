"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_dict


# def print_melon(name, seedless, price):
# 	hashasnot = 'have'
# 	if seedless:
# 		hashasnot = 'do not have'
	
# 	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)



# if __name__ == '__main__':
#     for i in melon_name.keys():
#         print_melon(melon_name[i], melon_seedless[i], melon_price[i])


class Melon:
	def __init__(self, name, price):
		self.name = name 
		self.price = price
		self.has_seeds = True
		self.rind_color = "green"
		self.flesh_color = "red"
		self.average_weight = 5



def main(): 
	melon_list = []
	melon_name_list = melon_dict.keys()

	# for melon in melon_name_list:
	# 	melon = Melon 


if __name__ == '__main__':
	main()

# melon_dict = {"Honeydew": [.99, True], "Crenshaw": [2.00, False], "Crane": [2.50, False], "Casaba": [2.50, False], "Cantaloupe": [.99, False]}

for k, v in melon_dict.iteritems(): 
	# print Melon(k, v[1])
	print k[0], k[1]    


