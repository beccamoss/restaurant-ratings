# """Restaurant rating lister."""


# import sys

# ratings = {}

# with open(sys.argv[1]) as file_name:

#     for line in file_name:
#         line = line.rstrip()
#         restaurant, rating = line.split(":")
#         ratings[restaurant] = rating

# sorted_restaurants = sorted(ratings.keys())

# for restaurant in sorted_restaurants:
#     print "{} is rated at {}.".format(restaurant, ratings[restaurant])



## Allowing the user to Add Ratings 

"""Restaurant rating lister."""


# import sys

# ratings = {}

# with open(sys.argv[1]) as file_name:

#     for line in file_name:
#         line = line.rstrip()
#         restaurant, rating = line.split(":")
#         ratings[restaurant] = rating

# user_restaurant = raw_input("What restaurant would you like to rate? ")
# user_rating = raw_input("What would you like to rate {}? ".format(user_restaurant))
# ratings[user_restaurant] = user_rating

# sorted_restaurants = sorted(ratings.keys())

# for restaurant in sorted_restaurants:
#     print "{} is rated at {}.".format(restaurant, ratings[restaurant])



## Further study


import sys

ratings = {}

with open(sys.argv[1]) as file_name:

    for line in file_name:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings[restaurant] = rating

user_restaurant = raw_input("What restaurant would you like to rate? ")

while True:
    user_rating = raw_input("What would you like to rate your restaurant? Please choose a number between 1 and 5. ")
    if user_rating.isalpha() or float(user_rating) not in range(1, 6):
        print "Invalid rating.  Try again. "
    else:
        break

ratings[user_restaurant.capitalize()] = user_rating

sorted_restaurants = sorted(ratings.keys())

for restaurant in sorted_restaurants:
    print "{} is rated at {}.".format(restaurant, ratings[restaurant])



