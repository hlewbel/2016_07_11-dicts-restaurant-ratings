""" Restaurant ratings program

restaurant-ratings.py opens and reads a file, and spits out ratings
alphabetically by restaurant.

all_restaurant_reviews - the whole dictionary of reviews
restaurant_review - a single review
restaurant - key for the review
"""

input_file = open("scores.txt")
all_restaurant_reviews = {}
#sorted_all_restaurant_reviews = []

for line in input_file:
    stripped_line = line.rstrip()
    restaurant_review = stripped_line.split(":")

# put each pair in dictionary then alphabetize
    all_restaurant_reviews[restaurant_review[0]]= restaurant_review[1]

# ask user for additional input

print "Please enter a new restaurant  and rating (ie: Buck's 3): "
user_input = raw_input()
user_input = user_input.split(" ")
all_restaurant_reviews[user_input[0]]= user_input[1]
print



#alphabetize - sorts by default on the keys, sorted returns a list
#print sorted(all_restaurant_reviews)
sorted_all_restaurant_reviews = sorted(all_restaurant_reviews)

#printed sorted list from dictionary of restaurants and reviews
for restaurant_sorted in sorted_all_restaurant_reviews:
    print "{} is rated at {}.".format(restaurant_sorted, 
        all_restaurant_reviews[restaurant_sorted])

input_file.close()
