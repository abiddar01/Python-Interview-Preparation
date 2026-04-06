# Write a function that reverses a string, then write another that checks if a string is a palindrome (reads same forwards and backwards). Test with 'racecar', 'hello', 'madam'.
"""
def string_reverser(word):
    result = word[::-1]
    return result

def isPalindrome(word,result):
    if word==result:
        print(word,"is a Palindrome")
    else:
        print(word,"String is not a Palindrome")

word = "racecar"
reverse = string_reverser("racecar")
isPalindrome(word,reverse)
"""

# Count vowels & consonants
"""
def count(word):
    vowels = 0
    consonants = 0
    for w in word.lower():
        if w.isalpha():
            if w in "aeiou":
                vowels += 1
            else:
                consonants += 1
    
    print("Vowels: ",vowels,"Consonants: ",consonants)

count('abid')
"""

# Anagram check
"""
def anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        print("Both Strings are Anagram")
    else:
        print("Both Strings are not Anagram")

anagram('listen','silent')
"""

# First non-repeating character
"""
word = 'aabbcde'
for ch in word:
    if word.count(ch) == 1:
        print(ch)
        break
"""



