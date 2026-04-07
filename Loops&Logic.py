# Number to words (partial)
"""
def number_to_words(n):
    
    numbers = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    
    if 1 <= n <= 19:
        print(numbers[n])
    else:
        return "Out Of Range"
    
number_to_words(10)
"""

# Sum of digits
"""
def sum(num):
    num = abs(num)
    total = 0

    while num>0:
        total += num%10
        num //= 10
    
    print(total)

num = int(input("enter num: "))
sum(num)
"""

# Find duplicates in a list
"""
num = [1,2,3,2,4,3,5]
unique = list(set(num))
print(unique)
"""

#FizzBuzz
i=1
while i<50:
    if i%3==0:
        print('Fizz') 
    elif i%5==0:
        print('Buzz') 
    elif i%5==0 and i%3==0:
        print('FizzBuzz') 
    else:
        print(i)
    i+=1