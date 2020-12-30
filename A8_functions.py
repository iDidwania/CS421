#Assignment 8: Implement isPalindrome and isAnagram methods
#Assignment 8: Test for both positive and negative cases

def  isPalindrome(word):
    
    #reverse the string
    reverse_string = reversed(word)
    
    #return the reversed equal to the original
    #if they are equal, it will return true
    #else, it will return false
    return(list(word) == list(reverse_string))

def  areAnagrams(word_1, word_2):
    
    #convert word_1 into a list
    list_word_1 = list(word_1)
    
    #sort the list in ascending order
    list_word_1.sort()
    
    #convert word 2 into a list
    list_word_2 = list(word_2)
    
    #sort the list in ascending order
    list_word_2.sort()
    
    #return the values equal to each other
    #if they are equal, then it will return true
    #else, it will return false
    return(list_word_1 == list_word_2)
    

#  Test cases for the two functions

# Palindrome positive test cases
# radar, level, rotor, kayak, racecar, madam
x = isPalindrome("radar")
print("Is radar a palindrome? = ",  x)

# Palindrome negative test cases
# python, java, silc
x = isPalindrome("python")
print("Is python a palindrome? = ",  x)


# Anagram positive test cases
# evil=vile,  silent=listen,  eleven plus two=twelve plus one
word_x = "evil"
word_y = "vile"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y," anagrams? = ", result)


# Anagram negative test cases
# python = pxthon, java = lava, a = abcdefghijklmnopqrstuvwxyz
word_x = "python"
word_y = "pxthon"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y," anagrams? = ", result)
