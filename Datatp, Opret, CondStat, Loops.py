age = 42
print(id(age))

age1 = 42
print(id(age1))
age = 43
print(id(age))
#we can see that even if the variables have changed, but if the value is same, we will still have the same memory location.

print(bin(2))
print(2>>1)
print(bin(1))
print(bin(2>>1))
print(bin(2<<1))

# Question 01 : Write a program to find those numbers which are divisible by 7 and 5, between 1500 and 2700
# Solution thinking
    # we have to use logical operator 'and' operator
    # range(1500,2701) -> 1500, 1501, 1502 ... 2700

list = []
for value in range(1500,2701):
    if (value%7==0) and (value%5==0):
        list.append(value)
print(list)









