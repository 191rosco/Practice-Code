#Tuple Practice

#Easy
#Write a program to create a tuple with 4 elements.

RandomDOB = ("13.02.1991", "18.06.1897", "31.06.1996", "01.12.2012")
print(RandomDOB)

#Medium
#Convert the tuple to a list.

edit1 = list(RandomDOB)
print(edit1)

#Hard
#Now delete the first element in the list and convert back to a tuple.

edit1.remove("13.02.1991")
print(edit1)
RandomDoB = tuple(edit1)
print(RandomDoB)
