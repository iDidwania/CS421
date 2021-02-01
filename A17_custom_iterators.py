# Exploring the custom iterators

# Create a 'book' class
class Book:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "Name: " + self.name + " Author: " + self.author
    
    def __repr__(self):
        return "Name: " + self.name + " Author: " + self.author


# Create a BackPack class
# This holds a collection of books
# Internal iterator is also implemented
class BackPack:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return books.__str()

    def __repr__(self):
        return books.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.books)):
            current_book = self.books[self.x]
            self.x = self.x+1
            return current_book
        else:
            raise StopIteration


# Create some books
b1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
b2 = Book("The Lord of the Rings", "J. R. R. Tolkien")
b3 = Book("The Hunger Games", "Suzanne Collins")
b4 = Book("Percy Jackson", "Rick Riordan")

#create a list of books
books = [b1,b2,b3,b4]

# Create back_pack object
back_pack = BackPack(books)

# Call the for loop on back_pack
print("--> Calling internal iterator")
for x in back_pack:
    print(x)

