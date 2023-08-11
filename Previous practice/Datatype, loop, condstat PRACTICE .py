# first_num = 10
# second_num = 20
# addition = first_num + second_num
# print(addition)
# print(first_num ** second_num)

# print(bin(2))
# print(bin(2>>1))
# print((bin(2<<1)))

# num1= 100
# num2= 200
# if num1 > num2 :
#     print("num1 is greater")
# elif num1<num2 :
#     print('num2 is greater')
# else:
#     print("both values are same")

# l=[1,2,3,4,5]
# for value in l:
#     print(value)

# l=[1,2,3,4,5]
# sum=0
# for value in l:
#     sum=sum+value
#     print(sum)                     #just the difference of indentation

# l=[1,2,3,4,5]
# sum=0
# for value in l:
#     sum=sum+value
# print(sum)                     #just the difference of indentation

# sum=0
# for value in range(10,60,10):
#     sum=sum+value
#     print(sum)

# ****************************************** Assignment 01 ******************************************
# Print numbers which are divisible by 7 and  5 and between 1500 to 2700
# count=1
# for value in range(1500,2701):
#     if value % 5==0 and value % 7==0:
#         print("The elements is" , value)
#         count= count +1
#     else:
#         continue
# else:
#     print("No element exist")
# print("The total numbers are ", count)

# ****************************************** Assignment 02 ******************************************
# #Print the number of even and odd numbers in a series from 1-9
# counteven=0
# countodd=0
# for value in range(1,10):
#     if value % 2 == 0:
#         counteven+=1
#     else:
#         countodd+=1
# print("The total even numbers are", counteven)
# print("The total odd numbers are", countodd)

# ****************************************** Assignment 03 ******************************************
#Print numbers from 1-50, for multiples of 3 print Fizz,
#for multiples of 5 print Buzz, for multiple of 3 and 5 print FizzBuzz
#
for value in range(1,51):
    if value % 5 == 0 and value % 3 == 0:
        print("FizzBuzz")
    elif value % 3 == 0:
        print("Fizz")
    elif value % 5 == 0:
        print("Buzz")
    else:
        print(value)

# ****************************************** Assignment 04 ******************************************
#Calculate the sum and average of n integers number
# sum=0
# avg=0
# value=int(input("Enter a positive number: "))
# for val in range(1,value+1):
#     sum = sum + val
#     avg = sum / value
# print(sum)
# print(avg)

# ****************************************** Assignment 05 ******************************************
#Find the factorial of a number
# mult = 1
# value=int(input("Enter a positive number: "))
# for val in range(value, 1, -1):
#     mult = mult * val
# print(mult)