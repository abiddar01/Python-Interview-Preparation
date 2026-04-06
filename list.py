



"""
duped = [1,3,2,1,4,3,5,2]
unique = list(dict.fromkeys(duped))
print(unique)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = [x for row in matrix for x in row]
print(result)

fruits = ['apple','banana','cherry']
for i, fruit in enumerate(fruits):
    print(f"{i} : {fruit}")
"""

"""
students = [['Ali',85],['Sara',92],['Umar',78],['Zara',95],['Bilal',88]]
#Sort students by score (highest first)
ranked = sorted(students, key=lambda s:s[1], reverse=True)
print(ranked)
#Get names of students who scored above 85
score = [n[0] for n in students if n[1]>85]
print(score)
#Find the highest and lowest score
num = [h[1] for h in students]
print(max(num),min(num))
#Compute the average score
score = [h[1] for h in students]
avg = sum(score) / len(score)
print(avg)
"""

"""
words = ['hello','world','python','interview','prep']

#Create a new list of word lengths
lengths = [len(w) for w in words]
print(lengths)

#Create a list of all words in uppercase
uppercase = [w.upper() for w in words]
print(uppercase)

#Create a list of (word, length) tuples
tuples = [(w,len(w)) for w in words]
print(tuples)

#Filter to only words longer than 4 chars, then uppercase them
WORDS = [x.upper() for x in words if len(x)>4]
print(WORDS)
"""

"""
numbers = [3, 8, 15, 2, 42, 7, 19, 24, 11, 36]

# Even numbers
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [8, 2, 42, 24, 36]

# Greater than 10
big = [x for x in numbers if x > 10]
print(big)    # [15, 42, 19, 24, 11, 36]

# Divisible by 3
div3 = [x for x in numbers if x % 3 == 0]
print(div3)   # [3, 15, 42, 24, 36]

# Even AND > 15
result = [x for x in numbers if x % 2 == 0 and x > 15]
print(result) # [42, 24, 36]

"""

"""
nums = [10, 20, 30, 40, 50, 60, 70]

# Index 2 to 5 inclusive
print(nums[2:6])    # [30, 40, 50, 60]

# Every other element
print(nums[::2])    # [10, 30, 50, 70]

# Reverse without .reverse()
print(nums[::-1])   # [70, 60, 50, 40, 30, 20, 10]

# Last 3 elements
print(nums[-3:])    # [50, 60, 70]

"""

"""
fruits = ['apple','banana','cherry','date','elderberry']

print('First element:', fruits[0])
print('Last element:', fruits[-1])

print('Length:', len(fruits))

if 'mango' in fruits:
    print('There is mango in fruits')
else:
    print('There is no mango in fruits')

fruits.append('fig')
fruits.insert(2, 'grape')

fruits.remove('banana')

print('Updated list:', fruits)

"""



"""
i = 0
list = []
while i<3:
    i+=1
    film = str(input("Enter your fav movies names: "))
    list.append(film)

print('movies',list)
"""

"""
list1 = [1,2,'list',2,1]
list2 = list1.copy()

i = 0
j = len(list1)-1
size = j
while i<=size:
    if list1[i]==list2[j]:
        result = 'list is a palindrome'
    else:
        result = 'list is not palindrome'
        break
    i+=1
    j-=1

print(result)
"""

"""
list1 = [1,2,3,2,1]
list2 = list1.copy()

list2.reverse()

if list1==list2:
    print('yes')
else :
    print('no')
"""

