#List Practice

#Easy
#Write a program to create a list with 5 items.

Family_list = ["Ross", "Austin", "taylor", "Margaret", "George"]
print(Family_list)

#Medium
#Update the 3rd element of the list.

Family_list.remove('taylor')
print(Family_list)
Family_list.insert(2, 'Taylor')
print(Family_list)

#Hard
#Create another list of 3 elements. Now create a final result as a concatenation of the first two lists.

Dog_list = ["bigjack", "weejack", "wabajack"]
print(Dog_list)
Family_and_dogs_list = Family_list + Dog_list
print(Family_and_dogs_list)
