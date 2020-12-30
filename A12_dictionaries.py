#A12: Halloween Candy
# Your code should only be between BEGIN and END.
# Please do not touch or change any other code.
# See the sample output your should try to get after your implementation.



# prints a dictionary; Prints both the keys and values
# try to sort the dictionary by keys
# output will be user friendly

def print_dictionary(d):

    #sort the list and print the values
    for i in sorted (d) : 
        print (i, "=", d[i])  

        
# adds two dictionaries into one
# keys will not be repeated
# values will be added
# a NEW dictionary will be returned

def add_dictionaries(d1,d2):

    new_dictionary = {}

    for key in d1:
        if key in d2:
            new_dictionary[key] = d1[key] + d2[key]
        else:
            new_dictionary[key] = d1[key]

    for key in d2:
        if key not in new_dictionary:
            new_dictionary[key] = d2[key]
            
    for i in sorted (new_dictionary) : 
        print (i, "=", new_dictionary[i]) 

        
# test data for my_candy_bag

my_candy_bag = {    
   "snickers" : 5,
   "butterfinger" : 3,
   "candycorn" : 10,
   "skittles" : 6,
   "twix" : 7
}

my_sisters_bag = {
   "starburst" : 5,
   "kitkat" : 6,
   "twix" : 8,
   "butterfinger" : 6,
   "candycorn" : 10
}



# derive our_combined_bag
print("")
print("[1] Our combined bag:")
print("=====================")
add_dictionaries(my_candy_bag, my_sisters_bag)

# print my_candy_bag
print("")
print("[2] My Candy Bag:")
print("=====================")
print_dictionary(my_candy_bag)

# print sisters_bag
print("")
print("[3] My Sister's Bag:")
print("=====================")
print_dictionary(my_sisters_bag)

