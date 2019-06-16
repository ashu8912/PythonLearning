nums=[1,2,3]
doubledNums=[x*10 for x in nums]
print(doubledNums)
name="ashu"
upperName=[char.upper() for char in name]
print(upperName)
#List comprehension with conditional logic
numbers=[1,2,3,4,5,6]
even=[num for num in numbers if num%2==0]
print(even)
odd=[num for num in numbers if num%2!=0]
print(odd)
#do half of even indexes and double of odd
newList=[num/2 if num%2==0 else num*2 for num in numbers]
print(newList)
#remove all vowels
sentence="python is great and i am enjoying it."
without_vowel=''.join([char for char in sentence if char not in "aeiou"])
print(without_vowel)