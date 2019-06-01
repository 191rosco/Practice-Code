#Conditionals Practice

#Easy
#Write a program to check if a number is less than 10.
x = 3
y = 300
z = 10
a = 100
if x<10:
    print("less than 10")

print(x)

#Medium
#Write a program to check if a given number is odd or even. ( % Symbol gives the decimal value of a division, use to define odd and even.)

if y%2 ==0:
    print("Even number")
elif y%2 >0:
    print("Odd number")

print(y)

#Hard
#Write a program to check if a number is divisible by both 10 and 50. If it is divisible by 30 as well print "This number is divivisible by 10, 50 and 30". If not, print "This number is divisible by 10 and 50 but not 30"

if y%10 ==0:
    if y%50 ==0:
        if y%30 ==0:
            print("This number is divivisible by 10, 50 and 30")
elif y%10 ==0:
    if y%50 ==0:
        print("This number is divisible by 10 and 50 but not 30")

print(y)

#End
