# Assignment 11: Exploring Sets
# You will pick yourself and one other family member.
# You identify 10 favorite words (sets) for each
# You will then compute the union, intersection, difference,
# and symmetric_difference between these sets.
# You print out results.



# TODO: You need to implement these four methods

# union method
def set_union(x,y):

    return x | y

# intersection method
def set_intersection(x,y):

    return x & y

# difference method
def set_difference(x,y):

    return x - y


# symmetric_difference method
def set_symmetric_difference(x,y):
    return x ^ y


# we will setup the test cases here
# TODO: fill in the sets with 10 words in each set

# ask user for my words separated by space
# convert user input into a list
# convert user input into a set
my_initial_words = input("Enter a list of 10 words for me separated by a space")
my_words_list = my_initial_words.split()
my_words = set(my_words_list)

# repeat same steps for mom words
mom_initial_words = input("Enter a list of 10 words for mom separated by a space")
mom_words_list = mom_initial_words.split()
mom_words = set(mom_words_list)


#Now call the methods and print the results
our_union = set_union(my_words, mom_words)
our_intersection = set_intersection(my_words, mom_words)
me_mom_difference = set_difference(my_words, mom_words)
mom_me_difference = set_difference(mom_words,my_words)
our_symmetric_difference = set_symmetric_difference(my_words,mom_words)

# Now print the output/results
print("UNION: List of words that exists in my set or my mom's set")
print(*our_union)

print("INTERSECTION: List of words that exists both sets")
print(*our_intersection)

print("DIFFERENCE 1: List of words that are exclusive to me")
print(*me_mom_difference)

print("DIFFERENCE 2: List of words that are exclusive to my mom")
print(*mom_me_difference)

print("SYMMETRIC DIFFERENCE: List of words that do not have any overlap")
print(*our_symmetric_difference)
