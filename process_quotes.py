#------ Read quotes into a list ------#
file = open("quotes.txt")
lines_list = file.readlines()
file.close()

#------ Sort by quote ------#
lines_list.sort()

sorted_quote = open("quotes_1.txt", "a")

for x in lines_list:
    sorted_quote.write(x)

sorted_quote.close()

#------ Sort by author ------#

def by_author(line):
    fields = line.split(" ; ")
    return fields[1]

lines_list.sort(key = by_author)

sorted_author = open("quotes_2.txt", "a")

for x in lines_list:
    sorted_author.write(x)

sorted_author.close()
