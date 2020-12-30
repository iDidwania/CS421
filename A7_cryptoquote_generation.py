# Get the quote. This is the input.
quote = input("Enter a quotation: ")
print("\n")

# [1] I need a list of all letters from the input quote
#https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-an-array-of-characters-in-python

# since cryptoquotes deal with only upper case letters
# let us make a temporary string to hold the upper-cased quote
quote_upper = quote.upper()

#convert quote_upper into a list
quote_list = list(quote_upper)

# create a temporary quote_list_temp for holding the swaps
quote_list_temp = list(quote_list)

# [2] We need an alphabet list which is ordered
# How do I create a ordered list of alphabest? 
#https://www.geeksforgeeks.org/python-ways-to-initialize-list-with-alphabets/

#import the string module
import string

# initializing empty list  
ordered_list = [] 
  
# using string module for filling alphabets 
# Since all cryptograms are not case sensitive, 
# let us go with upper case
ordered_list = list(string.ascii_uppercase) 

# [3]. We need a randomized list
# How do I randomize this ordered list 
# so that I can maintain the mapping
# between original (ordered) and the randomized list

import random

# make a copy of the original list
random_list = list(ordered_list);

#using the raondom module to shuffle (randomize) the input list
random.shuffle(random_list);

# All your code goes between BEGIN and END lines.

# BEGIN ============= Student Code ============

#[4]  We will now create the crypto quote
#   per the psedo-code given below

# we now have these four lists
#  quote_list
#  quote_lit_temp
#  ordered_list
#  random_list
# 
# Our algorithm depends on all these lists

# we need to keep track of the position 
# at which we are doing the substitution
q_pos = -1

# start the for loop on the quote_list
for x in quote_list:
    
    # bump up the position for the character
    # this is the character we are currently processing
    # increment q_pos by 1
    q_pos = q_pos + 1    
    
    # we need to swap only the characters
    # symbols and characters can be ignored
    # Check whether x is in the ordered list
    if x in ordered_list:
        
         # get the position of the character in the ordered list
         # the x_pos should be between 0 and 25
        x_pos = ordered_list.index(x)
        
        # Now find out our mapping letter for the substitution
        y_char = random_list[x_pos]
        
        # Now do the swap in the quote_list_temp
        quote_list_temp[q_pos] = y_char

# END ============== Student Code ============


#5. We need to convert the quote_list_temp (the cryptoquote) to a string
# How do I convert a list into a string?
# see  https://www.geeksforgeeks.org/jin-function-python/
# Variables for holding the final crypto quote
# We are joining the list into a single string

crypto = ""
crypto = crypto.join(quote_list_temp)

#6. We need to show one hint to the users.
# Since quote_list_temp contains the cryptic character
# and the quote_list contains the original character
# We can simply show the first character mapping from both the lists
hint = "Hint => " + quote_list_temp[0] + " = " + quote_list[0]



# All previous print statements can be commended 
# once the program is working.

#6 Now print all the variables in the end
# to verify that our algorithm is working
#print the quote
print("========== Your quote: ============ ")
print(quote,"\n")


#print the crypto
print("========== Crypto quote: ============ ")
print(crypto,"\n")
print(hint)
