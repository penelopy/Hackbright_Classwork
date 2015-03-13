

filename = open("scores.txt")

####################
# Using an empty list

# rest_listing = []

# for line in filename:
#     rest_data = line.strip()
#     rest_listing.append(rest_data)

# rest_listing.sort()

# for pair in rest_listing: 
#     name, rating = pair.split(":")
#     print "Restaurant %s is rated at %s" %(name, rating) 


###################
#Using an empty dictionary

rest_dict = {}
rating_dict = {}

for line in filename: 
    rest_data = line.strip()
    name, rating = rest_data.split(":")
    rest_dict[name] = int(rating)
    rating_dict.setdefault(int(rating), []).append(name)

print "***********************"
print "Numerically sorted ratings:"
for rating, restaurants in sorted(rating_dict.items()):
    for restaurant in sorted(restaurants): # alphabetize within rating
        print "Restaurant %s is rated at %s" % (restaurant, rating) 

print "***********************"
print "Numerically sorted highest-lowest using 2nd tuple item:"
# sorts items numerically first by 2nd tuple item, then alphabetically 
# using -x[1] tells it to sort by highest to lowest
sorted_tuple_list = sorted(rest_dict.items(), key=lambda x: (-x[1], x[0]))
for restaurant, rating in sorted_tuple_list:
    print "Restaurant %s is rated at %s" % (restaurant, rating) 

print "***********************"
print "Alphabetized restaurants:"
for restaurant, rating in sorted(rest_dict.items()):
    print "Restaurant %s is rated at %s" % (restaurant, rating) 
